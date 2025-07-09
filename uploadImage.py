import os
import pymongo
import urllib.parse as uprase

#%% initializations
uid = '406d2d1b'

mongouri = 'mongodb+srv://roumya2020second:'+ uprase.quote('ImDS@6294MySQL') +'@medicure.csyloil.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(mongouri)
execute = client.verification.user_details

current_dir = os.getcwd()
input_dir = os.path.join(current_dir, 'Inputs')

for file in os.listdir(input_dir):
    if(file.startswith('Keychain')):
        with open(os.path.join(input_dir, file), 'rb') as bytedata:
            if(file.split('.')[0] == 'Keychain'):
                execute.update_one({'UID' : uid}, {'$set' : {'Picture' : bytedata.read()}})
            else:
                execute.update_one({'UID' : uid}, {'$set' : {f'{file.split(".")[0].split("_")[1]}' : bytedata.read()}})

print('Uploaded Succesfully')