<h1 align="center"> Chatnet Hub </h1>

![Chat project cover](https://github.com/j0k3rD/real_time_chat_project/assets/83615373/f4528688-35b4-404a-bff3-5a271f48ae47)

Client-server application, which simulates a chat in real time, where users communicate in different already armed groups. It uses **django** and **microservices** to run user login and real-time chat.

## About
Chatnet Hub is a Real-time Chat project designed by us as work for our university subject __Ingenieria de Software__.

* Used tools:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) ![LINUX](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)  

## Architecture Graphic

  
```mermaid

flowchart TD

User[/User\]

Admin[/Admin\]

Login[Login]

Chat[Group Chat]

Register[Register]

Database[(User/Chat)]

User --> Login

Login -- login --> Chat

Login -- Register --> Register

Chat -- get/set chat --> Database

Register -- set user --> Database

Register -- login --> Chat

Admin -- get/set/from chat and user ----> Database

```
 
- The user can only write in the chat once logged into the system.
- The user can register in case of not having an account.
- The admin is in charge of managing the database through the **Django** admin interface, adding or removing both users and chat groups in the system.
- Both the Chat microservice and the User microservice use their own database.

#
Credits:
- Developers: 
     * [<i>Aaron Moya</i>](https://github.com/j0k3rD)
     * [<i>Nicolas Mayoral</i>](https://github.com/NKAmazing) 
     * [<i>Marcos Miglierina</i>](https://github.com/XxRaXoRxX)
     * [<i>Alexis Lino</i>](https://github.com/AlexSTM2)

- Instructor: Pablo Prats

- Institution: [<i>Universidad de Mendoza - Facultad de Ingenieria</i>](https://um.edu.ar/ingenieria/)

![um-cover](https://user-images.githubusercontent.com/83615373/235419081-c36fcb36-c412-4317-b40a-7cad5e937339.png)
