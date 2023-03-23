# python-api-sample
A sample Python API in Flask

## PyPi Dependency updates

    docker run -it --rm -v ${PWD}:/repo -w /repo python:3.11.2-slim bash
    pip install --upgrade pip
    pip install --upgrade Flask gunicorn
    pip freeze > requirements.txt

## API Endpoints

  - `/api/v1/users` - Returns a list of users, hardcoded for sample purposes
  - `/api/ready` - A K8s ready endpoint, returns 200 OK with a "success" body
  - `/api/liveness` - A K8s liveness endpoint, returns 200 OK with a "success" body

## Running locally

```commandline
export FLASK_APP=api_sample
export POD_NAME=localhost
flask --debug run
```