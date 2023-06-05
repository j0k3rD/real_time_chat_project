<h1 align="center"> Chatnet Hub </h1>

![Chat project cover](https://github.com/j0k3rD/real_time_chat_project/assets/83615373/f4528688-35b4-404a-bff3-5a271f48ae47)

Client-server application, which simulates a chat in real time, where users communicate in different already armed groups. It uses **django** and **microservices** to run user login and real-time chat.

## About

![Ing Software cover](https://github.com/j0k3rD/real_time_chat_project/assets/83615373/2503b6f6-8f01-4cce-89f9-29b51f6deac2)

<h3 align="center">

*Ingenieria de Software*
  
</h3>

Chatnet Hub is a Real-time Chat project designed by us as a part of work for our university subject __Ingenieria de Software__. 

We were asked to carry out a project built with microservices connected to each other using a Framework for the project structure and Docker containers for the DevOps management service.

* Tools used in the development of the project:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) ![VS CODE](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white) ![LINUX](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![WINDOWS](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![JAVASCRIPT](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![REACT](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)  

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
