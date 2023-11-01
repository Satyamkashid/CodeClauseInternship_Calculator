# Calculator in python using Object Oriented Programming

class Arithmatic:
    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

# Function Name : Addition
# Description : It will return the addition of two numbers
# Author Name : Satyam Sanjay Kashid
# Date : 01/11/2023

    def Addition(self):
        return self.No1 + self.No2
    
# Function Name : Subtraction
# Description : It will return the subtraction of two numbers 
# Author Name : Satyam Sanjay Kashid
# Date : 01/11/2023

    def Subtraction(self):
        return self.No1 - self.No2

# Function Name : Multiplication
# Description : It will return multiplication of two numbers
# Author Name : Satyam Sanjay Kashid
# Date : 01/11/2023

    def Multiplication(self):
        return self.No1 * self.No2

# Function Name : Division
# Description : It will return the division of two numbers
# Author Name : Satyam Sanjay Kashid
# Date : 01/11/2023

    def Division(self):
        if self.No2 == 0:
            return "Cannot divide by zero"
        return self.No1 / self.No2

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# Entry point Function
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def main():
    print("-------------Task By CodeClause-------------")

    print("-----------------Calculator----------------")

    print("Enter the First Number : ")
    No1 = int(input())

    print("Enter the Second Number : ")
    No2 = int(input())

    print("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\nEnter 5 To Perform All The Operation")
    value = int(input())

    obj = Arithmatic(No1,No2)
    if(value == 1):
        Add = obj.Addition()
        print("Addition of %s + %s is %s "% (No1,No2,Add))

    if(value == 2):
        Sub = obj.Subtraction()
        print("Subtraction of %s - %s is %s "% (No1,No2,Sub))

    if(value == 3):
        Mul = obj.Multiplication()
        print("Multiplication of %s * %s is %s "% (No1,No2,Mul))

    if(value == 4):
        Div = obj.Division()
        print("Division of %s / %s is %s "% (No1,No2,Div))

    if(value == 5):
        Add = obj.Addition()
        Sub = obj.Subtraction()
        Mul = obj.Multiplication()
        Div = obj.Division()

        print("Addition of %s + %s is %s "% (No1,No2,Add))
        
        print("Subtraction of %s - %s is %s "% (No1,No2,Sub))
        
        print("Multiplication of %s * %s is %s "% (No1,No2,Mul))
        
        print("Division of %s / %s is %s "% (No1,No2,Div))

if __name__ == "__main__":
    main()