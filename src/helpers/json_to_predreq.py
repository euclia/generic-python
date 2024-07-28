from ..entities.prediction_request import PredictionRequest
from ..entities.dataset import Dataset
from ..entities.dataentry import DataEntry
from ..helpers import model_decoder
import numpy as np
from typing import Dict, Any

def decode(dataset, additionalInfo):
    print("Dataset structure:")
    print(dataset)

    input_series = additionalInfo['fromUser']['inputSeries']
    independentFeatures = additionalInfo['independentFeatures']
    shorted = []

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
