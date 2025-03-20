import pandas as pd 

# Read in the data from the CSV file
data = pd.read_csv('schoolproject.csv')

# Calculate the mean of the "Grade" column
mean_grade = data['Grade'].mean()

# Print the result
print(f"The mean grade is: {mean_grade}")