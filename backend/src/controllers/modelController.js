const modelService = require("../services/modelService");

exports.getModel = async (req, res, next) => {
    try {
        const result = await modelService.getModel();

        res.json(result);
    } catch (err) {
        next(err);
    }
};

exports.generate = async (req,res,next) =>{
    try{
        const result = await modelService.generate(req.body.prompt);
        res.json(result);
    }catch(err){
        next(err);
    }
}