from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web
from tornado.escape import json_decode, json_encode
from ..entities.prediction_request import PredictionRequest
from ..entities.dataset import Dataset
from ..entities.dataentry import DataEntry
from ..helpers import model_decoder, json_to_predreq, doa_calc

import numpy as np


class SvmModelHandler(tornado.web.RequestHandler):
    # @tornado.asynchronous
    # @gen.engine
    def post(self):
        # print(self.request.body)
        json_request = json_decode(self.request.body)
        pred_request = PredictionRequest(json_request['dataset'], json_request['rawModel'], json_request['additionalInfo'])
        predFeatures = pred_request.additionalInfo['predictedFeatures']
        rawModel = pred_request.rawModel[0]
        model = model_decoder.decode(rawModel)
        dataEntryAll = json_to_predreq.decode(self.request)
        doaM = []
        try:
            doaM = json_request['doaMatrix']
        except KeyError:
            pass
        a = None
        if type(doaM).__name__ != 'NoneType' and len(doaM) > 0:
            doaMnp = np.asarray(doaM)
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
        self.set_header("Content-Type", "application/json")
        self.write(json_encode(finalAll))
