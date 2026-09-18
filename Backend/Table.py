from DataBase import Base
from sqlalchemy import Column,INTEGER,VARCHAR,ForeignKey
class Table(Base):
  __tablename__="Students_info"
  rollno=Column(INTEGER,primary_key=True)
  Name=Column(VARCHAR(50))
  Department=Column(VARCHAR(50))
  Year=Column(INTEGER)
  Email=Column(VARCHAR(50))
  Skill=Column(VARCHAR(60))


class Skill(Base):
  __tablename__="Skill_Sets"
  rollno=Column(INTEGER, ForeignKey("Students_info.rollno"),primary_key=True)
  Skill=Column(VARCHAR(50))
