import sys
from pandas import DataFrame
from sensor.exception import SensorException
from sensor.logger import logging

#class to map categorical target colum to 0s and 1s instead of label encoding
class TargetValueMapping:
    def __init__(self):
        self.neg: int = 0
        self.pos: int = 1
    
    def to_dict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))
    