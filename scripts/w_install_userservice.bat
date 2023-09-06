@echo off
cd user_service/
docker build -t userservice:v0.7.0 .
cd ..
pause