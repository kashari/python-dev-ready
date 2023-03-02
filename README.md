# python-dev-ready
Dockerized development environment using python 3.9 (Here an example with FastAPI but it supports Django and Flask also. See `start-server.sh`)

## how to run
```run docker-compose up -d ``` and you should be fine to go with a running server according to your app via http://localhost 
Note that your app should be inside the `/app` folder or simply modify the build files with the proper names.
### Note:
Also make sure to freeze the `pip` requirements into a file named `requirements.txt` inside the `/app` folder or just navigate inside that folder and run `pip freeze > requirements.txt`. Enjoy!