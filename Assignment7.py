# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Picking, Unpickling and Structured Error Handling
# ChangeLog (Who,When,What):
# PYChang, 11.30.2020,Modified code to complete assignment 7
# ---------------------------------------------------------------------------- #

import pickle

# Data -------------------------#
strFileName = 'ChristmasGift.txt'
lstItem = []
# Processing --------------------#

def store_data_to_file(objFile, list_of_data):
    objFile = open("/Users/pchang/Documents/_PythonClass/Assignment07/ChristmasGift.txt", "wb")
    pickle.dump(list_of_data, objFile)
    objFile.close()


def read_data_from_file(objFile):
    objFile = open("/Users/pchang/Documents/_PythonClass/Assignment07/ChristmasGift.txt", "rb")
    list_of_data = pickle.load(objFile)
    objFile.close()
    return list_of_data


# Presentation  -----------------#
class IO:
    @staticmethod
    def enter_item():
        while True:
            try:
                item_name = str(input("Enter an item for christmas wishlist: "))
                if item_name.isnumeric():
                    raise Exception('Please enter string only')
            except Exception as e:
                print(e, e.__doc__, type(e))
            else:
                break
        while True:
            try:
                int_priority = int(input("Enter on a scale of 1 to 5, how much you want this gift: "))
                if int_priority > 5:
                    raise Exception("Please enter a number between 1 to 5 only")
            except Exception as e:
                print(e, e.__doc__, type(e))
            lstItem = [item_name, int_priority]
            return lstItem

# Main Body -------------------------------#
# get user input #
christmas_list = IO.enter_item()

# store the list into a binary file - pickle #
store_data_to_file(strFileName, christmas_list)

# read data from the file - unpickle #
print(read_data_from_file(strFileName))


