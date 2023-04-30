@echo off
cd chat_service/
docker build -t chatservice:v0.4.0 .
cd ..
pause