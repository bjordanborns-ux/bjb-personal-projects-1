import time

print("NorthLight Launch Verification")


wind = int (input ("Wind Speed"))
pressure = int (input ("Pressure level in mmHg"))

status = []

recovery_armed = status.append (input ("Recovery System Armed? Y or N: "))
cameras_record = status.append (input ("Cameras Recording Y or N: "))
range_clear = status.append (input ("Range is clear? Y or N: "))

if wind > 12 or pressure >  1020:
    weather_go = False
else:
    weather_go = True 

count_go = 0

if weather_go == True:
    count_go = count_go + 1 
else:
    count_go = count_go + 0 

for i in range(0, 3):
    status[i]
    if status[i] == "Y":
        count_go = count_go + 1
        final_count = count_go
        time.sleep(1)
    else:
        final_count = 0
        print ("Launch Scrubbed. System Disagreement")

print ("Number of system go's")
print (final_count)

if final_count > 3:
    print ("Launch Approved")
else:
    print ("Launch Scrubbed: Weather No-Go")   



