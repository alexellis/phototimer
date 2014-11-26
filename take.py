import os
import sys
import time
from datetime import datetime
from camera import exposureCalc

def run_loop(base, pause):
    am = 700
    pm = 1700
    exposureCalc1= exposureCalc(am, pm)
    height = 1536
    width = 2048
    current_milli_time = lambda: int(round(time.time() * 1000))
    
    print("Pause : " + str(pause) )

    def try_to_mkdir(path):
        if os.path.exists(path) == False:
            os.makedirs(path)

    while True:
        hoursMinutes=int(time.strftime("%H%M"))
        exposureMode=exposureCalc1.get_exposure(hoursMinutes)
        take_shot = exposureCalc1.take_shot(hoursMinutes)

        if (take_shot == True):

            path = str( datetime.now().year) 
            try_to_mkdir(base + "/" +path)

            path = str( datetime.now().year)  + "/"  + str( datetime.now().month)
            try_to_mkdir(base + "/" +path)

            path = str( datetime.now().year)  + "/"  + str( datetime.now().month)+"/"+ str( datetime.now().day)
            try_to_mkdir(base + "/" +path)

            path =  str( datetime.now().year)  + "/"  + str( datetime.now().month)+"/"+ str( datetime.now().day)+"/"+ str( datetime.now().hour)
            try_to_mkdir(base + "/" +path)

            mili = str(current_milli_time())
            name=path.replace("/","_") +"_"+mili+".jpg"
            print("Capturing " + name+" in " + exposureMode + " mode")
            os.system("/opt/vc/bin/raspistill -q 40 "+\
                "-h "+str(height)+\
                " -w "+str(width)+\
                " --exposure " +exposureMode +\
                " --metering matrix"+\
                " -o "+base+"/"+path+"/"+name)
        else:
            print("Shot cancelled during hours of darkness")

        time.sleep(pause)

if(__name__ == '__main__'):
    if len(sys.argv) < 1:
        exit()
    else:
	try:
        	pauseInterval = int(sys.argv[1])
        	basePath="/mnt/usbflash"
        	run_loop(basePath,pauseInterval)
	except KeyboardInterrupt:
		print ("Cancelling take.py")

