from DataBase import injection
import Table
import Model
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
router=APIRouter()
@router.post("/StudentsDetails")
def details(content:Model.Details,db:Session=Depends(injection)):
 db.add(Table.Table(**content.model_dump()))
 db.commit()
 return"Added success"
@router.post("/Skills")
def skill(content:Model.Gkills,db:Session=Depends(injection)):
 db.add(Table.Skill(**content.model_dump()))
 db.commit()
 return"Added SuccessFully"
@router.get("/Skillstudentinfo")
def ssinfo(db:Session=Depends(injection)):
 emp=db.query(Table.Skill).all()
 return emp
@router.get("/Allstudentinfo")
def sinfo(db:Session=Depends(injection)):
 emp=db.query(Table.Table).all()
 return emp
@router.get("/Skillstudentinfo/{ques}")
def ssinfo(ques:str,db:Session=Depends(injection)):
 emp=db.query(Table.Skill).filter(Table.Skill.Skill.ilike(ques)).all()
 return emp
@router.get("/parstudentinfo/{id}")
def sinfo(id:int,db:Session=Depends(injection)):
 emp=db.query(Table.Table).filter(Table.Table.rollno==id).first()
 return emp
@router.put("/Update/{id}")
def update(id:int,content:Model.Details,db:Session=Depends(injection)):
  emp=db.query(Table.Table).filter(Table.Table.rollno==id).first()
  if emp:
   emp.rollno=content.rollno
   emp.Name=content.Name
   emp.Department=content.Department
   emp.Year=content.Year
   emp.Email=content.Email
   emp.Skill=content.Skill
   db.commit()
   return"Status Updated"
  else:
   return"Problem in entered Id"
  
@router.put("/UpdateSkill/{id}")
def updatee(id:int,content:Model.Gkills,db:Session=Depends(injection)):
  emp=db.query(Table.Skill).filter(Table.Skill.rollno==id).first()
  if emp:
   emp.rollno=content.rollno
   emp.Skill=content.Skill
   db.commit()
   return"Updated"
  else:
   return"Problem in entered Id"
  
@router.delete("/DeleteStudentsinfo/{id}")
def inbo(id:int,db:Session=Depends(injection)):
 emp=db.query(Table.Table).filter(Table.Table.rollno==id).first()
 skill=db.query(Table.Skill).filter(Table.Skill.rollno==id).first()
 if emp and skill:
  db.delete(emp)
  db.delete(skill)
  db.commit()
  return"Deleted"
 else:
  return"Problem in entered Id"
 

  
