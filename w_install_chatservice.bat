@echo off
cd chat_service/
docker build -t chatservice:v0.7.0 .
cd ..
pause