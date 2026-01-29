from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


app = FastAPI(title="Orion-IA")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

from routes.auth_routes import auth_roter

app.include_router(auth_roter)