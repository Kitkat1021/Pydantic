def insert_patient_data(name: str, age: int): # One Solution is to use Type Hinting
    
    if type(name) == str and type(age) == int: # Solution 2 is to use Type Validation
        if age < 0:
            raise ValueError("Age cannot be negative.") # data validation
        else:
            print(name)
            print(age)
            print("Inserted into Database")
    else:
        print("Invalid data type. Please insert correct data types.")

# Here is a problem that there is no Type validation hypothesis
# , so we can insert any type of data into the database which is not good for us.
insert_patient_data('Mudit', 20)
