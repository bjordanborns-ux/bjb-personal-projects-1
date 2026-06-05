import time
import os
# log file auto creates if nonexistent at path: cd/Paranormal/paralog.txt
log_path = 'paranormal/paralog.txt' 

print("Portage Metaphysical Research™")
time.sleep(1)

def temp_emf_status(temperature, emf_level):
    # EMF ranges 1-5, Temp. in celsius. Anthing above 3 for EMF and below 6 for temp will yield high activity status
    if emf_level >= 3 and temperature <= 6:
        act_status = "High"
        print("Activity Status: ", act_status)
    # if emf is less than 3 but above 1 and temp is over 6 but below 8, activity status will = medium. Any other numbers yield Normal status. 
    elif emf_level <= 3 and emf_level >= 1 and temperature >= 6 and temperature <= 8:
        act_status = "Medium" 
        print("Activity Status: ", act_status)
    else:
        act_status = "Normal"
        print("Activity Status: ", act_status)
    # provides activity status to be used in initial instance of normal running function (used as a loop)
    return act_status


def normal_running(act_status):
    location = input("Enter Test Room Location: ")
    
    temperature = int(input("Enter Test Room Temperature: ")) 
    
    emf_level = int(input("Enter Test EMF Level 1-5: ")) 
    
    temp_emf_status(temperature, emf_level)
    
    with open(log_path, 'a') as log_room: 
        log_room.write("Room: ")
        log_room.write(location)
        log_room.write("\n")
        log_room.write("Temp: ")
        log_room.write(str(temperature))
        log_room.write("\n")
        log_room.write("EMF: ")
        log_room.write(str(emf_level))
        log_room.write("\n")
        log_room.write("Activity Levels: ")
        log_room.write(act_status)
        log_room.write("\n")
        log_room.write("----------------")
        log_room.write("\n")  

    print("Recording Data.")
    time.sleep(1)
    print("Recording Data..")
    time.sleep(1)
    print("Recording Data...")
    time.sleep(1)
    print("Data Recorded. ")
    time.sleep(1)   
    
    # returns activity status to be recycled in normal running. 
    return act_status

# ----------------------------------------------------------------------------------------------
# Start of program: 
# Starts program by getting room name from user input: 
location = input("Enter Location for Baseline Test: ")
# Gets input for temperature, and EMF levels, prints both. 
temperature = int(input("Enter Baseline Room Temperature: "))
emf_level = int(input("Enter Baseline EMF Level 1-5: "))

# Opens paralog.txt file to have log written for location, temp, emf, and activity levels.
with open(log_path, 'w') as log_room: 
        log_room.write("Baseline Rec. Room: ")
        log_room.write(location)
        log_room.write("\n")
        log_room.write("Baseline Temp: ")
        log_room.write(str(temperature))
        log_room.write("\n")
        log_room.write("Baseline EMF: ")
        log_room.write(str(emf_level))
        log_room.write("\n")
        log_room.write("Activity Levels: ")
        log_room.write("Baseline recording")
        log_room.write("\n")  
        log_room.write("----------------")
        log_room.write("\n")  
# activity status initially set after first room completion.
act_status = temp_emf_status(temperature, emf_level)

while act_status == "Normal":
    for i in range(0, 2, 1):
        normal_running(act_status)
        time.sleep(1)
    exit()
# Saves log and finishes program if medium or high level evidence is logged. 
if act_status == "Medium":
    print("Possible Evidence Found.")
    time.sleep(1)
    print("Evidence Log: ", act_status, location, emf_level, temperature)
    SystemExit
elif act_status == "High":
    print("High Levels Recorded.")
    time.sleep(1)
    print("Evidence Log: ", act_status, location, emf_level, temperature)
    SystemExit


