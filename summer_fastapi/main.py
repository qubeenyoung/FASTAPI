from typing import Union

from fastapi import Body, FastAPI

from typing import Annotated

from enum import Enum

from datetime import datetime

MessageList=[]

app = FastAPI()

@app.get("/messages")
async def message_list():
    return MessageList 
        

@app.get("/send_message/{user}/{message}")
async def message_send(
    user:str, 
    message:str,
    time: Annotated[datetime | None, Body()] = None
    ) :
    time = datetime.now()
    Message = {"at" : time, "user" : user, "message" : message}
    MessageList.append(Message)

    return Message

