//backend//src/app.js
const express = require('express');
const cors = require('cors');

const logger = require('./middleware/logger');
const errorHandler = require('./middleware/errorHandler');
const modelRoute = require('./routes/models');

const app = express();

// Global Middleware
app.use(logger);
app.use(cors());
app.use(express.json());

//Routes
app.get('/', (req,res) => {
    res.json({
        message: 'MLM vs AR Benchmark API'
    });
});

app.use('/models' ,modelRoute);


app.use(errorHandler);

module.exports = app;