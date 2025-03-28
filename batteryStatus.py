import psutil
import sys


def check_battery(speak):
    print("Checking battery status...")

    battery_status = psutil.sensors_battery()

    if battery_status is None:
        print("Battery information not available.")
        return

    battery = battery_status.percent
    charger_plugin = battery_status.power_plugged

    if 30 >= battery >= 19 and not charger_plugin:
        speak(f"Power levels are critically low , {battery} %")

    elif battery < 10 and not charger_plugin:
        speak("Low power detected.Closing all active applications....")
        sys.exit()

    else:
        print(f"Battery capacity: {battery}%")

    # if battery <=20 :
    # print(f" battery : {battery}, initiated battery saver, i recommend you to plugin charger")
    # else:
# check_battery()
