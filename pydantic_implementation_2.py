from pydantic import BaseModel # always import these two

class Patient(BaseModel): # create a class that inherits from BaseModel
    # define ideal schema for the data
    name: str # Do Type Validation
    age: int

def insert_patient_data(patient: Patient): # create a function that takes an object of the patient class as an argument
            
    print(patient.name)
    print(patient.age)
    print("Inserted into Database")


patient_info = {'name':'Mudit',
                'age': 26}

# created an object of the patient class and passed the patient_info dictionary  
patient1 = Patient(**patient_info) # ** is used to unpack the dictionary 

insert_patient_data(patient1) # pass the object to the function
