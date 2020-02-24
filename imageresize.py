import os
from os import listdir
from os.path import isfile, join
from PIL import Image
mypath = os.getcwd()
onlyfiles=[f for f in listdir(mypath) if isfile(join(mypath,f))]
index = 30976
for images in onlyfiles[30976:]:
    image = Image.open(images)
    image = image.resize((300,300))
    image.save("s"+images)
    print(index)
    index+=1