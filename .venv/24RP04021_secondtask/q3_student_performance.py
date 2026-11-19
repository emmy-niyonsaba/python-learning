#Question 3: College Student Performance Analysis

"""a) Collection choice: a DICTIONARY {name: mark}.
   Each student name is a unique key mapped directly to one mark, so marks can
   be looked up and updated by name in O(1) time without touching other records.
   A list would need searching/indexing, and a tuple is immutable.
"""

students = {"Alice": 85, "Eric": 72, "Diane": 91, "Patrick": 48, "Aline": 76}


def statistics(data):
    """b) average, highest and lowest mark."""
    average = sum(data.values()) / len(data)
    top_name = max(data, key=data.get)
    low_name = min(data, key=data.get)
    return average, top_name, low_name


def above_average(data):
    """c) students who scored above the class average."""
    avg = sum(data.values()) / len(data)
    return {n: m for n, m in data.items() if m > avg}


def update_mark(data):
    """d) update one student's mark; other records remain untouched."""
    name = input("Enter student name to update: ").strip().title()
    if name not in data:
        print(f"Student '{name}' not found.")
        return
    while True:
        try:
            mark = float(input(f"New mark for {name} (0-100): "))
            if 0 <= mark <= 100:
                break
            print("Error: mark must be between 0 and 100.")
        except ValueError:
            print("Error: enter a valid number.")
    data[name] = int(mark) if mark.is_integer() else mark
    print(f"{name}'s mark updated to {data[name]}.")


def display_ranking(data):
    """e) descending order of marks."""
    print(f"\n{'Rank':<6}{'Name':<12}{'Mark':>6}")
    ranked = sorted(data.items(), key=lambda item: item[1], reverse=True)
    for rank, (name, mark) in enumerate(ranked, start=1):
        print(f"{rank:<6}{name:<12}{mark:>6}")


def main():
    avg, top, low = statistics(students)
    print("=== Class Statistics ===")
    print(f"Class average : {avg:.2f}")
    print(f"Highest mark  : {students[top]} ({top})")
    print(f"Lowest mark   : {students[low]} ({low})")

    print("\n=== Students above class average ===")
    for name, mark in above_average(students).items():
        print(f"{name}: {mark}")

    print("\n=== Update a mark ===")
    update_mark(students)

    avg, top, low = statistics(students)
    print(f"\nNew class average: {avg:.2f}")
    print("\n=== Ranking (descending) ===")
    display_ranking(students)


if __name__ == "__main__":
    main()
