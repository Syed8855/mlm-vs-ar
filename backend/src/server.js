const express = require('express');
const cors = require('cors');
const modelRoutes = require('./routes/models');
const app = express();

app.use(cors());
app.use(express.json());

app.get('/', (req,res) => {
    res.json({
        message: 'MLM vs AR Benchmark API'
    });
});
app.use('/models' ,modelRoutes);
const PORT = 5000;
 app.listen(PORT, () => {
    console.log(`Server running on ${PORT}`);
 });
