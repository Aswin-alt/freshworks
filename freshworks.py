import json
import os
import os.path
from os import path
import time


def read(n):
    for i in range(n):
        keys = input("Enter Key : ")  # here i have taken keys as strings
        values = input("Enter value : ")  # here i have taken values as String
        if keys in data:
            print("Key already exists!")
        else:
            data[keys] = values
            current_milli_time = int(round(time.time() * 1000))
            data1[keys] = current_milli_time
    return data


# JSON file location
print("The Time to live for a key is 1000 seconds")
location = input("Enter file location ('NO' for skipping path) : ")
filename = input("Enter the file name : ")
dir_path = os.path.dirname(os.path.realpath(__file__))

n = 1

while n == 1:

    print("Enter which operation to be performed : ")
    print("1.Create\n2.Read\n3.Delete\n4.Display file")
    choice = int(input("Enter your choice(1-4) : "))

    if location == "NO":

        if path.exists(dir_path + "/" + filename):

            f = open(filename, "r+")
            data = json.loads(f.read())

            f1 = open("time.json", "r+")
            data1 = json.loads(f1.read())

            # Input dic
            if choice == 2:
                n = int(input("Enter no.of key value : "))
                data = read(n)

            # Delete key
            elif choice == 3:
                delele = input("Enter the key to be deleted : ")
                del data[delele]
                del data1[delele]

            elif choice == 4:
                cur_time = int(round(time.time() * 1000))
                for i in data1:
                    if data1[i] > cur_time:
                        del data1[i]
                # Iterating through the json
                print(data)

            else:
                print("Enter a correct choice!")

            f = open(filename, "w+")
            json.dump(data, f)

            f1 = open("time.json", "w+")
            json.dump(data1, f1)

        else:
            f = open(filename, "w+")

            f1 = open("time.json", "w+")

            data = {}
            data1 = {}

            # Create dic
            if choice == 1:
                n = int(input("Enter no.of key value : "))
                data = read(n)

            # Delete key
            elif choice == 3:
                delele = input("Enter the key to be deleted : ")
                del data[delele]
                del data1[delele]

            elif choice == 4:
                cur_time = int(round(time.time() * 1000))
                for i in data1:
                    if data1[i] > cur_time:
                        del data1[i]

                # Iterating through the json
                print(data)

            else:
                print("Enter a correct choice!")

            json.dump(data, f)
            json.dump(data1, f1)

    else:
        if path.exists(location + "/" + filename):

            f = open(location + "/" + filename, "r+")
            data = json.loads(f.read())

            f1 = open(location + "/" + "time.json", "r+")
            data1 = json.loads(f1.read())

            # Input dic
            if choice == 2:
                n = int(input("Enter no.of key value : "))
                data = read(n)

            # Delete key
            elif choice == 3:
                delele = input("Enter the key to be deleted : ")
                del data[delele]
                del data1[delele]

            elif choice == 4:
                cur_time = int(round(time.time() * 1000))

                for i in data1:
                    if data1[i] > cur_time:
                        del data1[i]
                # Iterating through the json
                print(data)

            else:
                print("Enter a correct choice!")

            f = open(filename, "w+")
            json.dump(data, f)

            f1 = open("time.json", "w+")
            json.dump(data1, f1)

        else:
            f = open(location + "/" + filename, "w+")

            f1 = open(location + "/" + "time.json", "w+")

            data = {}
            data1 = {}
            # Create dic
            if choice == 1:
                n = int(input("Enter no.of key value : "))
                data = read(n)

            # Delete key
            elif choice == 3:
                delele = input("Enter the key to be deleted : ")
                del data[delele]
                del data1[delele]

            elif choice == 4:
                cur_time = int(round(time.time() * 1000))
                for i in data1:
                    if data1[i] > cur_time:
                        del data1[i]
                # Iterating through the json
                print(data)

            else:
                print("Enter a correct choice!")

            json.dump(data, f)
            json.dump(data1, f1)

    str1 = input("Do you want to continue(Y/N) : ")
    if str1 == 'N' or str1 == 'n':
        n = 0

        # Closing file
        f.close()
        f1.close()
