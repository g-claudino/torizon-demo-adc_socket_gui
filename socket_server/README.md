This is the socket server side application. 

It runs inside a docker container in Torizon that was designed following this architecture:

![image](https://user-images.githubusercontent.com/34245682/178801498-da67f04f-29bc-4dcd-9f13-ef9f7be8f2c2.png)

The SoM starts a container that depends mainly on the following libs: libgpiod, socket and threading. Other libs such as math were added for data treatment. The code then starts a thread for a socket server and in paralel, gets ADC input to calculate the actual temperature output from a Thermistor. 

If the connection is succesful, a GPIO will be toggled and temperature will be sent. 
