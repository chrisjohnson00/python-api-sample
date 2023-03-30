# python-api-sample
A sample Python API in Flask

## PyPi Dependency updates

    docker run -it --rm -v ${PWD}:/repo -w /repo python:3.11.2-slim bash
    pip install --upgrade pip
    pip install --upgrade Flask gunicorn
    pip freeze > requirements.txt

## PyPi Dependencies for Deploy (Pulumi Only)

    docker run -it --rm -v ${PWD}:/repo -w /repo python:3.11.2-slim bash
    pip install --upgrade pip
    pip install --upgrade "pulumi>=3.0.0,<4.0.0" "pulumi-azure-native>=1.0.0,<2.0.0"
    pip freeze > pulumi_requirements.txt

## API Endpoints

  - `/api/v1/users` - Returns a list of users, hardcoded for sample purposes
  - `/api/v1/comments` - Returns a list of comments, hardcoded for sample purposes
  - `/api/ready` - A K8s ready endpoint, returns 200 OK with a "success" body
  - `/api/liveness` - A K8s liveness endpoint, returns 200 OK with a "success" body

## Running locally

```commandline
export FLASK_APP=api_sample
export POD_NAME=localhost
flask --debug run
```

## OpenFaas

The two API endpoints are also implemented as OpenFaas functions, controlled via `open-faas.yml` and found in `users` 
and `comments` directories.

Checkout the additonal job in the `ci.yml` workflow for how it is used.
