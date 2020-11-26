import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO
from time import sleep
import urllib.request
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO_TRIGGER = 14
GPIO_ECHO = 15
ir = 16

CLK  = 11
MISO = 9
MOSI = 10
CS   = 8



GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(ir, GPIO.IN)


AcsValue=0.0
AcsValue1=0.0
Samples=0.0
Samples1=0.0
AvgAcs=0.0
AvgAcs1=0.0
Current1=0.0
Current2=0.0


current = 0.0
ir_read = 0
distance = 0
c=0.0

timeout = time.time() + 60*5


mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def fun_I():
    try:
        values = [0]*2
        global current
        Samples = 0
        Samples1 = 0
        for x in range (150):
            for i in range(2):
                values[i] = mcp.read_adc(i)
            AcsValue = values[0]
            AcsValue1 = values[1]
            Samples = Samples + AcsValue
            Samples1 = Samples1 + AcsValue1
            sleep(0.01)
            
        AvgAcs = Samples/150.0;
        AvgAcs1 = Samples1/150.0;
        
        Current1 = (2.5 - (AvgAcs * (5.0 / 1024.0)) )/0.066;
        Current2 = (2.5 - (AvgAcs1 * (5.0 / 1024.0)) )/0.066;

        print("Current 1 = ", round(Current1,2))
        print("Current 2 = ", round(Current2, 2))

        current = Current1-Current2

        if current < 0:
            current = current * (-1)
            
        print('Current Diff = ',round(current,2))

    except:
        print("\n Something Went wrong (fun_I)")



def fun_ir():
    try:
        global ir_read
        ir_read = GPIO.input(ir)
        if ir_read == False:
            ir_read = 1
        else:
            ir_read = 0
        print("IR detect = ",ir_read)
    except:
        print("\n Something Went wrong(fun_ir)")

def fun_distance():
    try:
        global distance
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        
        StartTime = time.time()
        StopTime = time.time()


        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()


        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()


        TimeElapsed = StopTime - StartTime

        distance = (TimeElapsed * 34300) / 2

        print ("Distance = ",round(distance,2))
        
    except:
        print("\n Something Went wrong(fun_distance)")


def IOT():
    try:
        request = urllib.request.Request("https://api.thingspeak.com/update?api_key=Z6D6Z9I4653LTKQ3"+"&field1=%s"%(current)+"&field2=%s"%(distance)+"&field3=%s"%(ir_read))                  
        urllib.request.urlopen(request)

    except:
        print("\n Check Network Connection (IOT)")


while True:
    try:
        a=time.time()
        
        fun_I()
        fun_ir()
        fun_distance()
        IOT()
        sleep(1)
        
        b=time.time()
        c=(c+(b-a))
        if c>15:
            c = 0.0
            IOT()
        
    except KeyboardInterrupt:
        print("Stopped by User")
        GPIO.cleanup()
