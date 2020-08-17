# django imports
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

#   rest framework imports
from rest_framework.test import APIClient
from rest_framework.test import RequestsClient

# my imports
from .models import Technologie, JobRole, Project, Naver
import json 

# Create your tests here.


class ModelCreateTestCase(TestCase):

    def setUp(self):
        """
        Description
        -----------

            The first step to test is populate step, 
            where we create some objects to see if value was correct
            when you don't get correct values many parts of the software fail

            First we create tecnologies and 
        """
        #   fake user to test the other components
        u = User.objects.create(username="django",email="django@django.com", password="django")

        t = Technologie.objects.create(
            name="Python", description="Django RestFramework")

        j = JobRole.objects.create(
            name="API developer", description="Some description that I put here"
        )

        n = Naver.objects.create(
            name="Breno ", admission_date="2020-05-08", end_date=None, birthdate="2020-05-08", job_role=j
        )

        p = Project.objects.create(
            name="Api building", description="Some description", start_date="2020-05-08", end_date="2020-05-28", status="A")

        #   Foreing key setting
        p.tecnologies.add(t)
        p.creator = u
        p.save()

        #   Foreing key setting
        n.projects.add(p)
        n.creator = u
        n.save()

    def test_job(self):
        self.assertTrue(JobRole.objects.exists())

    def test_technologies(self):
        self.assertTrue(Technologie.objects.exists())

    def test_project_create(self):
        """
        Description
        -----------
            In this test we see if the values was correctly created, 
            the value is need True to validate.
        """
        self.assertTrue(Project.objects.exists())

    def test_navers(self):
        """
        Description
        -----------
            In this test we see if the values was correctly created, 
            after create and populate one record and setting

        """
        self.assertTrue(Naver.objects.exists())


class LoginAPITestCase(TestCase):

    """
    Description
    -----------
        This test verify if login by API do your senteces and proposes
        , beside this it checkes if doesn't has some error

    """
    def setUp(self):
        #   fake user to test the other components
        u = User.objects.create(username="django",email="django@django.com", password="django")

    def test_login_(self):
        u = User.objects.all()

        print(u)
        client = Client()
        response = client.post(
            reverse('token_obtain_pair'),
            data=json.dumps({"username": "django", "password": "django"}),
            content_type='application/json'
        )
        
        print(response)


