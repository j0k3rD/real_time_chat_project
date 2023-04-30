@echo off
cd user_service/
docker build -t userservice:v0.4.0 .
cd ..
pause