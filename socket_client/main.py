# Made by Guilherme Claudino on July 2022. 
import sys
import os
import PySide2
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QUrl, QObject, QTimer
from PySide2.QtQuick import QQuickView
import threading
import socket
import time

# Function to be called after the QTimer timeout
def updateText(temperature, passedTime):
    txt.setProperty("text", "Current Temperature [°C]: \n" + temperature + "\n" + "Executing for " + passedTime + "s")
###

# Client side of socket
def sockClient():
    # Define the connection
    HOST = "10.22.1.113" 
    PORT = 1997
    ###

    # Reuses some global variables
    global curr_time
    global temp_str
    ###

    curr_time = 0
    
    # Start the connection and receive the temperature
    print('Connecting')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Connected')
        while True:
            s.send(b"Hello, world")
            data = s.recv(1024)
            temp_str = data.decode('utf-8')
            time.sleep(1)
            curr_time = curr_time+1
            print(temp_str)
    ###
###

# Simple script to hide one window and show another
def changePage(myWindow):
    global currWindow
    if(myWindow == 0):
        view2.show()
        view.hide()
        currWindow = 1
    else:
        view.show()
        view2.hide()
        currWindow = 0
###


# Main QT App
if __name__ == "__main__":
    # Define the main QT Objects
    app = QApplication(sys.argv)
    view = QQuickView()
    view2 = QQuickView()
    qml = QUrl("Qml_qt_design.qml")
    qml2 = QUrl("Qml_demo_second_window.qml")
    ### 
 
    # Define the two views
    view.setSource(qml)
    view.show()
    view2.setSource(qml2)
    view2.hide()
    ###

    # Define the global variables
    global txt
    global curr_time
    global currWindow
    global temp_str
    temp_str = ""
    curr_time = 0
    currWindow = 0
    ###

    # Start the socket thread
    clientThread = threading.Thread(target=sockClient, name="Socket Client")
    clientThread.start()
    ###

    # Define other useful QT Objects
    root = view.rootObject()
    root2 = view2.rootObject()
    title = root.findChild(QObject, "title")
    mainbutton = root.findChild(QObject, "mainButton")
    mainbutton2 = root2.findChild(QObject, "mainButton")
    txt = root.findChild(QObject,"Temp")
    txtOS = root2.findChild(QObject, "textOS")
    ###

    # cat /etc/os-release of the container
    with open("/etc/os-release") as cat_os:
        osinfo = cat_os.read()
    txtOS.setProperty("text",osinfo)
    ###
    
    # Change Windows
    mainbutton.clicked.connect(
        lambda: changePage(currWindow))

    mainbutton2.clicked.connect(
        lambda: changePage(currWindow))
    ###

    # Timer to constantly update the temperature text
    text_timer = QTimer()
    text_timer.timeout.connect(
        lambda: updateText(temp_str, str(curr_time))
    )
    text_timer.start(1000)
    ###

    sys.exit(app.exec_())
###