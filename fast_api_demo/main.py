from fastapi import FastAPI
from typing import Optional, List, Generic
from model import User, Role, Gender

app = FastAPI()

db : List[User] = [
User(id = 1 ,first_name=" Umesh",last_name = "singh",gender = Gender.male, roles = [Role.admin, Role.user]),
User(id =2,
     first_name=" Sandeep",
     last_name="Patil",
     gender=Gender.male,
roles = [Role.student, Role.user])]
@app.get('/')
def root () :
    return ({"hell":"wordl"})

@app.get('/api/get_user')
def get_user() :
    return (db)


