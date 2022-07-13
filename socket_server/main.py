# Made by Guilherme Claudino on July 2022. 
import socket
import os
import math
import time
import threading
import gpiod

def readAdc(path_adc, path_sample):
    # Define the base value and Sample
    with open(path_adc) as adc:
        adc_base = adc.read()
    with open(path_sample) as sample:
        adc_sample = sample.read()
    ###

    # Return the corrected value
    return float(adc_base)*float(adc_sample)/1000
    ###

def runServer():
    # Define the connection settings
    print('Server starting')
    HOST = "0.0.0.0" 
    PORT = 1997
    global message
    global connected
    ###

    # Wait for connection and send temperature message
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Waiting")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                connected = True
                if not data:
                    connected = False
                    break
                conn.send(message.encode('utf-8'))  
    ###
 
if __name__ == "__main__":
    # Create some variables and add print logs
    global message
    global connected
    connected = False
    print('working')
    ###

    # Starting the Socket Thread
    sockThread = threading.Thread(target=runServer, name="Sock Server")
    sockThread.start()
    ###

    # Define the ADC Information
    adc_dev = 'in_voltage4_raw'
    adc_sample = 'in_voltage_scale'
    iio_number = '0/'
    base_path = '/sys/bus/iio/devices/iio' + ':' + 'device'
    ###
    
    # Define the structure for the Temperature reading and do the first calculation
    Rin = 9500
    a = 1.5*10**(-4)
    b = 2.7*10**(-4)
    c = 10**(-6)
    Vin = 3.3
    Vout = readAdc(base_path + iio_number + adc_dev, base_path + iio_number + adc_sample)
    Rout = Rin*(Vin/Vout-1)
    logR = math.log(Rout)
    temperature = (1.0 / (a + b * logR + c * logR * logR * logR))-273.5
    message = str(temperature)
    ###
    
    # Define the GPIO Chip and Configure it as Output
    chip = gpiod.chip("/dev/gpiochip0")
    gpioline = chip.get_line(7)
    config = gpiod.line_request()
    config.consumer="GPIO sample"
    config.request_type=gpiod.line_request.DIRECTION_OUTPUT
    gpioline.request(config)    
    ###

    # Main Loop
    while True:
        if connected:
            time.sleep(1)
            # Calculate temperature again if connected
            Vout = readAdc(base_path + iio_number + adc_dev, base_path + iio_number + adc_sample)
            Rout = Rin*(Vin/Vout-1)
            logR = math.log(Rout)
            temperature = (1.0 / (a + b * logR + c * logR * logR * logR))-273.5
            message = str(temperature)
            print(message)
            ###

            # Turn the LED On
            gpioline.set_value(1)
            ###
            if temperature < -50:
                break
        else:
            # If not connected turn the LED off
            gpioline.set_value(0) 
            time.sleep(1)
    ### END