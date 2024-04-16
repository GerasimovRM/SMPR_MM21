import uvicorn


if __name__ == "__main__":
    uvicorn.run("api.server:app", port=5500, reload=True)
