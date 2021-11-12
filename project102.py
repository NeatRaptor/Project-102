from typing import NewType
import cv2
import dropbox
import time
import random
import os

startTime = time.time()

def CreateFolder():
    os.mkdir("class102/new")

def uploadFile(imageName):
    accessToken = "RvSOZNTyr48AAAAAAAAAAadI9-1tBLGEBec8kZXgH62A3lP_fL_X7cwGCJ0enzWY"
    file = imageName
    fileFrom = file
    fileTo = "NewFolder/" + (imageName)
    dbx = dropbox.Dropbox(accessToken)

    with open(fileFrom, 'rp') as f:
        dbx.files_upload(f.read(), fileTo, mode=dropbox.files.writeMode.overwrite)
        print("File Uploaded")

def main():
    while (True):
        if ((time.time() - startTime) >= 300):
            name = CreateFolder()
            uploadFile(name)

main()