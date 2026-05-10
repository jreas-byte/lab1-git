const axios = require('axios');

axios.get('https://api.github.com')
  .then(response => {
    console.log('Status:', response.status);
    console.log('Server:', response.headers.server);
  })
  .catch(error => {
    console.log(error);
  });
