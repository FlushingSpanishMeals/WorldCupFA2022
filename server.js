const { response } = require('express');
const express = require('express');

const app = express();

const port = 3000;

//Middleware 
// app.use(express.static(path.join(__dirname, '.')));


app.get('/', (request, response)=>{
    response.sendFile(path.join(__dirname, '.index.html'));
});

// app.get('/about', (request, response)=>{
//     response.sendFile(path.join(__dirname, './WorldCupFA2022/about.html'));
// });

// app.get('/matches', (request, response)=>{
//     response.sendFile(path.join(__dirname, './WorldCupFA2022/matches.html'));
// });

// app.get('/signup', (request, response)=>{
//     response.sendFile(path.join(__dirname, './WorldCupFA2022/signup.html'));
// });


app.listen(port, () =>{
    console.log(`Express Server Listening on port ${port}!`);
});