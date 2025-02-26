import fastapi
from fastapi import Request
import uvicorn
import os
app = fastapi.FastAPI()



@app.get('/')
async def root():
    return {"status": "ok"}

@app.post('/training')
async def training(request: Request):
    training_response = await request.json()
    training_id = training_response.get('id')
    status = training_response.get('status')
    model_name, trained_model_version  = training_response.get("output")['version'].split(":")


    print("training_id", training_id)
    print("status", status)
    print("model_name", model_name)
    print("trained_model_version", trained_model_version)

    
    return {"status": "ok"}

@app.post('/generate')
async def generate(request: Request, user_id):
    prediction_response = await request.json()
    training_id = prediction_response.get('id')
    status = prediction_response.get('status')
    image_url = prediction_response.get("output")[0]


    print("user_id", user_id)
    print("training_id", training_id)
    print("status", status)
    print("image_url", image_url)

    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
