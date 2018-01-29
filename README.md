# Axway Excercise

Underlying architecture:

![alt text](https://image.ibb.co/dTJL9R/Untitled_Diagram2.png)

The server has two endpoints currently approachable at:
  - http://localhost:8080/axway/weather access weather information for all cities Paris, London, Sofia, Madrid, Bucharest
  - http://localhost:8080/axway/weather/city access weather information for one city

### Prerequisites
 - Mongo
 - Python 2.7
 - RabbitMQ
 - Reddis


### Installation

Install Celery

```sh
$ pip install celery
```

Install Express Project

```sh
$ cd 
$ npm install 
```

### Start up
```sh
$ node server.js
```


### Todos
 - Write Unit Tests
 - Write Angular.js client
 - Flexible configuration, auth mechanism
 
 
### Author
  Mladen Dinev (mladenddinev@gmail.com)





