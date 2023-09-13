#!/bin/bash

# Import variables
source .env

# Validate variables
if [ -z "$GROUPREPOSITORY" ] || [ -z "$ACR_NAME" ] || [ -z "$LOCATION" ] || [ -z "$SERVICE_PRINCIPAL_NAME" ] || [ -z "$APP_IMAGE" ] || [ -z "$TAG" ]; then
    echo "[ERROR] Undefined or empty variables. Check your variables."
    exit 1
fi

# Check if necessary tools are available
if ! command -v "$DOCKER_CMD" &> /dev/null; then
    echo "[ERROR] Docker is not installed. Install it and try again."
    exit 1
fi

if ! command -v "$AZ_CMD" &> /dev/null; then
    echo "[ERROR] Azure CLI is not installed. Install it and try again."
    exit 1
fi

# Create resource group and repository
if [ "$($AZ_CMD group exists --name $GROUPREPOSITORY)" = true ]; then
    echo "[INFO] Resource group $GROUPREPOSITORY already exists."
else
    $AZ_CMD group create --name $GROUPREPOSITORY --location $LOCATION
fi

if [ "$($AZ_CMD acr check-name --name $ACR_NAME --query "nameAvailable" -o tsv)" = false ]; then
    echo "[INFO] Repository $ACR_NAME already exists."
else
    $AZ_CMD acr create --resource-group $GROUPREPOSITORY --name $ACR_NAME --sku Basic --admin-enabled true
fi

# Log in to the Azure Container Registry
$AZ_CMD acr login --name $ACR_NAME
ACR_REGISTRY_ID="$($AZ_CMD acr show --name $ACR_NAME --query "id" --output tsv)"
USER_NAME="$($AZ_CMD ad sp list --display-name $SERVICE_PRINCIPAL_NAME --query "[].appId" -o tsv)"
PASSWORD="$($AZ_CMD ad sp create-for-rbac --name $SERVICE_PRINCIPAL_NAME --scopes $ACR_REGISTRY_ID --role acrpull --query "password" -o tsv)"

# Build and push the Docker image
$DOCKER_CMD build -t $APP_IMAGE:$TAG .
$DOCKER_CMD tag $APP_IMAGE:$TAG $ACR_NAME.azurecr.io/$APP_IMAGE:$TAG
$DOCKER_CMD images
$DOCKER_CMD push $ACR_NAME.azurecr.io/$APP_IMAGE:$TAG

# List repositories in the Azure Container Registry
$AZ_CMD acr repository list --name $ACR_NAME --output table

# Create an Azure Container
$AZ_CMD container create --resource-group $GROUPREPOSITORY --name $CONTAINER_NAME --image $ACR_NAME.azurecr.io/$APP_IMAGE:$TAG --cpu 1 --memory 1 --registry-login-server $ACR_NAME.azurecr.io --ip-address Public --location $LOCATION --registry-username $USER_NAME --registry-password $PASSWORD --dns-name-label dns-um-$RANDOM --ports 6000
