from fastapi import FastAPI

app=FastAPI()


#minimal app - get request
@app.get("/",tags=['ROOT'])
async def root()->dict:
    return {"ping":'pong'}

# get -->read Todo
@app.get("/todo",tags=['todos'])
async def get_todo()->dict:
    return {"data":todos}


# post -->create Todo


@app.post("/todo",tags=['todos'])
async def create_todo(todo: dict)->dict:
    todos.append(todo)
    return {"data":"the data has been added"}
# put -->update Todo

@app.put("/todo/{id}",tags=["todos"])
async def update_todo(id: int,body: dict)->dict:
    for item in todos:
        if int((item['id']))==id:
            item['Activity'] = body['Activity']
            return {
                "data":f"Todo with {id} has been updated"
            }
    return {
        "data":f"Todo with is id number {id} has not flound!"
    }
# delete -->delete Todo

@app.delete("/todo/{id}",tags=["todos"])
async def delete_todo(id: int)->dict:
    for item in todos:
        if int((item['id']))==id:
            todos.remove(item)
            return {
                "data":f"Todo with {id} has been deleted"
            }
    return {
        "data":f"Todo with is id number {id} has not flound!"
    }












todos=[
    {'id':'1',
    "Activity": "Jogging for 2 Hours at 7:00 AM."
    },
    {
        "id":'2',
        "Activity":"Writing 3 pages of my new book at 2:00 PM"
    }
]