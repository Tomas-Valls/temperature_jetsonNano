import os
import subprocess
def main():
    temp_cmd = ["cat" ,"/sys/devices/virtual/thermal/thermal_zone0/temp"]
    temp = subprocess.run(temp_cmd,stdout=subprocess.PIPE)
    temp = temp.stdout.decode().rstrip()
    temp=int(temp)/1000
    print ( temp )

if __name__ == "__main__":
    main()
