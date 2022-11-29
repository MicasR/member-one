from pydantic import BaseModel

class Status404(BaseModel):
    detail:str = "Not found"

responses = {
    404: {"description": "Not found", "model":Status404}
}
