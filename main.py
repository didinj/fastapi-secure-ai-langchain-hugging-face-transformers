# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from auth import authenticate_user, create_access_token, get_current_user
from models.schemas import Token, User
from langchain_app import generate_response

app = FastAPI()

# Enable CORS for local frontend (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Secure AI App!"}

@app.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/prompt")
async def ai_prompt(prompt: str, current_user: User = Depends(get_current_user)):
    response = generate_response(prompt)
    return {"user": current_user.username, "response": response}

