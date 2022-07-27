# Google Image Downloader : create a python function that takes a url of an image from google and save location , then download the image in the save location

import requests 
import shutil 

url = input('Please enter an image URL :') 
file_name = input('Save image as :') 

res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')



    # an0ther code :
    
# import requests
# import shutil
# img_url=input("enter imge url to download: ")
# image_name=input("enter imge name: ")+".jpg"
# img=requests.get(img_url,stream=True)
# if img.status_code==200:
#     with open(image_name,'wb') as f:
#         shutil.copyfileobj(img.raw,f)
#     print("success download ^_^")
# else:
#     print("oh no Error -_-")