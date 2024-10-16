# Empty list variable
list = []

# Function to add data on list
def AddDataList(data):
    # Append the List Variable to add data
    list.append(data)
    # Return the List Variable
    return list


# Slice Function to slice the list
def Slice(slice1,slice2):
     
    # Conditional Statement to get the slice logic
    if slice1 == 0 and slice2 == 0 :
        slice = list[:]
        return slice
    elif slice1 != 0 and slice2 == 0:
        slice = list[slice1:]
        return slice
    elif slice1 == 0 and slice2 != 0:
        slice = list[:slice2]
        return slice
    else:
        slice = list[slice1:slice2]
        return slice
   

# Questions
user_input = "Add data you want to list (type exit or EXIT to stop)  :  "
slice_number1 = "(Optional Please if you don't like any start number index just type 0) : "
slice_number2 = "(Optional Please if you don't like any end number index just type 0) : "

# Try and Except to get the error inputs
try:
    # Use while True to ask question infinitely
    while True:

         # Hold the question user_inputs to data variable
        data = str(input(user_input))

        # Use conditional to exit the program
        if data == 'exit' or data == 'EXIT':
           break
        
        # Hold the AddDataList Function to result variable
        result = AddDataList(data)

         # Print the Result
        print("Not final list result : ", result , "\n")
    
    # Print the Final Result
    print("The final list result is : ", result , "\n")

    # Hold the slice_number1 question to slice1 variable
    slice1 = int(input(slice_number1))
    # Hold the slice_number2 question to slice2 variable
    slice2 = int(input(slice_number2))
    
except:
    # Print error inputs
    print("Error Inputs!")

# Print slice function
print(Slice(slice1,slice2))
