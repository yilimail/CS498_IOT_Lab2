# CS498_IOT_Lab2
This repo contains files related to CS 498 Lab2 - Edge Networking

Contributors:

Alexey Burlakov (NetID: alexeyb2) 
Christopher Lewis (NetID: calewis4) 
Li Yi (NetID: liyi2) 
Pui Sze Pansy Ng (NetID: ppn2) 
Zhijie Wang (NetID: zhijiew2)

Description: In this lab, we implemented a system that collects air quality data and number of MAC addresses. Using Zigbee, the data transimit to RPi wirelessly. At last, the data collected are put into two tables in database. A website is created to show data from database.

RPi_Web_Server
In order to get web server running on RPi, please execute app.py and xbeeRead.py. Database file is sensordata.db. running app.py to host website http://192.168.1.34:8181. It queries the data in airqua table, and shows records on the website. xbeeRead.py receives the data send from Xbee Edge (ESP-8266) and Xbee Router device (Air Quality Sensor/UNO). 

Air_Quality_UNO 
The sketch code read MQ-135 air quality data output decimal PPM data and trasimits to Zig coordinator

ESP8266
The code collect MAC addresses, returns the number of cliets have unique MAC addresses. 

To get the code work:

Upoad Air_quality.ino to Arduino UNO board connected with MQ-135 sensor.
Upload sniffing6.ino to ESP8266 connected with Xbee.
On RPi. executing app.py and xbeeRead.py
In a local network, go to http://192.168.1.34:8181
Enjoy