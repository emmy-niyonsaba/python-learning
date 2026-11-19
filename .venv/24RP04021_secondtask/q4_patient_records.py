"""Question 4: Hospital Patient Record Management


e) Why a dictionary is better than a list:
   Patient IDs are unique, so they work naturally as dictionary keys. Looking
   up a patient by ID is instant (hash lookup) instead of looping through a
   list, duplicate IDs are impossible because keys are unique, and a record can
   be updated directly with patients[id]["temperature"] = value. A list would
   require scanning every record and manual duplicate checks.
"""

patients = {
    "P001": {"name": "Jean Claude", "age": 34, "temperature": 36.8},
    "P002": {"name": "Marie Uwase", "age": 28, "temperature": 37.2},
    "P003": {"name": "Eric Habimana", "age": 45, "temperature": 38.1},
    "P004": {"name": "Aline Mukamana", "age": 19, "temperature": 36.5},
    "P005": {"name": "Patrick Nshimiyimana", "age": 62, "temperature": 37.9},
}


def read_number(prompt, low, high, label, integer=False):
    while True:
        try:
            value = int(input(prompt)) if integer else float(input(prompt))
        except ValueError:
            print("Error: enter a valid number.")
            continue
        if not (low <= value <= high):
            print(f"Error: {label} must be between {low} and {high}.")
            continue
        return value


def show_patient(pid):
    p = patients[pid]
    print(f"ID: {pid} | Name: {p['name']} | Age: {p['age']} | Temp: {p['temperature']} °C")


def search_patient():
    pid = input("Enter patient ID: ").strip().upper()
    if pid in patients:
        show_patient(pid)
    else:
        print("Patient not found.")


def update_temperature():
    pid = input("Enter patient ID: ").strip().upper()
    if pid not in patients:
        print("Patient not found.")
        return
    temp = read_number("New temperature (°C, 30-45): ", 30, 45, "temperature")
    patients[pid]["temperature"] = temp
    print("Temperature updated.")
    show_patient(pid)


def register_patient():
    pid = input("New patient ID: ").strip().upper()
    if not pid:
        print("Error: ID cannot be empty.")
        return
    if pid in patients:
        print(f"Registration refused: ID '{pid}' already exists.")
        return
    name = input("Name: ").strip()
    if not name:
        print("Error: name cannot be empty.")
        return
    age = read_number("Age (0-120): ", 0, 120, "age", integer=True)
    temp = read_number("Temperature (°C, 30-45): ", 30, 45, "temperature")
    patients[pid] = {"name": name, "age": age, "temperature": temp}
    print("Patient registered successfully.")


def list_patients():
    for pid in patients:
        show_patient(pid)


def main():
    menu = """
=== Patient Registration System ===
1. Search patient by ID
2. Update patient temperature
3. Register new patient
4. List all patients
5. Exit"""
    actions = {"1": search_patient, "2": update_temperature,
               "3": register_patient, "4": list_patients}
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye.")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
