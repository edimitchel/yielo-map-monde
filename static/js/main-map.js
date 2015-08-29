
;(function MapMondeLive(context){
    var users = [];

    function addUsers(userOrUsers){
        var usersBefore = users;
        if(typeof userOrUsers == 'array') {
            users.concat(userOrUsers);
            for(var i = 0; i < users.length; i++)
                userAdded(usersBefore, users[i]);
        }
        else {
            users.push(userOrUsers);
            userAdded(usersBefore, userOrUsers);
        }
    }


    var map = new OpenLayers.Map("map-monde");
    var mapnik = new OpenLayers.Layer.OSM();
    map.addLayer(mapnik);

    var markers = new OpenLayers.Layer.Markers( "Markers" );

    Communication.get().emit('get_users');
    Communication.get().on('pull_users', function(data){
        users.concat(data);
    });

    Communication.get().on('new_user', function(data){
        users.push(data);
    });

    function userAdded(before, user) {
        if(user.id === user_id) {
            // On se localise.

            var LonLat = new OpenLayers.LonLat(user.position.latitude, user.position.longetitude)
                .transform(
                    new OpenLayers.Projection("EPSG:4326"), //transform from WGS 1984
                    map.getProjectionObject() //to Spherical Mercator Projection
                );

            markers.addMarker(new OpenLayers.Marker(LonLat));

            map.setCenter(lonLat, 16);

            return;
        }
        map.addLayer(markers);
    }
})(window);
