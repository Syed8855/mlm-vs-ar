//backend/src/routes/models.js
const express = require('express');
const router = express.Router();

const {
    getModel,
    generate
} = require('../controllers/modelController');

router.get('/', getModel); 

const  validatePrompt = require('../middleware/validatePrompt');
router.post('/generate', validatePrompt, generate);

module.exports = router;