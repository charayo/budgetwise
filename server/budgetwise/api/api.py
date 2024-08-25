from typing import Any, List

from fastapi import FastAPI, HTTPException, Security, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

# import json
# from sqlalchemy.orm import Session

from server.budgetwise.app import types
import server.budgetwise.app.app as myapp

# import sentry_sdk
# from .utils import server_error


not_implemented = HTTPException(status_code=500, detail="Not Implemented")

app = FastAPI()

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path="/")
def get_root():
    # chr_tool.main()
    return "Welcome to Budgetwise API"


# Router with authentication enabled
# NOTE: can add role-based permissions here in the future
router = APIRouter(prefix="/budgetwise/v1")


@router.post(path="/analyze")
def ask_question(request: types.ChatRequestModel,):
    ask_ai = myapp.BudgetWiseLLM()
    response = ask_ai.generate_response(request.question) 
    return {"response": response}




app.include_router(router)
