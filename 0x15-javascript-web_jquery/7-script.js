$.get('https://swapi.co.alx-tools.com/api/people/5/?format=json', function (data) {
    $('DIV#character').text(data.name);
});
