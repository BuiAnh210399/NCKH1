# import RPi.GPIO as GPIO
# import serial
# import time
import pandas as pd
import pandas as np
import folium
from   pandas import DataFrame, Series
from math import cos, asin, sqrt
import numpy as np  

#khoi tao truyen thong
# ser = serial.Serial('/dev/ttyS0',115200)
# ser.flushInput()

#khoi tao ban dau
# power_key = 6
# rec_buff = '' #luu gia tri doc ve
# time_count = 0 #thoi gian tra ve ket qua
# gps_latitude = ''
# gps_longitude = ''
# data = ''

# def transfer_data(data):
#     gps_D = int(float(data)/100)
#     gps_M = int(float(data)%100/1)
#     gps_S = (float(data)%1)*60
#     gps = gps_D + round(gps_M/60,6) + round(gps_S/3600,6)
#     return round(gps,7)

# def handle_data(data):
#     answer1 = ''
#     answer1 = str(data.decode())
#     answer1 = answer1.replace(' ',',')
#     answer1 = answer1.replace('\n',',')
#     answer1 = answer1.replace('\r','')
#     answer1 = answer1.split(',')
#     gps_latitude = transfer_data(answer1[2])
#     gps_longitude = transfer_data(answer1[4])

#     print('Latitude: ', gps_latitude)
#     print('Longitude: ',gps_longitude)

fboiz=[[21.04620428,    105.7816722],
[21.04620428,   105.790308],
[21.0462455,    105.7976628],
[21.04622489,   105.8053931],
[0,   0],
[21.04620428,   105.7843447],
[21.04605999,   105.7830416],
[21.04531791,   105.7830195],
[21.04527669,   105.7843005],
[21.0460806 ,   105.7863104],
[21.04350394,   105.7863546],
[21.04166933,   105.7860895],
[21.04599815,   105.791589],
[21.04346271,   105.7901534],
[21.04168995,   105.7903522],
[21.04342149,   105.7917216],
[21.04160749,   105.7917436],
[21.04352456,   105.7935326],
[21.04610121,   105.7945265],
[21.04416357,   105.7946591],
[21.04164872,   105.7935989],
[21.04164872,   105.7944603],
[21.04605999,   105.7966468],
[21.04422541,   105.7966689],
[21.04418418,   105.7975965],
[21.04290615,   105.7975745],
[21.04286492,   105.7966468]
]
name=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

#vị trí nhà(điểm đầu=điểm 0)
lat=21.05752421432143 
long=105.78129990547909

# lat=gps_latitude                              
# long=gps_longitude
print("")
print("Toạ đỘ vị trí nhà(điểm 0) là:","    Vĩ độ:",lat,"     kinh độ:",long)

zoom = 15
gmap2 = folium.Map(location=(lat, long), zoom_start=zoom)
marker = folium.Marker(location=(lat,long), popup = 'Vi tri hien tai')
marker.add_to(gmap2)
n=27
i=0
# #ham danh dau cac diem tren ban ho
#     while (i<n):
#         marker = folium.Marker(location=(fboiz[i][0],fboiz[i][1]), popup = name[i])
#         marker.add_to(gmap2)
#         i=i+1
    
#nhap ma trang trong so
graph={'1':{'7':149},
'2':{'10':396,'13':153,'14':293},
'3':{'4':808,'23':102,'25':229},
'4':{'3':808},
'6':{'7':137,'9':98,'10':2004},
'7':{'1':149,'6':137,'8':97},
'8':{'7':97,'9':135},
'9':{'6':98,'8':135,'11':274},
'10':{'2':396,'6':204,'11':272},
'11':{'9':274,'10':272,'12':208,'14':410},
'12':{'11':208,'15':440},
'13':{'2':152,'16':290,'19':304},
'14':{'2':293,'11':410,'15':192,'16':158},
'15':{'12':440,'14':192,'17':149},
'16':{'13':290,'14':158,'17':194,'18':189},
'17':{'15':149,'16':194,'21':192},
'18':{'16':189,'20':158,'21':195},
'19':{'13':304,'20':206,'23':216},
'20':{'18':138,'19':206,'24':200},
'21':{'17':192,'18':195,'22':85},
'22':{'21':85,'27':269},
'23':{'3':102,"19":216,'24':200},
'24':{'20':200,'23':200,'25':104,'27':142},
'25':{'3':229,'24':104,'26':151},
'26':{'25':151,'27':93},
'27':{'22':269,'24':142,'26':93}}
# lat=gps_latitude
# long=gps_longitude
#Chuong trinh con tim duong di ngan nhat
def dijkstra(graph,start,goal):
#cac diem da xet
    shortest_distance = {} 
    predecessor = {}
