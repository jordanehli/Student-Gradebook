#Author: Jordan Ehlinger
#Assignment Number & Name: HW5A Gradebook
#Due Date: N/A
#Program Description: Receive's the student't name and grade average


def main():

    import Ehlinger_Jordan_HW5_Functions
    
    #Create a variable to control the loop.
    another = 'y'

    #Open the gradebook.txt file in write mode.
    gradebook_file = open('gradebook.txt', 'w')

    #Create accumulator
    total = 0
    #Add records to the file.
    while another == 'y' or another == 'Y':
        #Get the name and grade data.
        print("Enter the student's name and grade numeric average:")
        name = Ehlinger_Jordan_HW5_Functions.check_valid_name()
        grade = Ehlinger_Jordan_HW5_Functions.check_valid_average()

        #Append the data to the file.
        gradebook_file.write(name + '\n')
        gradebook_file.write(str(grade) + '\n')
        #add entry to accumulator
        total+=1
        #Determine whether the user wants to add another student to the file
        print("Do you want to add another student's information?")
        another = input('Y = yes, anything else = no: ')

    #Show the user the number of entries
    print()
    print(total,"students were added to the gradebook")

    #Close the file.
    gradebook_file.close()

#Call the main function.
main()

        
