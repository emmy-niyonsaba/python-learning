"""Question 2: Smart Agriculture Irrigation System
"""

MOISTURE_MIN, MOISTURE_MAX = 0, 100        
TEMP_MIN, TEMP_MAX = -10, 60                
MOISTURE_THRESHOLD = 30
TEMP_THRESHOLD = 25


def read_float(prompt, low, high, label):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Error: please enter a number.")
            continue
        if not (low <= value <= high):
            print(f"Error: {label} must be between {low} and {high}.")
            continue
        return value


def read_water():
    while True:
        answer = input("Is there water in the tank? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Error: please answer yes or no.")


def main():
    print("=== Smart Irrigation Controller ===")
    print(f"Limits: moisture {MOISTURE_MIN}-{MOISTURE_MAX}%, "
          f"temperature {TEMP_MIN} to {TEMP_MAX} °C")
    moisture = read_float("Soil moisture (%): ", MOISTURE_MIN, MOISTURE_MAX, "moisture")
    temp = read_float("Temperature (°C): ", TEMP_MIN, TEMP_MAX, "temperature")
    tank_has_water = read_water()

    dry = moisture < MOISTURE_THRESHOLD
    hot = temp > TEMP_THRESHOLD

    print("\n--- Decision ---")
    if dry and hot and tank_has_water:
        print("IRRIGATION ACTIVATED: soil is dry "
              f"({moisture}% < {MOISTURE_THRESHOLD}%), it is hot "
              f"({temp}°C > {TEMP_THRESHOLD}°C) and the tank has water.")
    else:
        print("IRRIGATION DEACTIVATED. Reason(s):")
        if not tank_has_water:
            print(" - The water tank is empty.")
        if not dry:
            print(f" - Soil moisture ({moisture}%) is not below {MOISTURE_THRESHOLD}%.")
        if not hot:
            print(f" - Temperature ({temp}°C) does not exceed {TEMP_THRESHOLD}°C.")


if __name__ == "__main__":
    main()
