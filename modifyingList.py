# Empty List Variable
list = []

# Function to add data on list
def AddDataList(data):
    # Append the List Variable to add data
    list.append(data)
    # Return the List Variable
    return list

# Function to update the index data
def UpdateTheIndexData(index,data):
     # Try and Except to get the user input out of range from the index
    try:
        # Get the list of index and change the index data using data variable
        list[index] = data
        # Return list variable
        return list
    except:
        # Return error message
        return "Error your index is out of range!"


# Questions
user_input = "Add data you want to list (type exit or EXIT to stop)  :  "
get_index = "Type the index number you want to update : "
data_change = "Add the data to update your list : "

# Try and Except to get the user input error message
try:
    # Use while true to ask question infinitely
    while True:
        # Hold the user_input question to data variable
        data = str(input(user_input))

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
    # Hold the data_change to change variable
    change = str(input(data_change))

    # Print the updated list
    print("The updated list are : ", UpdateTheIndexData(index,change))
except:
    # Print the error
    print("Error Inputs!")
