from gpiozero import CPUTemperature
from time import sleep, strftime, time

cpu = CPUTemperature()
t = 0
def write_temperature(t,temp):
    with open("./cpu_temperature.txt","a") as log:
        log.write("({0},{1}) ".format(t,temp))
                    
while True:
    temp = cpu.temperature
    t += 1
    write_temperature(t,temp)
    print(temp,t)
    sleep(1)
        
