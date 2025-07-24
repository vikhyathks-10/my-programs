age_input = input("Enter your age: ") 
try:
    age = float(age_input)  
    if age >= 18:  
        print("You are eligible to vote.")
    else:
        print("Wait until you are 18 years old to vote.")
        
except:
    print("Please enter a number .")  
