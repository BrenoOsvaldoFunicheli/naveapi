# my classes to comparison and router filters
from core.models import *
from core.api.query_string import NaversFilters 

class FilterStrategy:
    
    def __init__(self):
        self.conditions = {
            Naver: NaversFilters
        }
        
    def compare(self, cls):
        
        value =  self.conditions.get(cls, None)
        print(value(''))