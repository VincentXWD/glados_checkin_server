### Usage
0. 自行获取COOKIE
1. docker build -t glados_checkin . -f ./Dockerfile
2. docker run -dit --restart unless-stopped --name=glados_checkin -d glados_checkin "\<Your COOKIE\>"
