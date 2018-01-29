var mongoose = require('mongoose');
var WeatherSchema = mongoose.Schema;

var data = new WeatherSchema({city: String,
                       humidity: Number,
                       date: Date,
                       temperature: { temp_max: Number, temp_kf: Number, temp: Number, temp_min: Number},
                       wind: {speed: Number, deg:Number}}, {collection:'weather_historical_data'})

module.exports = mongoose.model('Bear', data);