//backend/src/routes/models.js
const express = require('express');
const router = express.Router();

const {
    getModel
} = require('../controllers/modelController');

router.get('/', getModel); 

module.exports = router;