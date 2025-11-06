def pts_to_grade(points):
    # Initialize the grade as an empty string
    grade = ''
    
    # Check the conditions for the grade
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    
    # Return the final grade
    return grade

# Test the function with a score of 15
test_result = 15
final_grade = pts_to_grade(test_result)

# Print the result
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}.')