import random
import time

# - - - Vehicle Preferences
# Vehicle dictionary with name and status (status updated in section below)
vehicle = {
    "name" : "Test Article 1",
    "status" : ""
}

vehicle_name = input("Enter vehicle name: ")
vehicle["name"] = vehicle_name
# - - -

# - - - Maximum Allowed Temp.
# Gets maximum temperatuer accepatable from user:
def ask_maximum():    
    while True:
        try:
            temp_accept = int(input("Enter Maximum Temperature in Farenheit: "))
            return temp_accept
        except ValueError:
            print("INVALID INPUT: Input must be in form of number.")

temp_accept = ask_maximum()
# - - -

# - - - Temperature Generation
# Creates lists to be used in generate_temperature critical temp counts and temperature list  
temperature_list = []
critical_count = []

# Generates 10 sets (1 second between) of random integer temperatures between 20 and 120, prints each sensor # and temperature
def generate_temperature(temp_accept):
    for i in range(11):
        new_temp = random.randint(20,120)
        print(f"Sensor {i}: {new_temp}°F")
        temperature_list.append(new_temp)
        check_temperature(new_temp, i, temp_accept)
        time.sleep(1)

# if new temp added is over 100 degrees farenheit, 1 is added to the critical count list.
        if new_temp > temp_accept:
            critical_count.append(1)
    
    return new_temp, i

def check_temperature(new_temp, i, temp_accept):
    if new_temp < 80:
        temp_status = "NOMINAL"
        vehicle[f"Sensor {i}"] = f"Temperature Status: {temp_status}"

    elif 80 <= new_temp < temp_accept:
        temp_status = "CAUTION"
        vehicle[f"Sensor {i}"] = f"Temperature Status: {temp_status}"

    elif new_temp > temp_accept:
        temp_status = "CRITICAL"
        vehicle[f"Sensor {i}"] = f"Temperature Status: {temp_status}"

    return

generate_temperature(temp_accept)
# - - -

# - - - Print header
print("=======================================================")
print("Vehicle Temperature Sensor Reading Analysis")
print(f"Vehicle Name: {vehicle["name"]}")
print("=======================================================")
# - - -

# - - - Temperature Analysis and Display
avg_temperature = round(sum(temperature_list) / len(temperature_list), 2)
print(f"Average Temperature: {avg_temperature:.2f}°F")

max_temperature = max(temperature_list)
print(f"Highest Temperature: {max_temperature}°F")

min_temperature = min(temperature_list)
print(f"Lowest Temperature: {min_temperature}°F")

total_critical = len(critical_count)
print(f"Number of critical temps: {total_critical}")
# - - -

# - - - Go/No-Go Detemination
# If no critical temperatures are encountered, status is set to go
if total_critical == 0:
    print("Vehicle go for launch")
    vehicle["status"] = "GO"
# If one critical temperatures is encountered, status is set to hold
if total_critical == 1 :
    print("Caution: Review Required.")
    vehicle["status"] = "HOLD"
# If more than one critical temperatures are encountered, status is set to no-go
if total_critical > 1:
    print("NO-GO: Thermal Limit Exceeded")
    vehicle["status"] = "NO-GO"
# - - -

# - - - Post-run Status Display
print(f"Status: {vehicle["status"]}")
for i in range(11):
    print(f"Sensor {i} : {vehicle[f"Sensor {i}"]}")
# - - - 