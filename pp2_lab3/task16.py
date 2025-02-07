class StringManipulator:
    def __init__(self):
        self.input_string = ""  

    def getString(self):
        self.input_string = input("Жолды енгізіңіз: ")

    def printString(self):
        print(self.input_string.upper())

string_obj = StringManipulator()
string_obj.getString() 
string_obj.printString() 