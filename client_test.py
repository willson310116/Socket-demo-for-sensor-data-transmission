import socket
import traceback
import time
import csv
import pandas as pd

# saving data in csv file, and don't need to append list, 
# only need to split the spring received, 
# EXPECT DATA RECEIVED FROM SOCKET IS IN THE FORM OF 1,2,3,4,...

class SocketClient():
    def __init__(self, remote="127.0.0.1", port=8080):
        self.remote = remote
        self.port = port
        self.sock = None

    def initialize(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #socket()
    def connect(self):
        try:
            self.sock.connect((self.remote, self.port))
            # self.sock.settimeout(2)
            print(f"Sucesssfully connect to {self.remote} {self.port}")
        except:
            traceback.print_exc()
    

    def send_text(self,text):
        
        self.sock.send(bytes(text,encoding="utf-8"))

    def recv_text(self):
        msg = self.sock.recv(4096) # blocking _> wait
        #recv non-blocking
        return msg
    def close(self):
        self.sock.close()
    
# def file_initialize(file):
#     with open(file, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["Test1","Test2","Test3"])

    # 寫入資料
    # writer.writerow(["ClO2 ppm","Temp(C)","Temp(F)","RH","water level",
    #   "pm1.0","pm2.5","pm4.5","pm10.0",
    #   "nc0.5","nc1.0","nc2.5","nc4.5","nc10.0","typical partical size"])
    

# def add_data(data,file):
#     with open(file, 'a+', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(data)

# def show_data(file):
#     with open(file, newline='') as csvfile:
#         rows = csv.reader(csvfile)
#         for row in rows:
#             print(row)
#             #print(type(row))

def data_process(data):
    data = str(data)
    print(type(data))
    data = data[2:-1]
    data = data.split(",")
    return data

# file_name = "test.csv"
# file_name = input("Type file name(csv): ")

if __name__ == "__main__":
    socket_client = SocketClient(remote="127.0.0.1", port=9997)
    #socket_client = SocketClient(remote="192.168.1.104", port=9998)
    socket_client.initialize()
    socket_client.connect()

    #file_initialize(file_name)
    #show_data(file_name)
    count = 0

    # create dataframe
    #df = pd.DataFrame({"test1":[],"test2":[],"test3":[]})

    df = pd.DataFrame({"ClO2 ppm":[],"Temp(C)":[],"Temp(F)":[],"RH":[],"water level":[],
        "pm1.0":[],"pm2.5":[],"pm4.5":[],"pm10.0":[],
        "nc0.5":[],"nc1.0":[],"nc2.5":[],"nc4.5":[],"nc10.0":[],"typical partical size":[]})
    

    while True:
        data = socket_client.recv_text()
        print(data)
        
        
        if data == bytes("q",encoding='utf-8'):
            print("terminated")
            socket_client.send_text("Client has closed!")
            break

        else:
            socket_client.send_text("Client has received!")
            data = data_process(data) # return a fine list

            # Need to refresh data, here default refresh if more than 3 data
            if(count>2):
                count = 0
                df.loc[count] = data
                count += 1
            else:
                df.loc[count] = data
                count += 1


            '''
            # Don't need to refresh data, infinitely append data
            # create a new set to append to Dataframe
            new = pd.DataFrame({"test1":data[0],"test2":data[1],"test3":data[2]},index=[1])

            df = df.append(new,ignore_index=True) #append new data to last row
            df.to_csv("data.csv",encoding="utf-8",index=0)
            '''


            '''
            df = pd.read_csv(file_name) # read file as pd
            data = data_process(data) # return a fine list
            add_data(data,file_name) # add to output file
            '''
            print(df.head())
            print("-----------")
            # print(df.describe()) pandas don't recognize the data as int
            df = df.astype(float) # change data in dataframe into float type
            print(df.describe())
            # print(df.astype(float).describe())
            print("----------------------------")
            df.to_csv("data.csv",encoding="utf-8",index=0)

    #df = df.reset_index()
    #df.to_csv("data.csv",encoding="utf-8",index=0)
    
    socket_client.close()

    df = pd.read_csv("data.csv")
    print(df.head())
    print("----------------------------")
    print(df.describe())
    


