import sys
import urllib.request
from csv import reader
import os.path
csv_filename = sys.argv[1]
with open(csv_filename.format(csv_filename), 'r') as csv_file:
    csv_file = reader(csv_file)
    next(csv_file)
    for line in csv_file:
        print(line[7])
        if os.path.isfile("/Users/akhilnamburi/Desktop/imagesDataSet/" + line[0] + ".jpg"):
            print("Image skipped for {0}".format(line[0]))
        else:
            if line[7] != '' and line[0] != "SIGNIDNO":
                urllib.request.urlretrieve(line[7], "/Users/akhilnamburi/Desktop/imagesDataSet/" + line[0] + ".jpg")
                print("Image saved for {0}".format(line[0]))
            else:
                print("No result for {0}".format(line[0]))
