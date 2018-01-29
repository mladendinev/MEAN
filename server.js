// server.js

// call the packages we need
var express    = require('express');        // call express
var app        = express();                 // define our app using express
var bodyParser = require('body-parser');

// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8080;        

var mongoose   = require('mongoose');
mongoose.connect('mongodb://localhost:27017/weather_data');

var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));

db.once('open', function() {
  console.log("DB connection alive");
});

var Weather = require('./app/models/weather');

// Routes
// =============================================================================
var router = express.Router();             

// middleware to use for all requests
router.use(function(req, res, next) {
    // do logging
    console.log('Middleware log statement');
    next();
});


router.get('/weather', function(req, res) {
		Weather.find(function(err, data) {
			if (err)
				res.send(err);

			res.json(data);
		});
});

router.get('/weather/:city', function(req, res) {
        cityParam = req.params.city;
		Weather.find({'city': cityParam}, function(err, data) {
			if (err)
				res.send(err);

			res.json(data);
		});
});

// more routes for the API will happen here

// REGISTER routes
// all of our routes will be prefixed with /axway
app.use('/axway', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Server started on port: ' + port);