from pydantic import BaseModel

class Patient(BaseModel):

    name:str
    age:int
    gender:str

    weight:float


def show_patient(patient:Patient):
    print("patient name",patient.name)
    print("patient age",patient.age)
    print("patient gender",patient.gender)
    print("patient weight",patient.weight)





patient_data = {"name":"john","age":20,"gender":"Male","weight":65.5}
patient1 = Patient(**patient_data)


show_patient(patient1)

