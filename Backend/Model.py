from pydantic import BaseModel,EmailStr

class Details(BaseModel):
 rollno:int
 Name:str
 Department:str
 Year:str
 Email:EmailStr
 Skill:str

class Gkills(BaseModel):
 rollno:int
 Skill:str
