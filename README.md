# navedex API

## Backend Challenge to provide the API implementation with Django

A complete implementation of RESTful API to store and consume some structures that it contains, such as users, navers, jobs of navers, projects and tecnologies of projects, which were created using django 3 and django rest_framework.

## Sections

* :snake: [Patterns](#patterns-used) (optional)
* :blue_book: [Requirements and Model](#blue_book-creating-a-project)
* :page_with_curl: [Building App](#page_with_curl-creating-an-app)
* :page_with_curl: [Registry on API](#tv-creating-a-view)
* :art: [Authentication](#art-creating-a-template)
* :ticket: [API Consuming](#ticket-creating-a-model)
* :postbox: [Testing](#postbox-creating-model-objects-and-queries)

## :snake: [Patterns](optional)

In order to create the real stage API to consuming I follow some best pratice and concepts of RESTful APIs must has, beside this, I provide the detailed documentation about API with the postman to test endpoints.

### Implemented concepts

* Versioning: All endpoints contains as prefix /api/v1/ that show the version api is first. So when I change some detail or implementation of API I Don't broken any implementation on my API in other application.

* Pagination: As many people can consuming the endpoints I need provide some throughput data. to first version we apply the limit with 5 registries.

* Authentication: I make the API visualization with the JWT tokens to Authentication on each endpoints

## :blue_book: [Requirements and Model](#blue_book-creating-a-project)

The system consists of a creator of navedex's API, where you can register using email and password, and then when logging in you will have access to your browsers' database, with information such as: names, birth data, loads, company time and projects who participated.

### Requirements

* Authentication: The user registry himself with the password and email and can be get the token to access any endpoint to create and delete his registry.

* User tracked: In order to provide some security and isolation of registry all user only have access to own registry with exception of the dad tables, such as tecnologies and jobs.

* Navers Endpoint
    * Create: create new navers
    * List: return all values
    * Retrive: return the specific
    * Update: alter navers
    * Delete: delete the registry
    * filters: Some user can filter search by naver name, company time or job
    * observation: all registry of this model only can accessed by his own owner and this data need authentication.

* Projects Endpoint
    * Create: create new projects
    * List: return all values
    * Retrive: return the specific
    * Update: alter project by JSON information
    * Delete: delete the registry
    * filters: Some user can filter search by project name
    * observation: all registry of this model only can accessed by his own owner and this data need authentication.
