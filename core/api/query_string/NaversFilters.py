from core.models import Naver


class NaversFilters:

    def __init__(self, params):
        self.queryset = Naver.objects
        self.name = params.get('name', None)
        self.n_params = 0

    def get_name(self):
        if self.name:
            self.queryset = self.queryset.filter(name__iexact=self.name)
            self.n_params += 1

    def process(self):
        self.get_name()

    def get_objects(self):
        self.process()

        if self.n_params > 0:
            return self.queryset
        else:
            return self.queryset.all()
