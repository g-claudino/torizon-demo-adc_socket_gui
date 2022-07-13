This is the client side of the application:

It runs inside a docker container in Torizon that was designed following this architecture:

![image](https://user-images.githubusercontent.com/34245682/178802376-965e4937-a1be-4ee4-b037-64ccfdc68081.png)

The SoM starts a container responsible for setting up a GUI using QT and PySide2. This container depends on the socket library to receive data from the server and update it to the GUI. 
