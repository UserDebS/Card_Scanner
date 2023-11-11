import serial
import serial.tools.list_ports as port_list
import os
import pymongo
import urllib.parse as uprase

#%% initializations
uid = ''
image_names = ['Picture', 'aadhaar', 'pan', 'voter']
current_folder = os.getcwd()
target_folder = os.path.join(current_folder, 'Images')

mongouri = 'mongodb+srv://roumya2020second:'+ uprase.quote('ImDS@6294MySQL') +'@medicure.csyloil.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(mongouri)
execute = client.verification.user_details


#%% Functions

def flush_dir(dirpath):
    for file in os.listdir(dirpath):
        os.remove(os.path.join(dirpath, file))

def InsertImages(uid):
    flush_dir(target_folder)
    filter = {
        'UID' : str(uid).split('\r')[0]
    }
    result = execute.find_one(filter)
    username = result['Name']
    for category in image_names:
        with open(f'{target_folder}/{username}_{category}.png', 'wb') as file:
            file.write(result[f'{category}'])
    

#%% main

if __name__ == '__main__':
    try:
        if(not os.path.exists(os.path.join(current_folder, target_folder))):
            os.mkdir(target_folder)

        port = ''

        for p in port_list.comports():
            if(p.description == 'Arduino Uno (COM3)'):
                port = p.device

        if(port != ''): print(f'Reading port : {port}')


        serial_port = serial.Serial(port,9600)
        while(True):
            try:
                while serial_port.in_waiting == 0:
                    pass

                uid = serial_port.readline().decode('utf-8').split('\n')[0] or ''

                InsertImages(uid)
            except:
                print('Device has been detached')
                break

    except:
        print('Device not connected')


