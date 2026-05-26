# We will be using the same example but deep diving into more features

from pydantic import BaseModel # always import these two
from typing import List, Dict

class Patient(BaseModel): # create a class that inherits from BaseModel
    # define ideal schema for the data
    name: str # Do Type Validation
    age: int
    weight: float
    married: bool
    allergies: List[str] # List of strings
    contact_details: Dict[str, str] # Dictionary with string keys and string values


def insert_patient_data(patient: Patient): # create a function that takes an object of the patient class as an argument
            
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted into Database")


patient_info = {'name':'Mudit',
                'age': 26,
                'weight': 70.5,
                'married': True,
                'allergies': ['Pollen', 'Dust'],
                'contact_details': {'email': 'mudit@example.com',
                                     'phone': '123-456-7890'}}

# created an object of the patient class and passed the patient_info dictionary  
patient1 = Patient(**patient_info) # ** is used to unpack the dictionary 

insert_patient_data(patient1) # pass the object to the function
