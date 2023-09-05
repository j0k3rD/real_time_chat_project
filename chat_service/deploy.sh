#!/bin/bash

source .env
# Create group and repository

if [ $(az group exists --name $GROUPREPOSITORY) = true ]; then
    echo "[!] Resource group $GROUPREPOSITORY already exists"
else
    az group create --name $GROUPREPOSITORY --location $LOCATION
fi

if [ $(az acr check-name --name $ACR_NAME --query "nameAvailable" -o tsv) = false]; then
    echo "[!] Repository $ACR_NAME already exists"
else
    az acr create --resource-group $GROUPREPOSITORY --name $ACR_NAME --sku Basic --admin-enabled true
fi

az acr login --name $ACR_NAME
ACR_REGISTRY_ID=$(az acr show --name $ACR_NAME --query "id" --output tsv)
USER_NAME=$(az ad sp list --display-name $SERVICE_PRINCIPAL_NAME --query "[].appId" -o tsv)
PASSWORD=$(az ad sp create-for-rbac --name $SERVICE_PRINCIPAL_NAME --scopes $ACR_REGISTRY_ID --role acrpull --query "password" -o tsv)

docker build -t $APP_IMAGE:$TAG .
docker tag $APP_IMAGE:$TAG $ACR_NAME.azurecr.io/$APP_IMAGE:$TAG
docker images
docker push $ACR_NAME.azurecr.io/$APP_IMAGE:$TAG

az acr repository list --name $ACR_NAME --output table
az container create --resource-group $GROUPREPOSITORY --name $APP_IMAGE --image $ACR_NAME.azurecr.io/$APP_IMAGE:$TAG --cpu 1 --memory 1 --registry-login-server $ACR_NAME.azurecr.io --registry-username $USER_NAME --registry-password $PASSWORD --ip-address Public --dns-name-label dns-um-$RANDOM --ports 5000