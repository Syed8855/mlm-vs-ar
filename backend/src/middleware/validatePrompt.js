function validatePrompt(req, res, next) {
    const {prompt} = req.body;
    if (!prompt){
        return res.status(400).json({
            error: "Prompt is required"
        });
    }
    next();
}
module.exports = validatePrompt;