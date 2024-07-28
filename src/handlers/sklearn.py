from ..helpers import model_decoder, doa_calc, json_to_predreq
import numpy as np
from ..entities.dataset import Dataset


def SKLearnHandler(dataset: Dataset, rawModel: list, additionalInfo: dict, doaMatrix: list = None):

    predFeatures = additionalInfo['predictedFeatures']
    rawModel = rawModel[0]
    print('hello before')
    model = model_decoder.decode(rawModel)
    print('hello after')
    dataEntryAll = json_to_predreq.decode(dataset, additionalInfo)
    a = None
    if doaMatrix and len(doaMatrix) > 0:
        doaMnp = np.asarray(doaMatrix)
        a = doa_calc.calc_doa(doaMnp, dataEntryAll)

    predictions = model.predict(dataEntryAll)

    preds = []
    j = 0
    for i in list(predFeatures.values()):
        for pred in predictions:
            if np.issubdtype(type(predictions[j]), int):
                fPred = {i: int(predictions[j])}
                if a is not None:
                    for key, value in a[j].items():
                        fPred[key] = value
                preds.append(fPred)
            if np.issubdtype(type(predictions[j]), float):
                fPred = {i: float(predictions[j])}
                if a is not None:
                    for key, value in a[j].items():
                        fPred[key] = value
                preds.append(fPred)
            if np.issubdtype(type(predictions[j]), str):
                fPred = {i: predictions[j]}
                if a is not None:
                    for key, value in a[j].items():
                        fPred[key] = value
                preds.append(fPred)
            j += 1
    finalAll = {"predictions": preds}
    return finalAll
