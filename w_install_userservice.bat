@echo off
cd user_service/
docker build -t userservice:v0.5.0 .
cd ..
pause