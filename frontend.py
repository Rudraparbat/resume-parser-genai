from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse

routers = APIRouter(
    prefix="/resume-parser",
    tags=["frontend"]
)

templates = Jinja2Templates(directory="templates")

@routers.get("/" , response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request , name = "index.html")