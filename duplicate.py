student_data = {
    "id1": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}


result = {}
seen_values = []

for student_id, details in student_data.items():
    unique_value = (details["name"], details["class"], details["subject_integration"])

    if unique_value not in seen_values:
        seen_values.append(unique_value)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)