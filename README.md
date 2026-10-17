# Patient Schema Validation with Pydantic

A lightweight Python script demonstrating how to enforce type safety and parse dictionary data into a structured object using **Pydantic V2**.

## 🚀 Features
* **Automatic Validation**: Guarantees raw input maps accurately to strict data types (`str`, `int`, `float`).
* **Clean Data Access**: Demonstrates object-attribute dot notation (`patient.name`) instead of dictionary key lookups.

## 📦 Installation
Ensure you have Python installed, then install Pydantic:
```bash
pip install pydantic
```

## 💻 Script Implementation
Save the following code in a file named `main.py`:

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    weight: float

def show_patient(patient: Patient):
    print("patient name:", patient.name)
    print("patient age:", patient.age)
    print("patient gender:", patient.gender)
    print("patient weight:", patient.weight)

patient_data = {"name": "john", "age": 20, "gender": "Male", "weight": 65.5}
patient1 = Patient(**patient_data)

show_patient(patient1)
```

## 🎯 Expected Output
Run the script using your terminal:
```bash
python main.py
```

Output:
```text
patient name: john
patient age: 20
patient gender: Male
patient weight: 65.5
```
