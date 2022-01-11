from fastapi import FastAPI, APIRouter
from finance import finance
from marketing import marketing
from hr import hr


server = FastAPI()

@server.on_event('startup')
async def startup():
    finance_router = APIRouter(prefix='/finance', tags=['finance'])
    hr_router = APIRouter(prefix='/hr', tags=['hr'])
    marketing_router = APIRouter(prefix='/marketing', tags=['marketing'])
    
    await finance.setup(finance_router)
    await hr.setup(hr_router)
    await marketing.setup(marketing_router)

    server.include_router(finance_router)
    server.include_router(hr_router)
    server.include_router(marketing_router)
