import os
import subprocess
def main():
    #temp = os.popen(“cat /sys/devices/virtual/thermal/thermal_zone0/temp”).read()
    temp_cmd = ["cat" ,"/sys/devices/virtual/thermal/thermal_zone0/temp"]
    temp = subprocess.run(temp_cmd,stdout=subprocess.PIPE)
    temp = temp.stdout.decode().rstrip()
    print ( temp )

if __name__ == "__main__":
    main()
