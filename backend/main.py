from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.exception_handlers import http_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException



# Import Paths
from paths import (
    path_available,
    path_fish,
    path_bug
)



# Start the App
app = FastAPI()



# Add Middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



# 404 Redirect
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return RedirectResponse(url="/")
    return await http_exception_handler(request, exc)



# Add Paths
app.include_router(path_available.router)
app.include_router(path_fish.router)
app.include_router(path_bug.router)



# Run the App
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


