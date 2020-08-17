from core.models import Naver
import datetime


class NaversFilters:

    def __init__(self, user, params):
        """
            Parameters
            ----------
            params : QuerySet
                     Description .
        """

        self.queryset = Naver.objects.filter(creator=user.id)
        self.name = params.get('name', None)
        self.job = params.get('job', None)
        self.user = user
        self.company_time_eq = params.get('company_time_equal', None)
        self.company_time_gt = params.get('company_time_more_than', None)
        self.company_time_lt = params.get('company_time_less_than', None)
        self.params = params

    def get_name(self):
        if self.name:
            self.queryset = self.queryset.filter(name__iexact=self.name)

    def get_job(self):
        if self.job:
            self.queryset = self.queryset.filter(
                job_role__name__iexact=self.job)

    def company_time_is_equal(self):
        if self.company_time_eq:
            self.queryset = Naver.company_time.equal(
                self.user, self.company_time_eq)

    def company_time_more_than(self):
        if self.company_time_gt:
            self.queryset = Naver.company_time.more_than(
                self.user, self.company_time_gt)

    def company_time_less_equal(self):
        if self.company_time_lt:
            self.queryset = Naver.company_time.less_than(
                self.user, self.company_time_lt)

    def process(self):
        self.get_name()
        self.get_job()
        self.company_time_is_equal()
        self.company_time_more_than()

    def get_objects(self):
        self.process()
        return self.queryset
