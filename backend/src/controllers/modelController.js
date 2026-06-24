const models = require('../data/models.json');

exports.getModels = (req, res) => {
    res.json(models);
};