import serial, time, datetime, sys
import sqlite3
import os.path
#from xbee import XBee, ZigBee

SERIALPORT = '/dev/ttyUSB0'    # the com/serial port the XBee is connected to, the pi GPIO should always be ttyAMA0
BAUDRATE = 9600      # the baud rate we talk to the xbee
#TIMEOUT=1

ser = serial.Serial(SERIALPORT, BAUDRATE)
#conn=sqlite3.connect('sensordata.db')
#c=conn.cursor()
airq = 0
macnum = 0
#xbee = ZigBee(ser)

#print ('Receiving xbee data')
# Continuously read and print packets
while True:
#    try:
        conn=sqlite3.connect('sensordata.db')
        c=conn.cursor()
        incoming = ''
        #ser.write('hello user \r\n') #response = ser.readline().strip() #wait_read_frame()
        incoming = ser.readline().strip()
        print(incoming)
        if(incoming.find('PPM') >= 0):
            c.execute("INSERT INTO airqua(currenttime, airq, macs) values(time('now'),(?), (select macnum from mac order by currenttime DESC limit 1))", (incoming,))
        else:
            c.execute("INSERT INTO mac(currenttime, macnum) values(time('now'),(?))", (incoming,))
        conn.commit()
        conn.close()
            #cursor.execute("INSERT INTO mac(currenttime, mac) values(time('now'),(?))", incoming)
        #c.execute("INSERT INTO airqua(currenttime, airq) values(time('now'),(?))", incoming)
        #print(incoming) #(response)
    #except KeyboardInterrupt:
     #   break

#ser.close()