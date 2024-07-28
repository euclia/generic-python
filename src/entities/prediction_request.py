from typing import Optional, List
from pydantic import BaseModel
from .dataset import Dataset


class PredictionRequest(BaseModel):

    dataset: Optional[Dataset]
    rawModel: Optional[list]
    additionalInfo: Optional[dict]
    doaMatrix: Optional[List[list]]
