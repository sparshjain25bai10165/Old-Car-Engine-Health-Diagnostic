# ==========================================
# OLD CAR ENGINE HEALTH DIAGNOSTIC
# ==========================================
# Student Name : Sparsh Jain
# Reg. No.     : 25BAI10165
# Course       : Programming in Python
# Topic        : Old Car Engine Health Diagnostic
# Project Type : Python Console Application
# ==========================================


# Checks engine temperature
def check_temperature(temperature):
    if temperature <= 95:
        return 25, "Temperature is normal"
    elif temperature <= 105:
        return 15, "Temperature is slightly high"
    else:
        return 0, "Engine overheating"


# Checks engine oil pressure
def check_oil_pressure(oil_pressure):
    if oil_pressure >= 30:
        return 25, "Oil pressure is normal"
    elif oil_pressure >= 20:
        return 15, "Oil pressure is slightly low"
    else:
        return 0, "Oil pressure is very low"


# Checks battery voltage
def check_battery(battery_voltage):
    if 12.4 <= battery_voltage <= 14.7:
        return 25, "Battery voltage is normal"
    elif battery_voltage >= 11.5:
        return 15, "Battery voltage is weak"
    else:
        return 0, "Battery voltage is very low"


# Checks unusual engine noise
def check_engine_noise(engine_noise):
    if engine_noise == "No":
        return 25, "No unusual engine noise"
    else:
        return 0, "Unusual engine noise detected"


# Gives final engine health category
def get_health_category(score):
    if score >= 90:
        return "EXCELLENT"
    elif score >= 70:
        return "GOOD"
    elif score >= 50:
        return "NEEDS SERVICE"
    else:
        return "CRITICAL"


def run_engine_diagnostic():
    print("\n======================================")
    print("     OLD CAR ENGINE HEALTH DIAGNOSTIC")
    print("======================================")

    print("Student Name : Sparsh Jain")
    print("Reg. No.     : 25BAI10165")
    print("======================================")

    try:
        temperature = float(input("Enter engine temperature (°C): "))
        oil_pressure = float(input("Enter oil pressure (PSI): "))
        battery_voltage = float(input("Enter battery voltage (V): "))
        engine_noise = input(
            "Is there any unusual engine noise? (Yes/No): "
        ).strip().capitalize()

    except ValueError:
        print("Invalid input. Please enter numbers where required.")
        return

    if temperature < 0 or oil_pressure < 0 or battery_voltage < 0:
        print("Please enter valid positive values.")
        return

    temp_score, temp_status = check_temperature(temperature)
    oil_score, oil_status = check_oil_pressure(oil_pressure)
    battery_score, battery_status = check_battery(battery_voltage)
    noise_score, noise_status = check_engine_noise(engine_noise)

    total_score = temp_score + oil_score + battery_score + noise_score
    health = get_health_category(total_score)

    print("\n----------- DIAGNOSTIC REPORT -----------")
    print(f"Temperature        : {temperature:.1f} °C")
    print(f"Temperature Status : {temp_status}")
    print(f"Oil Pressure       : {oil_pressure:.1f} PSI")
    print(f"Oil Status         : {oil_status}")
    print(f"Battery Voltage    : {battery_voltage:.2f} V")
    print(f"Battery Status     : {battery_status}")
    print(f"Engine Noise       : {engine_noise}")
    print(f"Noise Status       : {noise_status}")
    print("-----------------------------------------")
    print(f"Health Score       : {total_score}/100")
    print(f"Engine Condition   : {health}")
    print("-----------------------------------------")

    if health == "EXCELLENT":
        print("Recommendation     : Continue regular maintenance.")
    elif health == "GOOD":
        print("Recommendation     : Check during the next service.")
    elif health == "NEEDS SERVICE":
        print("Recommendation     : Professional servicing is recommended.")
    else:
        print("Recommendation     : Immediate professional inspection is recommended.")

    print("-----------------------------------------")


# Main program
if __name__ == "__main__":
    run_engine_diagnostic()
