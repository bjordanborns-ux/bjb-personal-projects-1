import time

print("Coffee Machine")

def start_up():
    start = input("Type Brew or Clean: ")
    if start == "Brew":
        time.sleep(1)
        print("Starting brewing process:")
        machine_start_time()
        machine_state = "Brewing"
        print("Machine State:", machine_state)
        return machine_state    
    elif start == "Clean":
        print("Cleaning mode selected.")
        machine_state = "Preparing for cleaning"
        return machine_state
    
def machine_start_time():
    start_time = time.time()
    return start_time

def machine_run_time(start_time):
    t = time.time()
    run_time = int (t - start_time)
    return run_time

def heat_rate():
    heat_raise_rate = int (3)
    return heat_raise_rate

def bean_rate():
    bean_usage_rate = int (1)
    return bean_usage_rate

def water_rate():
    water_usage_rate = int (2)
    return (water_usage_rate)

def water_level_calculation(water_usage_rate, water):
    water_level = int (water - water_usage_rate)
    water = water_level
    return water

def temperature_calculation(temperature, heat_raise_rate):
    temperature_new = int (temperature + heat_raise_rate)
    temperature = temperature_new
    return temperature

def bean_level_calculation(beans, bean_usage_rate):
    bean_level = (beans - bean_usage_rate)
    beans = bean_level
    return beans

def machine_run(beans, water, temperature):
    machine_state = "Brewing"
    beans = bean_level_calculation(beans, bean_rate())
    water = water_level_calculation(water_rate(), water)
    temperature = temperature_calculation(temperature, heat_rate())
    print("Bean Level:", beans, "Water Level:", water, "Temperature:", temperature, end='\r')
    return beans, water, temperature, machine_state

# Start of program

machine_state = "Idle"
temperature = 70
water = 100
beans = 100
print("Machine State:", machine_state)
machine_state = start_up()
if machine_state == "Brewing":
    start_time = machine_start_time()
while machine_state == "Brewing":
    beans, water, temperature, machine_state = machine_run(beans, water, temperature)
    if beans >= 30 and water >= 30:
        time.sleep(1)
    else:
        print()
        print("Brewing complete.")
        time.sleep(1)
        machine_state = "Preparing for cleaning"
        print("Machine State:", machine_state)
       
while machine_state == "Preparing for cleaning":   
    if water <=30 or water >=60:
        time.sleep(1)
        print("Beginning cleaning process.")
        time.sleep(1)
        print("Cleaning .", end='\r')
        time.sleep(2)
        print("Cleaning ..", end='\r')
        time.sleep(2)
        print("Cleaning ...")
        time.sleep(2)
        print("Cleaning complete.")
        machine_state = "Idle"
    else:
        print()
        time.sleep(1)
        print("Cleaning error. Please try again.")
        exit()

