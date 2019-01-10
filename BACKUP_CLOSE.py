import sys
import subprocess
subprocess.call(["taskkill","/K","/IM","googledrivesync.exe"])
import os
import time
# creating a forever loop
while 1 :
    os.system("TASKKILL /F /IM googledrivesync.exe")
    time.sleep(10)
    os.system("TASKKILL /F /IM googledrivesync.exe")
exit()
sys.exit()
