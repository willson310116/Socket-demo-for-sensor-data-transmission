# Socket demo for sensor data transmission

### Abstract
This is a simple demo of transmitting real-time sensor data from a disinfection robot to remote deivce for displaying on monitor.
- Sensor data contains: 
ClO2 ppm, Temp(C), Temp(F), RH(%), water level, pm1.0, pm2.5,pm4.5, pm10.0, nc0.5, nc1.0, nc2.5, nc4.5, nc10.0, typical partical size
Total 15 kinds of data need to be transmitted instantly.
- Socket with TCP protocol:

![](https://i.imgur.com/KIMQ1Td.png =350x400)

- Excepted display GUI

![](https://i.imgur.com/bS4w4bV.png)


### Usage
1. `server.py`
    - set port 
    - send 15 data separated with comma manually(client should connected first)
    - ex: `0.1,0.2,1.1,2,3,9,4,3.4,6,9.0,80,1.5,3.7,8.7,9.3`
2. `server_random.py`
    - set port
    - randomly send 15 data (client should connected first)
3. `client.py`
    - set proper port and ip address
    - recieve data and convert into DataFrame
    - allows users to set # to refresh data (only show the stats of # latest data)
    - show data and its stats
    - write data into a csv file after each update
 
    