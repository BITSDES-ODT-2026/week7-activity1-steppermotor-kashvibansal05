#stepup motor clockwise and anticlockwise movement without using lists
from machine import Pin
import time

in1 = Pin(5, Pin.OUT)
in2 = Pin(14, Pin.OUT)
in3 = Pin(18, Pin.OUT)
in4 = Pin(19, Pin.OUT)

while True:
    for i in range(500):
        in1.value(1)
        in2.value(0)
        in3.value(0)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(0)
        in2.value(1)
        in3.value(0)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(0)
        in2.value(0)
        in3.value(1)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(0)
        in2.value(0)
        in3.value(0)
        in4.value(1)
        time.sleep_ms(5)
    time.sleep(1)
    
    for i in range(500):
        in1.value(0)
        in2.value(0)
        in3.value(0)
        in4.value(1)
        time.sleep_ms(5)
        
        in1.value(0)
        in2.value(0)
        in3.value(1)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(0)
        in2.value(1)
        in3.value(0)
        in4.value(0)
        time.sleep_ms(5)
    
        in1.value(1)
        in2.value(0)
        in3.value(0)
        in4.value(0)
        time.sleep_ms(5)
    time.sleep(1)


#stepup motor clockwise and anticlockwise movement using one list
from machine import Pin
import time

in1 = Pin(5, Pin.OUT)
in2 = Pin(14, Pin.OUT)
in3 = Pin(18, Pin.OUT)
in4 = Pin(19, Pin.OUT)

direction = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for i in range(500):
        for x in direction:
            in1.value(x[0])
            in2.value(x[1])
            in3.value(x[2])
            in4.value(x[3])
            time.sleep_ms(5)
    
    for k in range(500):
        for l in direction:
            in1.value(l[3])
            in2.value(l[2])
            in3.value(l[1])
            in4.value(l[0])
            time.sleep_ms(5)


#steup motor clockwise and anticlockwise movement using two lists
from machine import Pin
import time

in1 = Pin(5, Pin.OUT)
in2 = Pin(14, Pin.OUT)
in3 = Pin(18, Pin.OUT)
in4 = Pin(19, Pin.OUT)

clockwise = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
anticlockwise = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
                  
while True:
    for i in range(500):
        for x in clockwise:
            in1.value(x[0])
            in2.value(x[1])
            in3.value(x[2])
            in4.value(x[3])
            time.sleep_ms(5)
    
    for k in range(500):
        for l in anticlockwise:
            in1.value(l[0])
            in2.value(l[1])
            in3.value(l[2])
            in4.value(l[3])
            time.sleep_ms(5)
