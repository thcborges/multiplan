# Multiplan Challenge

## Rent The Runway

### Executing
You can execute the project locally with docker using the bellow command

```bash
docker run -p 5000:5000 thcborges/renttherunway
```

Then you can access in your favorite browser in `localhost:5000`.


### Development

The project was built using the docker Python3.10 image with Poetry as package manager.

It is based on a Dash web application.

During the deployment of the docker image the required datasets are build in [multiplan/build.py](multiplan/build.py).


