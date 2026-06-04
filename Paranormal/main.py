import time

log_path = 'log.txt' 

print("Metaphysical Research™")
time.sleep(1)

def temp_emf_status(temperature, emf_level):
    if emf_level >= 3 and temperature <= 6:
        act_status = "High"
        print("Activity Status: ", act_status)
    
    elif emf_level <= 3 and emf_level >= 1 and temperature >= 6 and temperature <= 8:
        act_status = "Medium" 
        print("Activity Status: ", act_status)
    else:
        act_status = "Normal"
        print("Activity Status: ", act_status)
    return act_status


def normal_running(act_status):
    location = input("Enter Next Room Location: ")
    print("Room = ", location)
    temperature = int(input("Enter Next Room Temperature: ")) 
    print("Temperature = ", temperature)
    emf_level = int(input("Enter Next EMF Level 1-5: ")) 
    print("EMF Level = ", emf_level)
    temp_emf_status(temperature, emf_level)
    
    with open(log_path, 'a') as log_room: 
        log_room.write("Room:\r ")
        log_room.write(location)
        
        log_room.write("Temp:\r")
        log_room.write(temperature)
        
        log_room.write("EMF: \r")
        log_room.write(emf_level)

        log_room.write("Activity Levels:\r ")
        log_room.write(act_status)


    print("Recording Data.")
    time.sleep(1)
    print("Recording Data..")
    time.sleep(1)
    print("Recording Data...")
    time.sleep(1)
    print("Data Recorded. ")
    time.sleep(1)   
    return act_status
# ----------------------------------------------------------------------------------------------
# Start of program: 
# Starts program by getting room name from user input: 
location = input("Enter Room Location: ")
print("Room = ", location)
# Gets input for temperature, and EMF levels, prints both. 
temperature = int(input("Enter Room Temperature: "))
print("Temperature = ", temperature)
emf_level = int(input("Enter EMF Level 1-5: "))
print("EMF Level = ", emf_level)
act_status = temp_emf_status(temperature, emf_level)

while act_status == "Normal":
    normal_running(act_status)

while act_status == "Medium":
    print("Possible Evidence Found. ")
    print("Evidence Log: ", act_status, location, emf_level, temperature)
    SystemExit

while act_status == "High":
    print("High Levels Recorded. ")
    print("Evidence Log: ", act_status, location, emf_level, temperature)
    SystemExit


