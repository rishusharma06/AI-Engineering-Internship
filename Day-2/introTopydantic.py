from pydantic import BaseModel
# Pydantic checks that API data has the right structure and types.

class Expense(BaseModel):
    amount : float
    category : str
    description : str

# works well
e = Expense(amount = 1000, category = "shopping", description = "shoes")

# throws error 
e = Expense(amount = "one thousand", category = "shopping", description = "shoes")


