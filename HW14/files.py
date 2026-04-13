"""Student data management program: recording to a file
   analyzing academic performance, and displaying statistics."""
from typing import Any, Dict, List

student_data: List[Dict[str, Any]] = [
    {"name": "John", "group": "A1", "grades": [5, 4, 5]},
    {"name": "James", "group": "B2", "grades": [4, 4, 2]},
    {"name": "Edward", "group": "С3", "grades": [6, 2, 3]},
    {"name": "Joe", "group": "D4", "grades": [5, 3, 5]},
]

total_students = 0
group_stats = {}

try:

    with open("students.txt", "w", encoding="utf-8") as file:
        for student in student_data:
            if student["grades"]:
                average = sum(student["grades"]) / len(student["grades"])
                file.write(f"{student['name']} {student['group']} {average}\n")

    with open("students.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue
            total_students += 1
            group = parts[1]
            score = float(parts[2])
            if group not in group_stats:
                group_stats[group] = [1, score]
            else:
                group_stats[group][0] += 1
                group_stats[group][1] += score

    if total_students > 0:
        print(f"Total students: {total_students}")
        with open("students.txt", "a", encoding="utf-8") as file:
            file.write("\nStatistics\n")
            file.write(f"Total students: {total_students}\n")
            for group, data in group_stats.items():
                count = data[0]
                total_score = data[1]
                group_average = total_score / count
                info = f"Group {group}: students - {count}, {group_average}"
                print(info)
                file.write(info + "\n")
    else:
        print("No student data found.")

except Exception as error:  # pylint: disable=broad-exception-caught
    print(f"Something went wrong: {error}")
