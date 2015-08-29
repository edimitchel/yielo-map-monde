function initSession(domain, port, api) {
    return function(userId){
        navigator.geolocation.getCurrentPosition(function(position) {
            Communication.get(domain, port).emit('init_session', {
                id_user : userId,
                geolocalisation : {
                    la : position.coords.latitude,
                    lo : position.coords.longitude
                }
            });
        });
    }
}
