# Exception Handling
# Error occur due to mistakes in the code that prevent it from running. These can be syntax errors or logical errors.
# --- Syntax error ----
# print("Hello world" #Missing closing parenthesis
# Now this above code will give the error of syntax.

# Indentation Errors
# def function():
# print("hello")  #No indentation

# function()


# Here already know what is indentation and if you don't follow it you will get the error.
# There is one more tab error when you mix tabs and spaces.
# These errors cannot be handled. but what can be handled are exceptions.

# Exceptions
#   1.Excepitons are unexcepeted events or errors that occurs during the execution of a program, which disrupts the normal flow of the program.
#  print("Start")
#  print(10/0)  #Raise "ZeroDivisionError: division by zero"
#  print("End") #This line will never run
# Now this is a ZeroDivisionError and cab be counted as Exception and because of this exception the next line cannot be executed.
# Like this there are many other exceptions just leave the three errors we saw at start otherwise others are exceptions.
# And the good part is we can handel them lets see how.


# agar user input me 0 nummber input de diye to "ZeroDivisionError: division by zero" aa jayega and aaage ka code ke normalflow kharab ho jayega.
# a = int(input("Tell your number :- "))
# print(10/a)

# print("Ok i have done the division..")

# ***************************************************************************
# Exception Handling
# ***************************************************************************
#       Keyword                     Purpose
#        try        -->           Wrap the block of code that might cause an exception.
#       except      -->           Handle the exception if it occurs
#        else       -->           Run code only if no exception occurs
#       finally     -->           Run code no matter what, whether there's an exception or not
#       raise       -->           Manually throw an exception

# a = int(input("Tell your number :- "))
# try:
#     print(10/a)
# except Exception as err:   #koi bhi exception occur hone pe ye except block run hoga, else block run nahi hoga.
#     print(f"Sorry there is an error as : {err} ")


# else:  #Koi exception code me nahi aaya to else block run hoga agar exception aaya to 'except' block run hoga.
#     print("Good there is no exception..")

# finally:   #ye humesa run hoga chae exception aaye ya na aaye
#     print("I will run no matter what..")



# print("Ok i have done the division..")

# -----> Accept age only above of 18+
age=int(input("Tell you age :- "))
try:

    if age < 10 or age>18:
        #ye manully throw exception, chhe wo exception ho ya nahi
        raise ValueError("Your age need must be between 10 to 18")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"An error occured as : {err}")
    
print("The club will start soon")



