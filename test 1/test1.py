import random
import time

temperature_list = []
critical_count = []
def generate_temperature():
    for i in range(0,10,1):
        new_temp = random.randint(20,120)
        print(f"Sensor {i}: {new_temp}°F")
        temperature_list.append(new_temp)
        time.sleep(1)
        
        if new_temp >= 100:
            critical_count.append(1)
    
    return

generate_temperature()

avg_temperature = sum(temperature_list) / len(temperature_list)
print(f"Average Temperature: {avg_temperature}°F")

max_temperature = max(temperature_list)
print(f"Highest Temperature: {max_temperature}°F")

min_temperature = min(temperature_list)
print(f"Lowest Temperature: {min_temperature}°F")

total_critical = len(critical_count)
print(f"Number of critical temps: {total_critical}")

vehicle = {
    "name" : "Test Article 1",
    "status" : ""
}

if total_critical == 0:
    print("Vehicle go for launch")
    vehicle["status"] = "GO"

if total_critical == 1 :
    print("Caution: Review Required.")
    vehicle["status"] = "HOLD"

if total_critical > 1:
    print("NO-GO: Thermal Limit Exceeded")
    vehicle["status"] = "NO-GO"

