#Author: Jordan Ehlinger
#Assignment Number & Name: HW5C Gradebook
#Due Date: N/A
#Program Description: Display all students and their grades as well as the highest and lowest overall scores


def main():
    #Open the gradebook.txt file.
    gradebook_file = open('gradebook.txt', 'r')

    #Initialize list of grades for min & max
    grade_list=[]
    
    #Read the first name in the gradebook.
    name = gradebook_file.readline()

    #Read the rest of the file.
    while name != '':
        #Read the grade field.
        grade = float(gradebook_file.readline())
        grade=int(grade)

        #Strip the \n from the name.
        name = name.rstrip('\n')

        #Display the record.
        print(name, "'s grade is ", grade, sep='')

        #Add grade to grade list
        grade_list.append(grade)
        
        #Read the next name.
        name = gradebook_file.readline()

    #Display the highest and lowest grade.
    print("The highest grade is:", max(grade_list))
    print("The lowest grade is:", min(grade_list))
    
    #Close the file.
    gradebook_file.close()

#Call the main function.
main()
