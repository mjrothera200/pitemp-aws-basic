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

## Step 3:  Sign up for AWS Cloud and Launch IoT Core

1. Sign up for the AWS cloud from this link: 
https://aws.amazon.com/
2. After you go through the registration process, login with your Amazon ID.
3. Launch the IoT Core service

## Step 4:  Create a Thing called "pitemp"

1.  Navigate to Manage click on the button "Register a Thing", and then "Create a Single Thing".
2.  In the name field type "pitemp1".  This will be the unique name of your device.
3.  In the "Apply a Type" field, hit the button to create a type and then:
    a.  for the type name, select "pitemp"
    b.  put a description of it, like "my raspberry pi temperature"
4.  Create a group in the next field - call it "mypitemps"
5.  Hit Next to the move to the next page.
6.  Create a set of certificates by hitting the button "Create Certificate"
7.  Next, download the following:
   a.  The three certificates: The Thing Certificate, Public, and Private Key
   b.  The Root CA for AWS. (Amazone Root 2048 CA will work fine).
8.  Put all of these certificates into the directory of this program wherever you have it on your Raspberry PI
   

## Step 5:  Customize your Configuration Values in the Python Script

1.  Edit the "iot-temp.py" and make sure the directory path points to the location of the certificates.  Make sure they are all absolute paths

## Step 6:  Run the Program
 

```console
python3 iot-temp.py
```

## Step 7:  Monitor Results in AWS

1.  Navigate to your device under Devices.  Verify that the device shows "Connected"
2.  Navigate to "Recent events" to watch the live JSON IoT data arrive


Enjoy!

Matt Rothera


## License

This project is licensed under the terms of the MIT license.
