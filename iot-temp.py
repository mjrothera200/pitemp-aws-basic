import paho.mqtt.client as paho
import json
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import ssl


ca = "/home/pi/dev/iot-temp/pitemp-aws-basic/AmazonRootCA1.pem" 
cert = "/home/pi/dev/iot-temp/pitemp-aws-basic/bf1cf3d223-certificate.pem.crt"
private = "/home/pi/dev/iot-temp/pitemp-aws-basic/bf1cf3d223-private.pem.key"



# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 17
instance = dht11.DHT11(pin=17)

# extract the serial number
cpuserial = "0000000000000000"
try:
    f=open('/proc/cpuinfo', 'r')
    for line in f:
        if line[0:6]=='Serial':
            cpuserial = line[10:26]
    f.close()
except:
    cpuserial="ERROR000000000"

print("CPU Serial # is %s" % (cpuserial))

#aws_iot_endpoint = cpuserial+".iot.us-east-1.amazonaws.com" # <random>.iot.<region>.amazonaws.com
aws_iot_endpoint = "data.iot.us-east-1.amazonaws.com" # <random>.iot.<region>.amazonaws.com
IoT_protocol_name = "x-amzn-mqtt-ca"
url = "https://{}".format(aws_iot_endpoint)

# --------------- #
# Callback events #
# --------------- #

# connection event
def on_connect(client, data, flags, rc):
    print('Connected, rc: ' + str(rc))

# connection event

def on_disconnect(client, data, rc):
    print('Disonnected, rc: ' + str(rc))

# subscription event
def on_subscribe(client, userdata, mid, gqos):
    print('Subscribed: ' + str(mid))

# received message event
def on_message(client, obj, msg):
    print(msg.topic)
# ------------- #
# MQTT settings #
# ------------- #

def ssl_alpn():
    try:
        #debug print opnessl version
        print("open ssl version:{}".format(ssl.OPENSSL_VERSION))
        ssl_context = ssl.create_default_context()
        #ssl_context.set_alpn_protocols([IoT_protocol_name])
        print("ca:{}".format(ca))
        ssl_context.load_verify_locations(cafile=ca)
        print("cert:{}".format(cert))
        print("private:{}".format(private))
        ssl_context.load_cert_chain(certfile=cert, keyfile=private)

        return  ssl_context
    except Exception as e:
        print("exception ssl_alpn()")
        raise e

if __name__ == '__main__':
    out_topic_environmentals = "environmentals"
    try:
        client = paho.Client()
        client.on_message = on_message
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_subscribe = on_subscribe
        ssl_context= ssl_alpn()
        client.tls_set_context(context=ssl_context)
        print("start connect: {}".format(aws_iot_endpoint))
        client.connect(aws_iot_endpoint, port=8883)
        print("connect success")
        client.loop_start()

        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            print("try to publish:{}".format(now))
            result = instance.read()
            if result.is_valid():
                temp_c = result.temperature 
                temp_f = (result.temperature * 9)/5 + 32 
                humidity = result.humidity 
                message = { 'd': {'temp_c': temp_c, 'temp_f': temp_f, 'humidity': humidity } }     
                client.publish(out_topic_environmentals, json.dumps(message))
            time.sleep(1)

    except Exception as e:
        print("exception main()")
        print("e obj:{}".format(vars(e)))
        print("message:{}".format(e.message))




