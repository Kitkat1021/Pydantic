def insert_patient_data(name, age):
    print(name)
    print(age)
    print("Inserted into Database")


# Here is a problem that there is no Type validation hypothesis
# , so we can insert any type of data into the database which is not good for us.
insert_patient_data('Mudit', 'twenty')
