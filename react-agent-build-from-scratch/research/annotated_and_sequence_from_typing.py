from typing import Annotated

# Without Annotated
age: int  # Just says "this is a number"

# With Annotated
Age = Annotated[int, "Must be between 0 and 150"]  # Says "this is a number AND here's a note about it"
user_age: Age = 25

# Real-world example with multiple annotations
from pydantic import BaseModel

class User(BaseModel):
    # This says: it's a string AND must be > 3 chars AND must be an email
    email: Annotated[str, "Min length 3", "Must be valid email"]
    
from typing import Sequence

# Instead of being specific like this:
def process_list(numbers: list[int]) -> int:
    return sum(numbers)
# This only accepts lists: process_list([1, 2, 3]) -> 6
# This rejects sequences like tuples: process_list((1, 2, 3)) -> TypeError

# With Sequence:
def process_sequence(numbers: Sequence[int]) -> int:
    return sum(numbers)
# This accepts lists, tuples, and other sequences: process_sequence([1, 2, 3]) -> 6
# This rejects other iterables like sets: process_sequence({1, 2, 3}) -> TypeError

process_sequence([1, 2, 3])
process_sequence((1, 2, 3))
process_sequence({1, 2, 3})