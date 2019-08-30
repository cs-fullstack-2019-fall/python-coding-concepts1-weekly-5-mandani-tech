# # python-coding_concepts1-weekly-5
#
# You must push BEFORE 2:30pm or your answers will not be graded.
# Once you finish, do not leave the property. You will be interviewed about your questions at 2:45pm.
#
# DON'T FORGET TO USE THE assessment_handout.txt FILE.
#
# Do NOT use any notes or previous projects on this test.
# Each individual question file has the same questions as the README.
# ### Problem 1:
# Ask a user for the year they were born by calculating their age.
# Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”
#
userInput=int(input("Enter the year were you born in : "))
userAge= 2019-userInput
print(f'You are {userAge} years old!')

# ### Problem 2:
# Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”.
# Otherwise print “Hello Student”
#
userString= input("Please enter your name :")
if userString=="Kenn":
    print(f'Hello Teacher')
elif userString=="Kevin":
    print(f'Hello Teacher')
elif userString=="Erin":
    print(f'Hello Teacher')
elif userString=="Autumn":
    print(f'Hello Teacher')
else:
    print("Hello Student")

# ### Problem 3:
# Ask the user for a negative number. Print from 7 down to the user's negative number.
You must include the user's number.
userNumber=int(input("Enter a Negative Number here: "))
for i in range(7,userNumber-1,-1):
    print(i)

#
# ### Problem 4:#todo
# Ask the user to enter a number between -10 to -5.
# If their input is not between the two numbers ask them to do it again until they get it right.
# Afterward they print the correct number, print "Good job"
numList=[-10,-9,-8,-7,-6,-5]
usrNumInput=0
usrNumInput=int(input("Enter a number between -10 and -5: "))
for i in numList:
    while usrNumInput != numList[i]:
        print(usrNumInput)
        usrNumInput=int(input("Try again Enter a number between -10 and -5: "))
print(f"Good Job you entered {usrNumInput}")


# ### Problem 5:
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"].
# Print the list in reverse without using a list method.
# squad = ["One", "Two", "Three", "Four", "Five"]
# for i in range (0,-5,-1):
#     print(squad[i])

# ### Problem 6:
# Create a function that will have the string firstName as a parameter.
# In the function ask the user for their last name.
# Print "Hello [FIRST & LAST NAME]" in the function. Call that function

def nameFunc(firstName):
    lastName=input("Enter your Last Name: ")
    print(f"Hello {firstName}  {lastName} !")

fname=input("Enter your First Name : ")
nameFunc(fname)

# ### Problem 7:
# Create the class Books with name, rating, genre, and author properties/attributes.
# Create a class method that will change the rating of the book. Outside of the class,
# create three objects of the class Book and put them in an array. Lastly,
# USING THE ARRAY print only the names of the books using any method we’ve learned in class.

class Books:
    def __init__(self,name, rating, genre, author):
        self.name=name
        self.rating=rating
        self.genre=genre
        self.author=author
    def changerating(self,newRating):
        self.rating=newRating
    def __str__(self):
        return f'{self.name}\n{self.rating}\n{self.genre}\n{self.author}'


book1=Books("Alchemist",5,"fiction","Paul Coho")
book2=Books("7 Habbit",4,"Motivational","Steven Cohen")
book3=Books("No God But God",4.8,"fiction","Anonymous")
bookArray=[book1,book2,book3]

for i in bookArray:
    print(i.name)





#
# ### Problem 8:
# Create a function that asks the user to enter a number.
# If the number is between and include -50 and 5, return "Funds too low".
# If the number is between 5 and 50, return “You should add more funds.”
# If the number is more than 50, return “Just enough.”
#
def NumberFunc():
    userNumber1=int(input("Enter a Number here:"))
    if userNumber1>-50 and userNumber1<=5:
        result=(f"Funds too low")
    elif userNumber1>5 and userNumber1<=50:
        result=(f"You should add more funds.")
    elif userNumber1>50:
        result=(f"Just Enough")
    return result

print(NumberFunc())


# ### Problem 9:
# Ask the user for a positive number. Create an empty array and starting from zero,
# add each number by 1 into the array. Print EACH ELEMENT of the array.

askuserNum=int(input("Please Enter Positive Number"))
for i in range (0,askuserNum):
    i=i+1
    print(i)


# ### Problem 10:
# Create a new empty array called pet_list. Create a Pet class with a type and
# breed attribute/property. Include a method that will print each attribute/property.
# Add 3 pet objects to the pet_list array. Print the attributes/properties for each pet.
 pet_list=[]
 class Pet:
     def __init__(self, type,breed):
         self.type=type
         self.breed=breed
     def  printtype(self):
         print(f'{self.type}')

     def  printbreed(self):
         print(f'{self.breed}')

dog1=Pet("vcodsai","kvds")
dog2=Pet("vjbjkai","kvsdss")
dog3=Pet("vcvsdfsai","kvwywys")

