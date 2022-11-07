from fastapi import FastAPI

app = FastAPI()


@app.get('/años')
async def index():
    return {'esta': 'andando'}
