from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.security import OAuth2PasswordRequestForm
from app.api.analyze import router as analyze_router
from app.auth.jwt import create_access_token, get_current_user
from app.core.config import demo_users_db, ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI(title="Market_Trade API")


app.include_router(analyze_router)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = demo_users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=None
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.exception_handler(HTTPException)
def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"detail": exc.errors()}) 