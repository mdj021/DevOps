from typing import Union

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/Home")
def read_root():
    return {"Hello": "World"}

@app.get("/About")
def about():
    return{"msg":"About us"}

@app.get("Contact-Us")
def contact_us():
    return {"email":"abc@gmail.com","mob_no":"1234567890"}

@app.get("/login")
def login(username : str,password : str):
    if username == "aman" and password == "abc12345":
        return{"Data":"Login This is a login page"}
    else: 
        return{"Data":"Login failed incorrect username or password incorrect"}
    
@app.post("/login")
def login_post(request:Request):
    print(request.headers)
    print(request.body)