

from pydantic import BaseModel, EmailStr, AnyUrl, Field, FieldValidator, ValidationError
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    # define ideal schema for the data
    name: str
    email: EmailStr # Do Email Validation
    age: int 
    weight: float 
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str] 

    # create new 

def insert_patient_data(patient: Patient): # create a function that takes an object of the patient class as an argument
            
    print(patient.name)
    print("Inserted into Database")


patient_info = {'name':'Mudit',
                'email': 'mudit@example.com',
                'LinkedIn': 'https://www.linkedin.com/in/mudit',
                'age': 26,
                'weight': '70.5', 
                'married': True,
                'allergies': ['Pollen', 'Dust'],
                'contact_details': {'email': 'mudit@example.com',
                                     'phone': '123-456-7890'}}

# created an object of the patient class and passed the patient_info dictionary  
patient1 = Patient(**patient_info) # ** is used to unpack the dictionary 

insert_patient_data(patient1) # pass the object to the function
