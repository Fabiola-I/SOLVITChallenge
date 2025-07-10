#  Write a Python program that creates a dictionary representing a student's grades in 
# different subjects. - Prompt the user to enter the subject name and the corresponding grade for each 
# subject. - Store the subject-grade pairs in the dictionary. - Calculate the average grade. - Display the dictionary and the average grade. 
# These exercises cover a range of Python concepts and provide practical examples to 
# reinforce learning. They also encourage problem-solving and critical thinking skills. Feel free 
# to modify the exercises as needed to suit your learning objectives and level of expertise.
grades={}
subject=input("enter the your first subject name:")
marks=float(input("enter the marks of {}:".format(subject)))

grades[subject]=marks
subject_2=input("enter the second subject name :")
marks_2=float(input("enter the marks of {}:".format(subject_2)))
grades[subject_2]=marks_2

subject_3=input("enter the third subject name :")
marks_3=float(input("enter the marks of {}:".format(subject_3)))

grades[subject_3]=marks_3
print("the grades are {}".format(grades))
average_grades=sum(grades.values())/len(grades)
print("the average of the grades is {}".format(average_grades)) 