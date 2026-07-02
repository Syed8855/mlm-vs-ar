//services/modelService.js
async function getModel(){
    const models = require('../data/models.json');
    return models;
}

async function generate(prompt){
        const result ={
            prompt,
            message:"Successfully generated result"
        };
        return result;
    
}
module.exports ={
    generate,
    getModel
};