def calculate_average(numbers):
    if not numbers:
        return 0
    
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 2)

school_project_data = [5.5, 6.7, 7.8, 8.9]
average_grade = calculate_average(school_project_data)
print(f"The average grade in the project is: {average_grade}")
