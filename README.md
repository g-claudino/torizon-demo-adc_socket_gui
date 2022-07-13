# torizon-demo-adc_socket_gui
Repository containing the files to set up a custom demo with TorizonCore. TorizonCore Version used was 5.6.0 for the Demos Preparation. The following picture describes the overall structure intended for this project:

![image](https://user-images.githubusercontent.com/34245682/178584934-379499ec-19eb-44a4-ac5d-ca4dd2d6f8df.png)

The idea is to have two modules running TorizonCore each with their own docker containers. One module, would be responsible to gather external data using ADC and use GPIO for additional functions. The other, would be responsible to generate a GUI. The modules would communicate through socket and there are also threads being created inside the containers to better divide functions and allow it to work on separate loops. 

This is a work in progress, so many of the codes may not be bugless. Please feel free to interact with it if you wish to. 

# Socket Server Side

It runs inside a docker container in Torizon that was designed following this architecture:

![image](https://user-images.githubusercontent.com/34245682/178801498-da67f04f-29bc-4dcd-9f13-ef9f7be8f2c2.png)

The SoM starts a container that depends mainly on the following libs: libgpiod, socket and threading. Other libs such as math were added for data treatment. The code then starts a thread for a socket server and in paralel, gets ADC input to calculate the actual temperature output from a Thermistor. 

If the connection is succesful, a GPIO will be toggled and temperature will be sent. 

# Socket Client Side

It runs inside a docker container in Torizon that was designed following this architecture:

![image](https://user-images.githubusercontent.com/34245682/178802376-965e4937-a1be-4ee4-b037-64ccfdc68081.png)

The SoM starts a container responsible for setting up a GUI using QT and PySide2. This container depends on the socket library to receive data from the server and update it to the GUI. 
