const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Connected');
});

app.get('/predict', (req, res) => {
  const prediction = {
    Result: 'This is your example result',
  };
  res.send(prediction);
});

app.listen(port, () => {
  console.log('Server Listening on PORT:', port);
});
