import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.entities.prediction_request import PredictionRequest

from src.handlers.sklearn import SKLearnHandler as sklearnHandler
from typing import Dict, Any

app = FastAPI(title="Generic Python API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/predict/sklearn/")
# def sklearn_model(req: PredictionRequest):
def sklearn_model(req: Dict[Any, Any] = None):
    try:
        doa_matrix = req['doaMatrix']
    except KeyError:
        doa_matrix = None
    # print(req['doaMatrix'])
    try:
        resp = sklearnHandler(req['dataset'], req['rawModel'], req['additionalInfo'], doa_matrix)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    else:
        return resp


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8002)