#mang chua cac diem tren ban do
    unseenNodes = graph 
    infinity = 9999999
    path = []
    'khoi tao mang shortest_distance'
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    while unseenNodes:
#diem duoc xet tiep theo
        minNode = None 
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
#kiem tra xem da phai duong di ngan nhat hay chua, neu chua thi xet lai
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
        
    currentNode = goal
#ham kiem tra dich den
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
#path chinh la cac diem thoa man
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print("")
        print('Quãng đường phải đi: ' + str(shortest_distance[goal]),"m")
        print("")
        print('Đoạn đường đi ngắn nhất là: ' + str(path))
        print("") 
    return path
#In ra duong di ngan nhat
def distance(lat1, lon1, lat2, lon2):
    R = 6371 # Ban kinh trai dat (km)
    p = np.pi/180 # gia tri pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 2*R*asin(sqrt(a))

min=10     #giả sử min bằng 10km điểm gần nhất so với vị trí nhà
# print(min)


#Tim diem gan vi tri hien tai nhat
v=0
for i in range(0,26):
    if min > distance( fboiz[i][0],fboiz[i][1], lat, long):
            min = distance(fboiz[i][0],fboiz[i][1], lat, long )
            # print(min)
            v=i
print("")
print("Điểm gần nhất cách nhà với khoảng cách là:",min,"km")
print("")
print("Điểm gần vị trí nhà nhất là điểm",v+1)

#nhập giá trị để tính khoảng cách từ nhà đến các điểm mong muốn
k=str(v+1)
c=dijkstra(graph,k, '22')
j=1
d=[j for j in range(0,30)]
k=len(c)
i=0
m=0
#Chuyen kieu du lieu tu string sang int, roi gan vao list d[i]
for i in range(0,k):
    m=int(c[i])
    d[i]=m    
#lap list gom co k hang va 2 cot
fbgirl = []   
for i in range(0, k+1):
    fbgirl.append([])
    for j in range(0, 2):
        x =fboiz[i][j]
        fbgirl[i].append(x)
#tao list chua toa do cua cac diem di qua
j=0
fbgirl[0][0]=lat
fbgirl[0][1]=long
for i in range(1,k+1):
    m=d[j]
    fbgirl[i][0]=fboiz[m-1][0]
    fbgirl[i][1]=fboiz[m-1][1]
    j=j+1
#noi cac diem voi nhau
for i in range(0,k+1):
    folium.PolyLine(fbgirl, color='red', weight=4.5, opacity=.5).add_to(gmap2)
gmap2.save("foliumMarkerMultiple.html")

# #Truyen lenh AT den mudule SIM7600
# def send_at(command,back,timeout):
#     rec_buff = ''
#     ser.write((command+'\r\n').encode())
#     time.sleep(timeout)
#     if ser.inWaiting():
#         time.sleep(0.01 )
#         rec_buff = ser.read(ser.inWaiting())
#     if rec_buff != '':
#         if back not in rec_buff.decode():
#             print(command + ' ERROR')
#             print(command + ' back:\t' + rec_buff.decode())
#             return 0
#         else:
#             print(rec_buff.decode())
#             if '+CGPSINFO: ' in rec_buff.decode():
#                 handle_data(rec_buff)
#                 time.sleep(30)
#             return 1
#     else:
#         print('GPS is not ready')
#         return 0

# def get_gps_position():
#     answer = 0
#     print('Start GPS session...')
#     rec_buff = ''
#     send_at('AT+CGPS=1,1','OK',1)
#     time.sleep(2)    
#     answer = send_at('AT+CGPSINFO','+CGPSINFO: ',1)
#     if 1 == answer:
#         answer = 0
#         if ',,,,,,' in rec_buff:
#             print('GPS is not ready')
#             time.sleep(1)
#     else:
#         print('error %d'%answer)
#         rec_buff = ''
#         send_at('AT+CGPS=0','OK',1)
#         time.sleep(1.5)

# def power_on(power_key):
#     print('SIM7600X is starting:')
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setwarnings(False)
#     GPIO.setup(power_key,GPIO.OUT)
#     time.sleep(0.1)
#     GPIO.output(power_key,GPIO.HIGH)
#     time.sleep(2)
#     GPIO.output(power_key,GPIO.LOW)
#     time.sleep(20)
#     ser.flushInput()
#     print('SIM7600X is ready')

# def power_down(power_key):
#     print('SIM7600X is loging off:')
#     GPIO.output(power_key,GPIO.HIGH)
#     time.sleep(3)
#     GPIO.output(power_key,GPIO.LOW)
#     time.sleep(18)
#     print('Good bye')

# power_on(power_key)
# get_gps_position()
# power_down(power_key)
