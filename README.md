Simple application to manage your stretching routine. 

Motivation is to build an CRUD API with FastAPI, SQLAlchemy, Postgres, and Docker.


###### Motivation

Develop a simple CRUD API using modern Python tools such as FastAPI/Pydantic, SQLAlchemy, Postgres, and Docker.

###### Structure
**src/models**
Contains data models for ORM mapping.

**src/repositories**
Contains access patterns for CRUD operations on the database.

**src/routes**
Contains routes, linking FastAPI's router to the `schemas` layer and the `services` layer.

**src/schemas**
Contains validation models using Pydantic to validate incoming API requests.

**sr/services**
Wraps repository functions for API usage. Some API calls may use multiple repositories.
