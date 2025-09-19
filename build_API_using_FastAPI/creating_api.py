from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    org: str

@app.get('/')
def read_root():
    return {'message': 'this is root url'}

@app.get('/user')
def get_user(user_id: int):
    return {'user': User(id=user_id, name='Aman', org='OpenAI')}