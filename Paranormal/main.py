import time
import os
# log file auto creates if nonexistent at path: cd/Paranormal/paralog.txt
log_path = 'paranormal/paralog.txt' 

print("Portage Metaphysical Research™")
time.sleep(1)

rooms_recorded = []

def temp_emf_status(temperature, emf_level, high_act_count, med_act_count, normal_count):
    # EMF ranges 1-5, Temp. in celsius. Anthing above 3 for EMF and below 6 for temp will yield high activity status
    if emf_level >= 3 and temperature <= 6:
        act_status = "High"
        high_act_count = (int(high_act_count) + 1)
        print("Activity Status: ", act_status)       
    # if emf is less than 3 but above 1 and temp is over 6 but below 8, activity status will = medium. Any other numbers yield Normal status. 
    elif emf_level <= 3 and emf_level >= 1 and temperature >= 6 and temperature <= 8:
        act_status = "Medium" 
        med_act_count = (int(med_act_count) + 1)
        print("Activity Status: ", act_status)
    else:
        act_status = "Normal"
        normal_count = ((normal_count) + 1)       
        print("Activity Status: ", act_status)
        
    # provides activity status to be used in initial instance of normal running function (used as a loop)
    return act_status, high_act_count, med_act_count, normal_count


def normal_running(act_status):
    location = input("Enter Test Room Location: ")
    rooms_recorded.append(location)

    temperature = int(input("Enter Test Room Temperature: ")) 
    
    emf_level = int(input("Enter Test EMF Level 1-5: ")) 
    
    temp_emf_status(temperature, emf_level, high_act_count, med_act_count, normal_count)
    
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
high_act_count = (0)
med_act_count = (0)
normal_count = (0)

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
act_status, high_act_count, med_act_count, normal_count = temp_emf_status(temperature, emf_level, high_act_count, med_act_count, normal_count)

while act_status == "Normal":
    for i in range(0, 4, 1):
        normal_running(act_status)
        time.sleep(1)
        print(rooms_recorded)

# Saves log and finishes program if medium or high level evidence is logged. 
if act_status == "Medium":
    print("Possible Evidence Found.")
    for i in range(0,4,1):
        normal_running(act_status)
        time.sleep(1)
        print(rooms_recorded)
    time.sleep(1)
    print("Evidence Log: ", act_status, location, emf_level, temperature)
    print(rooms_recorded)

elif act_status == "High":
    print("High Levels Recorded.")
    for i in range(0,4,1):
        normal_running(act_status)
        time.sleep(1)
        print(rooms_recorded)
    time.sleep(1)
    print("Evidence Log: ", act_status, location, emf_level, temperature)
    print(rooms_recorded)
    print(high_act_count)
    print(med_act_count)
    print(normal_count)



