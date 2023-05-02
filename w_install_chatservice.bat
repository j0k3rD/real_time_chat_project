@echo off
cd chat_service/
docker build -t chatservice:v0.6.0 .
cd ..
pause