from fastapi import FastAPI, Depends

app = FastAPI(
    debug=True,
    title='Kot',
)


def get_db():
    return "Database TEST!"



@app.get("/")
async def root(
        get_db = Depends(get_db),
):
    return {"message": get_db}