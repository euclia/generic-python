from ..entities.prediction_request import PredictionRequest
from ..entities.dataset import Dataset
from ..entities.dataentry import DataEntry
from ..helpers import model_decoder
import numpy as np
from typing import Dict, Any

# def decode(request):
#     json_request = json_decode(request.body)
#     pred_request = PredictionRequest(json_request['dataset'], json_request['rawModel'], json_request['additionalInfo'])
#     input_series = pred_request.additionalInfo['fromUser']['inputSeries']
#     independentFeatures = pred_request.additionalInfo['independentFeatures']
#     shorted = []
#     actualIndepFeatKeys = []
#     # pred_request.dataset.features['key']
#     for actual in input_series:
#         for key in independentFeatures:
#             if actual == independentFeatures[key]:
#                 for feature in pred_request.dataset['features']:
#                     if feature['name'] == actual:
#                         shorted.append(feature['key'])
#                 # shorted.append(key)
#     dataEntryAll = []
#     for dataEntry in pred_request.dataset['dataEntry']:
#         dataEntryToInsert = []
#         for key in shorted:
#             dataEntryToInsert.append(dataEntry['values'][key])
#         dataEntryAll.append(dataEntryToInsert)
#     return dataEntryAll


def decode(dataset, additionl_info):

    print("Dataset structure:")
    print(dataset)

    input_series = additionl_info['fromUser']['inputSeries']
    independentFeatures = additionl_info['independentFeatures']
    shorted = []
    actualIndepFeatKeys = []
    # pred_request.dataset.features['key']
    for actual in input_series:
        for key in independentFeatures:
            if actual == independentFeatures[key]:
                for feature in dataset['features']:
                    if feature['name'] == actual:
                        shorted.append(feature['key'])

    print("Shorted keys:", shorted)

    dataEntryAll = []
    dataEntry = dataset['dataEntry']
    print("DataEntry structure:", dataEntry)

    if isinstance(dataEntry, dict) and 'values' in dataEntry:
        values = dataEntry['values']
        dataEntryToInsert = []
        for key in shorted:
            print(f"Accessing key: {key}, type: {type(key)}")
            value = values.get(str(key))
            print(f"Retrieved value: {value}")
            if value is not None:
                dataEntryToInsert.append(value)
        dataEntryAll.append(dataEntryToInsert)
    else:
        print(f"Unexpected dataEntry structure: {dataEntry}")

    print(f"DataEntryAll: {dataEntryAll}")
    return dataEntryAll
