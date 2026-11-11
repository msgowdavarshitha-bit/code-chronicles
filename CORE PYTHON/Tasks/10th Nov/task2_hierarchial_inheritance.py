# Task 2: Hierarchical Inheritance – Person → Doctor / Patient 
# 
# Objective: Create multiple child classes that inherit from a single parent class.
# 
# Class Structure              Person           
#                             /      \         
#                           Doctor    Patient 
# 
# 1. Parent Class – Person 
# Attributes: ● name ● age 
# Method: ● display_info() – Display the person's basic information. 
# 
# 2. Child Class – Doctor 
# Attribute: ● specialization 
# Method: ● diagnose() – Display the doctor's specialization and diagnosis information. 
# 
# 3. Child Class – Patient 
# Attribute: ● disease 
# Method: ● treatment() – Display the patient's disease and treatment details. 
# 
# Task: 
# ● Create a Doctor object and access the properties and methods of the Person and Doctor classes. 
# ● Create a Patient object and access the properties and methods of the Person and Patient classes.                                                                                                                              
# ● Display the complete information of both objects. 
# 
# 
# Concept: Hierarchical Inheritance 


class Person:
    def display_info(self,name,age):
        self.name=name
        self.age=age
        print("Name of the person: ",name)
        print("AGe of the person: ",age)

class  Doctor(Person):
    def diagnose(self,specialization):
        self.specialization=specialization
        print("doctor's specialization: ",specialization)

class Patient(Person):
    def treatment(self,disease):
        self.disease=disease
        print("Name of the disease the patient is suffering from: ",disease)
        print("The treatment is as provided in the prescription")



name=input("Enter the name of the person: ")
age=int(input("Enter the age of the person: "))
specialization=input("Enter the doctor's specialization: ")
disease=input("Enter the disease of the patient: ")

print("1")
#  Create a Doctor object and access the properties and methods of the Person and Doctor classes. 
Doctor=Doctor()
Doctor.display_info(name,age)
Doctor.diagnose(specialization)


print("2")
# Create a Patient object and access the properties and methods of the Person and Patient classes
Patient=Patient()
Patient.display_info(name,age)
Patient.treatment(disease)


print("3")
# Display the complete information of both objects.
Doctor.diagnose(specialization)
Patient.treatment(disease)

