# Empty List Variable
list = []

# Function to add data on list
def AddDataList(data):
    # Append the List Variable to add data
    list.append(data)
    # Return the List Variable
    return list

# Function to get the index and return it
def GetIndexToPrint(index):
    # Try and Except to get the user input out of range from the index
    try:
        # Hold the list index to result variable
        result = list[index]
        # Return the result variable
        return result
    except:
        # Return error message
        return "Error your index is out of range!"
    


# Questions
user_inputs = "Add data you want to list (type exit or EXIT to stop)  : "
get_index = "Type the index number of the data to print it : "



# Try and Except to catch User Input Error
try:
    # Use while True to ask question infinitely
    while True:

        # Hold the question user_inputs to data variable
        data = str(input(user_inputs))

        # Use conditional to exit the program
        if data == 'exit' or data == 'EXIT':
            break

        # Hold the AddDataList Function to result variable
        result = AddDataList(data)
        
        # Print the Result
        print("Not final list result : " , result , "\n")


    # Print the Final Result
    print("The final list result is : " , result , "\n")

        
    # Hold the get_index question to index variable
    index = int(input(get_index))

    # Print the index data you get from the list
    print("The index data you get from the list is : ", GetIndexToPrint(index))
except:
    # Print the error
    print("Error Inputs!")






