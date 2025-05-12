# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List  # for type hinting

# app = FastAPI()

# # Place model with an additional id field
# class Place(BaseModel):
#     id: int              # Add ID for identification
#     placename: str
#     distance: int
#     location: str
#     rating: float
#     description: str
#     is_favorite: bool

# # In-memory list to store Place objects
# places: List[Place] = []

# @app.get("/")
# def get_object():
#     return {"message": "Welcome to Nishan FastAPI app"}

# @app.get("/pk")
# def get_read_object():
#     return places  # returns the list of all places

# @app.post("/pk")
# def add_object(all_data: Place):
#     places.append(all_data)
#     return all_data  # returns the posted Place object

# @app.put("/pk/{item_id}")
# def update_object(item_id: int, updated_object: Place):
#     for index, all_data in enumerate(places):
#         if all_data.id == item_id:
#             places[index] = updated_object  # update the object
#             return updated_object
#     return {"error": "Place not found"}

# @app.delete("/pk/{item_id}")
# def delete_object(item_id: int):
#     for index, all_data in enumerate(places):
#         if all_data.id == item_id:
#             deleted = places.pop(index)  # remove and return the object
#             return deleted
#     return {"error": "Place not found"}



from fastapi import FastAPI
from pydantic import BaseModel
#base model is used to valid automatically data validation 
from typing import List
app = FastAPI()
class Place(BaseModel):
    id:int
    placename:str
    distance:int
    location:str
    rating:float
    description:str
    is_favorite:bool

places:List[Place] = []
@app.get("/")
def get_object():
    return {"message":"welcome to nishan fastapi app"}

@app.get("/pk")
def get_read_object():
    return places
@app.post("/pk")
def add_object(all_data: Place):
    places.append(all_data)
    return all_data

@app.put("/pk/{item_id}")
def update_object(item_id: int, updated_object: Place):
    for index, place in enumerate(places):
        # enumerate gives both object and  index
        if place.id == item_id:
            updated_object.id = item_id  # Force the correct ID
            places[index] = updated_object
            return {"message": "Place updated", "place": updated_object}
    return {"error": "Place not found"}



@app.delete("/pk/{item_id}")
def delete_object(item_id:int):
    for index,place in enumerate(places):
        if place.id == item_id:
            deleted= places.pop(index)
            return deleted
    return {"error":"place is not found"}