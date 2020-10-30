## To run locally
- Install [Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/).
- Clone the repo and run docker-compose.
```shell
git clone https://github.com/simpuid/cvbuilder.git
cd cvbuilder
docker-compose up
```
- Go to [localhost:5000](http://localhost:5000/) to use the application.
- Run `docker-compose down` to stop the containers.

Note:
1. To use [adminer](https://www.adminer.org/), go to [localhost:8080](http://localhost:8080/).
2. Some default users have been added for testing purposes:
```python
for i in range(100,201):
  username = i
  password = i
```
__So you can pick any number number between 100 and 200 and use that as user id and password.__

### Live Demo: [`CV Builder`](http://iitr-cvbuilder.herokuapp.com)
