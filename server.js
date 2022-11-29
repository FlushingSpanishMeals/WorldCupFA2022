const express = require('express');
const path = require('path');


const app = express();

const port = 3000;

//Middleware 
app.use(express.static(path.join(__dirname, 'css')));


app.get('/', (request, response)=>{
    response.sendFile(path.join(__dirname, './index.html'));
});

app.get('/about', (request, response)=>{
    response.sendFile(path.join(__dirname, './about.html'));
});

app.get('/matches', (request, response)=>{
    response.sendFile(path.join(__dirname, './matches.html'));
});

app.get('/signup', (request, response)=>{
    response.sendFile(path.join(__dirname, './signup.html'));
});


app.listen(port, () =>{
    console.log(`Express Server Listening on port ${port}!`);
});