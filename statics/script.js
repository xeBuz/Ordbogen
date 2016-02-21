$.fn.api.settings.api = {
  'get continents' : '/api/continents/',
  'get countries'  : '/api/countries/',
  'get country'    : '/api/countries/{code}',
  'search country' : '/api/countries/?name={name}',
};


//$.fn.api.settings.api.search = '/api/countries/?name={name}';
// $('.routed.example .search input')
//  .api({
//    action       : 'search',
//    stateContext : '.ui.input'
//  })
//;


$(document)
.ready(function () {

$('.ui.search')
  .search({
    apiSettings: {
      action: 'get countries',
      onResponse: function(Country) {
        var response = [];

        console.log(Country.data);
        $.each(Country.data, function(index, item){
          console.log(item.short_name)
            response.push({
            name  : item.short_name
          });

        });
        console.log(response);
        return response;
      }
    },
    fields: {
      results : 'data',
      name    : 'short_name'
    },
    minCharacters : 2,
    //debug: true,
    //verbose: true
  })
;

});