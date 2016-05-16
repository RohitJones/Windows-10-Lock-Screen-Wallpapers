import os
import hashlib
import shutil

HashList = []
Username = os.environ['USERNAME']
SourcePath = "C:\\Users\\" + Username + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"
DestinationPath = "C:\\Users\\" + Username + "\\Pictures\\Lockscreen Wallpapers\\"

def CacheHashes():
    try:
        hashFile = open(DestinationPath + "Hashes.txt", "r")
    except IOError:
        try:
            hashFile = open(DestinationPath + "Hashes.txt", "w+")
        except IOError:
            os.mkdir(DestinationPath)
            hashFile = open(DestinationPath + "Hashes.txt", "w+")

    for eachLine in hashFile:
        HashList.append(eachLine.rstrip("\n"))
    hashFile.close()


def UpdateHashes():
    CacheHashes()
    hashFile = open(DestinationPath + "Hashes.txt", "a")

    for each in os.listdir(DestinationPath):
        if each == "Hashes.txt":
            continue

        FullPath = DestinationPath + each
        hash = hashlib.md5(open(FullPath, 'rb').read()).hexdigest()
        if hash not in HashList:
            hashFile.write(str(hash) + "\n")

    hashFile.close()


def RebuildHashes():
    hashFile = open(DestinationPath + "Hashes.txt", "w")
    for each in os.listdir(DestinationPath):
        if each == "Hashes.txt":
            continue
        FullPath = DestinationPath + each
        hash = hashlib.md5(open(FullPath, 'rb').read()).hexdigest()
        hashFile.write(str(hash) + "\n")
    hashFile.close()


def CopyPictures():

    CacheHashes()
    number_of_existing_files = len(HashList)

    PictureList = []
    HashCacheFile = open(DestinationPath + "Hashes.txt", "a")
    for each in os.listdir(SourcePath):
        FullPath = SourcePath + each
        if os.lstat(FullPath).st_size // 1024 > 400:
            md5hash = hashlib.md5(open(FullPath, 'rb').read()).hexdigest()
            if md5hash not in HashList:
                HashCacheFile.write(md5hash + "\n")
                PictureList.append(each)
    HashCacheFile.close()

    for each in PictureList:
        shutil.copy2(SourcePath + each, DestinationPath + str(number_of_existing_files + 1) + ".jpg")
        number_of_existing_files += 1


def main():
    while True:
        print("1) Update Hashes")
        print("2) Rebuild Hashes")
        print("3) Get All Pictures")
        print("4) exit\n")

        option = int(input("Enter your choice: "))

        if option == 1:
            UpdateHashes()
        elif option == 2:
            RebuildHashes()
        elif option == 3:
            CopyPictures()
        elif option == 4:
            break

if __name__ == "__main__": main()
