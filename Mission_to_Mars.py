import time

def launch():
    print("---------------")
    print("Mission To Mars")
    print("---------------")
    print("")
    time.sleep(0.5)
    print("Starting count down...")
    print("")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Lift Off!")
    print("")
launch()

def travel_time_to_mars(distance, speed, fuel, crew_ready, onboard_systems, mars_weather_conditions):
    time = distance / speed
    if speed < 20000:
        print("warning: speed is too slow for a timely arrival!")
        print("")
    elif speed >50000:
        print("warning: Speed is too fast, Risk of overshooting The planet!")
        print("")
    else:
        print("Speed is optimal for Mission.")
        print("")
    print("Travel time to landing is:", time, "hours")
    print("")

    if fuel < 500000:
        print("Warning: not enough fuel")
        print("")
    else:
        print("fuel levels are sufficient")
        print("")
    
    if crew_ready:
        print("crew is ready for mission.")
        print("")
    else:
        print("crew is not ready mission delayed")
        print("")

    if onboard_systems:
        print("onboard Systems running")
        print("")
    else:
        print("onboard System Error")
        print("")

    if mars_weather_conditions:
        print("Opimal Weather conditions on Mars")
        print("")
    else:
        print("Poor weather conditions on Mars")
        print("")
print("---------")
print("Mission 1")
print("---------")
travel_time_to_mars(225000000, 25000, 600000, True, True, True)
time.sleep(1)
print("")
print("---------")
print("Mission 2")
print("---------")
travel_time_to_mars(225000000, 15000, 400000, True, False, False)
time.sleep(1)
print("")
print("---------")
print("Mission 3")
print("---------")
travel_time_to_mars(225000000, 25000, 500000, False, True, True)

