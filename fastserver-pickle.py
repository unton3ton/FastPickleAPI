from fastapi import FastAPI, File, UploadFile
import pickle

app = FastAPI()

@app.post('/forecast')
async def forecast(input_file: UploadFile = File(...)):
    contents = await input_file.read()  # Read the contents of the uploaded file
    data = pickle.loads(contents)  # Unpickle the data
    print(data)
    return {'data': len(data)}

# uvicorn fastserver-pickle:app --host 0.0.0.0 --port 8000 --reload