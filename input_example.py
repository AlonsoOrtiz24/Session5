name = input("What is your name?")
print("Hello", name)
age = input("How old are you? ")
try:
    age = int(age) #i am trying to convert it to number
    #new_age = age / 0
except ValueError:
    print("you are trying to trick me")
except ValueError:
    print("you are trying to trick me")
    print("better time last time")
except ZeroDivisionError:
    print("you can't divide by zero")
else: #this happens if no error occurred
    print("you were probably in", 2024 - age)
finally:
    print("thanks for playing")