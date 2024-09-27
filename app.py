from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from logic import handle_negotiation

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class OfferRequest(BaseModel):
    user_price: float
    user_message: str

@app.post("/negotiate/")
async def negotiate(request: OfferRequest):
    try:
        response = handle_negotiation(request.user_price, request.user_message)
        return {"bot_response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/")
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
