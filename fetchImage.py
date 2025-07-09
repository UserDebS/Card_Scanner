import os
import pymongo
import urllib.parse as uprase

#%% initializations
uid = '406d2d1b'

mongouri = 'mongodb+srv://roumya2020second:'+ uprase.quote('ImDS@6294MySQL') +'@medicure.csyloil.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(mongouri)
execute = client.verification.user_details

image_names = ['Picture', 'aadhaar', 'pan', 'voter']
current_folder = os.getcwd()
target_folder = os.path.join(current_folder, 'Images')


result = execute.find_one({'UID': uid})
username = result['Name']
for category in image_names:
    with open(f'{target_folder}/{username}_{category}.png', 'wb') as file:
        file.write(result[f'{category}'])