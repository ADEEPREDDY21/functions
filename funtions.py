#Function is reusable  block of code  that performs a specific task.
# You define function with "def" keyword followed by function name and parameters in parentheses.and a colon at the end of the line
#Function can take arguments, return values and have a body that contains a series of statements to be performed
#Function can be called multiple times from different parts of the program
#Functions there are two types of functions in python: built-in functions and user-defined functions
#Built-in functions are functions that are already defined in python and can be used directly in the program
#User-defined functions are functions that are defined by the user in the program by using the def keyword
#Functions have formal arguements and Actual argurements
print("Example for the user defined function")
def my_function(x,r):#here x and r are formal arguments or else we can say parameters
    return x*r#reture will return the value of the expression x*r
multiple=my_function(34,45)#here multiple is new variable and 34 and 45 are actual arguments
print(multiple)#Actual arguements are the values that are passed to the function when it is called
#And perform the operation and return the result
print("Example for Function with Greeting")
def greet():
    print("Hello, how are you?")#print a simple greeting message
    print("Welcome to python programming")
greet()#Function is the such kind of feature that can be used to repeat a block line without each time in the program    
print("Example for Function with Greeting and Name")
def greet(name):
    print(f"Hello ,{name} how are you")
greet("Adeep Reddy")    