const express = require('express');
const router = express.Router();
const models = require('../data/models.json');

router.get('/',(req,res) => {
    res.json(models);
});

module.exports = router;