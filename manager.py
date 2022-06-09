import pandas as pd
import numpy as np

class manager:
    
    def __init__(self):
        self._featureToEncode = []
        
    def appendFeatureToEncode(self, feature):
        self._featureToEncode.append(feature)
        
    def getFeatureToEncode(self):
        return self._featureToEncode
        