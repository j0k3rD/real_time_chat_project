@echo off
cd user_service/
docker build -t userservice:v0.6.0 .
cd ..
pause