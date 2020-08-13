# my classes to comparison and router filters
from core.models import Naver
from core.api.query_string.FilterStrategy import FilterStrategy

class CoreFilters:
    
    def __init__(self, params, cls):
        cls_instance = FilterStrategy().compare(cls)       
        print(cls_instance)
