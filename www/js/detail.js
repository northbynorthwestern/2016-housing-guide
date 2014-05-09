  $(function() {
    $(".rslides").responsiveSlides();
  });

  var geojson;

  var defaultStyle = {'weight': '0', fillColor: '#381f5e', fillOpacity: '1'};

  var map = L.map('small-map', {
    minZoom: 15,
    maxBounds: [
      [42.07095890994855, -87.65922546386719],
      [42.039094188385945, -87.69158363342285]
    ]
  }).setView([42.05504447993239,-87.6753830909729], 16);
  L.tileLayer.provider('MapQuestOpen.OSM').addTo(map);

   $.ajax({
    url: 'http://nbn-housing.s3.amazonaws.com/static/json/{{dorm.slug}}.json',
    async: true,
    dataType: 'jsonp',
    jsonp: false,
    jsonpCallback:'myCallback',
    success:function(data) {
        parse_map_data(data);
    }
  });
  function parse_map_data(data){
    $.each(data, function(key, val){
        geojson = new L.GeoJSON(val, {
          style: function(feature) {
          return defaultStyle;
        }
      }).addTo(map);
      var bounds = geojson.getBounds();
      map.setView(bounds.getCenter(), 17);
    });
}

$('#video-tab').click(function() {
  $('#embed-container').append('<iframe src="{{dorm.video_embed}}" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>');
  $('#media-container img').css('display', 'none');
  $('#video-tab').css('background', '#381F5E');
  $('#photo-tab').css('background', '#c3bccf');
  $('#embed-container').css('display','block');
});

$('#photo-tab').click(function() {
  $('#embed-container iframe').remove();
  $('#embed-container').hide();
  $('#media-container img').css('display', 'block');
  $('#photo-tab').css('background', '#381F5E');
  $('#video-tab').css('background', '#c3bccf');
});