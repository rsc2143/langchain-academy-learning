from typing import TypedDict
from pydantic import BaseModel, Field, ValidationError

# TypedDict way (just type checking)
class UserDict(TypedDict):
    name: str
    age: int
    email: str

# Pydantic way (validation + type checking)
class UserModel(BaseModel):
    name: str
    age: int = Field(gt=0, lt=150)  # age must be between 0 and 150
    email: str

# TypedDict example (no validation at runtime)
user_dict: UserDict = {
    "name": "John",
    "age": -5,  # Invalid age but TypedDict won't catch this
    "email": "not_an_email"  # Invalid email but TypedDict won't catch this
}

# Pydantic example (validates at runtime)
try:
    user_model = UserModel(
        name="John",
        age=-5,  # This will raise a ValidationError
        email="not_an_email"  # You could add email validation too
    )
except ValidationError as e:
    print("Validation errors:")
    print(e)
