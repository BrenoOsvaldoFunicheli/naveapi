# navedex API

## Backend Challenge to provide the API implementation with Django

A complete implementation of RESTful API to store and consume some structures that it contains, such as users, navers, jobs of navers, projects and tecnologies of projects, which were created using django 3 and django rest_framework.

## Sections

* :scroll: [Patterns](#scroll-patterns) (optional)
* :blue_book: [Requirements and Model](#blue_book-requirements-and-model)
* :wrench: [Building App](#wrench-building-app)
* :key: [Authentication](#key-authentication)
* :ticket: [API Consuming](#ticket-api-consuming)
* :postbox: [Testing](#postbox-testing)

## :scroll: Patterns

In order to create the real stage API to consuming I follow some best pratice and concepts of RESTful APIs must has, beside this, I provide the detailed documentation about API with the postman to test endpoints.

### Implemented concepts

* Versioning: All endpoints contains as prefix /api/v1/ that show the version api is first. So when I change some detail or implementation of API I Don't broken any implementation on my API in other application.

* Pagination: As many people can consuming the endpoints I need provide some throughput data. to first version we apply the limit with 5 registries.

* Authentication: I make the API visualization with the JWT tokens to Authentication on each endpoints

## :blue_book: Requirements and Model

The system consists of a creator of navedex's API, where you can register using email and password, and then when logging in you will have access to your browsers' database, with information such as: names, birth data, loads, company time and projects who participated.

### Requirements

* Authentication: The user registry himself with the password and email and can be get the token to access any endpoint to create and delete his registry by request.

* User tracked: In order to provide some security and isolation of registry all user only have access to own registry with exception of the dad tables, such as tecnologies and jobs.

* Navers Endpoint
    - Create: create new navers
    - List: return all values
    - Retrive: return the specific
    - Update: alter navers
    - Delete: delete the registry
    - filters: Some user can filter search by naver name, company time or job
    - observation: all registry of this model only can accessed by his own owner and this data need authentication.

* Projects Endpoint
    - Create: create new projects
    - List: return all values
    - Retrive: return the specific
    - Update: alter project by JSON information
    - Delete: delete the registry
    - filters: Some user can filter search by project name
    - observation: all registry of this model only can accessed by his own owner and this data need authentication.

### Model

In order to attendant the previous requirements, I make model to store data.

![alt text](https://github.com/BrenoOsvaldoFunicheli/naveapi/blob/conversion/documentation/DER.png?raw=true)

## :wrench: Building App

### Docker Build

This API was construct with the docker implementation, so you can run without others dependecies and scale after make your implementations, so you need make docker and docker compose in your machine.

#### Docker installation

To install docker follow the instructions in the links below depending on your operating system:

* CentOS: https://docs.docker.com/install/linux/docker-ce/centos/
* Debian: https://docs.docker.com/install/linux/docker-ce/debian/
* Fedora: https://docs.docker.com/install/linux/docker-ce/fedora/
* Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/
* MacOS: https://docs.docker.com/docker-for-mac/install/
* Windows: https://docs.docker.com/docker-for-windows/install/

#### Steps to Set Up

For API build you need some simple steps, download the this repository with the follow command:

``` linux

git clone https://github.com/BrenoOsvaldoFunicheli/naveapi.git

```

before the next step you need create the docker-volume to store the database data.

``` linux

docker volume create nave-pgdata

```

Next, you need setting the app and database containers with the follow command on the folder downloaded, that make(download all dependencies of the project), building(when you don't have container in your machine it downloaded it) and setting containers with docker compose.

``` linux

docker-compose build

docker-compose up

```

After this you need create database on container, because django can't create automatic, the database container is running the postgres. so you need create the database with the name nave.

* Docker attach

``` linux

docker exec -it [container-name] /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"

```

* Postgres create

``` sql

CREATE DATABASE nave;

```

Finally, you can't press CTRL+C to exit database and set it up again with the docker-compose up, with this you'll have the API running.

## :key: Authentication

As the API was implemented with JWT tokens all access on the endpoints are do with the jwt tokens, so you need apply the request and set in the authorization.

### Token duration

So when you access token through the url [uri]/api/v1/[resource] you can get two values on the payload response, first is the access token, with it, you can access the endpoint for 5 minutes, after you need used the refresh endpoint that gives the token to access for 24 hours.  

## :ticket: API Consuming

The API consuming were detailed on the postman collection, that implements all steps to consuming and explain some steps to use. The ordering of steps need to be follow, because you need authentication before consuming. The collection link is https://documenter.getpostman.com/view/8382418/T1LQfk9N

## :postbox: Testing
