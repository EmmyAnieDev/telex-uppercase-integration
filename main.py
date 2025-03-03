from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.integration import router as integration_router
from routes.message_format import router as format_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(integration_router)
app.include_router(format_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)