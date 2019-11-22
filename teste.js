let axios = require('axios').default;
axios({
    method: 'GET',
    url: 'https://api-mercado-django.herokuapp.com/lote',
    responseType: 'json'
}).then(function (reposta) {
    console.log(resposta);
});
