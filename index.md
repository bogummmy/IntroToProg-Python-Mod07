# Pickling and Structured Error Handling
## IntroToProg-Python Assignment 7

### Introduction
This document will walk through the steps and process on how I created the Python Script for assignment 7. The assignment is to create a new script that demonstrate pickling and structured error handling work.   

To demonstrate pickling and structured error handling, I create a script that asks user to create a Christmas wish list by entering an item and rank the item on a scale of 1 to 5. The script will store the data in a binary file. I also build in some error handling language in the script that will raise warnings to user when data entered is in the incorrect format.

The primary usage and benefit of using pickle in python is to serializing the deserializing the Python object structure. It is an efficiency way of storing the object in a database. 

### Step 1. Pickle and Unpickle
  - **import pickle** – the module pickle is called
  -	**pickle.dump()** – this function is used to serialize (write) to a binary file. The function will open the ChristmasGift.txt file and add new data to the file. If the           file does not exist, it will create the file. 
  -	**pickle.load()** – this function is used to deserializing (read) from a binary file. The function will open the ChristmasGift.txt file that we created earlier.
![Figure 1. Pickling and Unpickling](https://github.com/bogummmy/IntroToProg-Python-Mod07/blob/main/docs/Figure%201.%20Pickle%20and%20Unpickle.png "Figure 1.")


### Step 2. Create a Christmas Wish List with User Input and Error Handling
  - Now, I create function that asks user to enter an item and a rank for the item from a scale of 1 to 5. 
  - There are two error handling mechanism build in the function.    
  - The first one is to check if the Christmas wish list item entered is a string (not numeric). If it’s a string, then an exception will be raised with the message “Please enter string only”. 
  - The second is to check if the number entered is between 1 and 5. If the number is greater than 5, then an exception will be raised with the message “Please enter a number between 1 to 5 only”. 
 ![Figure 2. Get user Input and Error Handling](https://github.com/bogummmy/IntroToProg-Python-Mod07/blob/main/docs/Figure%202.%20User%20input%20with%20error%20handling.png "Figure 2.")
 
### Step 3. Main Body 
Now, we have successfully set up functions for pickle, unpickle and get user input, we are ready to create the main body of the script. We will call the **enter_item()** function to get user input. And use the **store_data_to_file()** function to store the list to a binary file (pickle) and **print(read_data_from_file())** function to ready data from file (unpickle).
 ![Figure 3. Main Body](https://github.com/bogummmy/IntroToProg-Python-Mod07/blob/main/docs/Figure3.%20Main%20Body.png "Figure 3.")
 

