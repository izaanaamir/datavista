import uvicorn
from core.router.data_fetchers import space_exploration
from fastapi import FastAPI

app = FastAPI()
app.include_router(space_exploration.router)


@app.get("/")
async def root():
    return {"message": "Hello World. First Commit with FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
