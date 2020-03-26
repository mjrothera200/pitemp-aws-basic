# Raspberry PI Temperature with AWS - Basic MQTT 

The goal of this project is to provide a very simple method of getting started with AWS and an MQTT client using a real sensor.  I have selected a DHT11 Temperature and Humidity sensor given the simplicity of how to wire the solution.  

**This is not meant to be an all-inclusive tutorial to Watson IoT connectivity, but a simple "getting started".  To learn aout the platform and other options for connectivity, please refer to the Watson IoT documentation**

**Special thanks for the code already included in this repository that helps read the sensor values from the DHT11**
https://github.com/szazo/DHT11_Python.git

Raspberry PI Dependencies

1.  Python 3

```console
python3 --version
```

2.  There may be packages you need to install:

```console
sudo pip3 install paho-mqtt
```

## Step 1:  Wire the DHT 11 Sensor to your PI

Follow the instructions here:
https://www.instructables.com/id/DHT11-Raspberry-Pi/

Some hints:
1.  You can do this with simply the DHT11 and 3 Female to Female jumper wires
2.  If you hold the raspberry pi such that the USB inputs are on the right and the Pins are on the top:
    * Wire the first pin on the bottom row to the VCC of the DHT11 - This is 3.3V power
    * Wire the second pin on the top row to the ground (GND) of the DHT11 - this is the ground 
    * Wire the third pin on the 6th pin on the bottom row to the DATA of the DHT11 - this is GPIO Pin 17

## Step 2:  Verify the DHT 11 is working properly

Run the following command to verify that you are receiving values:

```console
python3 dht11_example.py
```

Verify that the temperature and humidity readings are displayed.


```console
Last valid input: 2019-12-17 10:33:59.947765
Temperature: 18.3 C
Temperature: 64.9 F
Humidity: 39.0 %
```

## Step 3:  Sign up for IBM Cloud and Create an IoT Service

1. Sign up for the IBM cloud from this link: 
https://www.ibm.com/cloud
2. After you go through the registration process, login with your IBM ID.
3. Create an instance of the IoT service by clicking "Create Resource" and searchign for IoT
4.  Select "Internet of Things Platform" and a pricing plan (Lite plan or Free works fine to get started)
5.  Launch the Internet of Things platform dashboard.      
**Important:  Take note of your Organization ID which is a 6 character identifier in the upper right hand corner above your name**

## Step 4:  Create a Device Type called "pitemp"

1.  Navigate to Devices and "Create a Device Type".    
**You can name it whatever you want, but the program here uses the device type called "pitemp"**

## Step 5:  Create a new Device called "pi1"

1.  Create a Device Type called "pi1" which is of type "pitemp"
**Again, you can name it whatever you want, but this program assumes the device identifier of "pi1"**

2.  As you walk through the work flow to create a device, it will ask you to generate a device token or type one.  It is generally safer and more secure to have the system automatically create one, but for this exercise just type "12345678".  This token is embedded in the program and is part of the authentication part of the process.  

## Step 6:  Customize your Configuration Values in the Python Script

1.  Edit the program and put it in your specific credentials.  
    * The path to the cert. This must be an absolute path - where you are running this program on the PI
    * Your organization:  The 6 character identification
    * The device token if different than 12345678

```python
# device credentials
ca_absolute_path = '/home/pi/dev/iot-temp/pitemp-wiot-basic/messaging.pem'
iotidentifier = 'pi1'
iotorg = 'cg3orm'
iottype = 'pitemp'

device_id        = 'use-token-auth'      # * set your device id (will be the MQTT client username)
device_secret = '12345678'
random_client_id = 'd:'+iotorg+':'+iottype+':'+iotidentifier      # * set a random client_id (max 23 char)
```

## Step 7:  Run the Program
 

```console
python3 iot-temp.py
```

## Step 8:  Monitor Results in Watson IoT

1.  Navigate to your device under Devices.  Verify that the device shows "Connected"
2.  Navigate to "Recent events" to watch the live JSON IoT data arrive


Enjoy!

Matt Rothera


## License

This project is licensed under the terms of the MIT license.
