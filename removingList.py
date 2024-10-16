# Empty List Variable
list = []

# Function to add data on list
def AddDataList(data):
    # Append the List Variable to add data
    list.append(data)
    # Return the List Variable
    return list

# Function to remove the data from list 
def RemoveDataList(data):
    try:
        # Remove the data inside list
        list.remove(data)
        # Return list variable
        return list
    except:
        # Return error message
        return "Error your data is not available "


# Questions
user_input = "Add data you want to list (type exit or EXIT to stop)  :  "
remove_data = "Type the data to remove it from the list : "

# Try and Except to get the user inputs error 
try:
    # Use while True to ask question infinitely
    while True:

        # Hold the user_input question to data variable
        data = str(input(user_input))

        # Use conditional to exit the program
        if data == 'exit' or data == 'EXIT':
            break
        
        # Hold the AddDataList Function to result variable
        result = AddDataList(data)

        # Print the result
        print("Not final list result : " , result , "\n")

    # Print the final result
    print("The final list result is : " , result , "\n")

    # Hold the remove_data question to remove variable
    remove = str(input(remove_data))

    # Print the updated list after removing a data from the list
    print("The updated list after removing the data from list are : ", RemoveDataList(remove))

except:
    # Print the error message
    print("Error Inputs!")