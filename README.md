# Worldline demo project

This is to fulfill the test as outlined by [this gist](https://gist.github.com/dpaymark/36bb8cde62dec758fb2045c70c2b6425)

## Usage

Ensure that [Docker](https://www.docker.com/products/docker-desktop/) is installed and running

Use your environment of choice (VS Code w/ the Dev Containers extension is the easiest) to clone the repository in a container

```sh
> git clone https://github.com/...
```

Use `uvicorn` to run the endpoint server

```sh
> uvicorn main:app
```

HTTP POST requests will be accepted on the endpoint address at port 8000.  
Use the `/redoc` path to view a pretty schema of the endpoint

## Architecture

The repository is setup as a combined Python-based HTTP endpoint, as well as PostgreSQL database for storing transaction data

The use of FastAPI enables built-in automated endpoint documentation and simple use of HTTP REST-ful requests
