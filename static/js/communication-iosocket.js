var Communication = {
	domain : document.domain,
	port : '5000',
	namespace : '/api',
    socket : null,
    get : function(domain, port, namespace) {
        if(this.socket == null){
            this.init(domain, port, namespace);
        }
        return this.socket;
    },
    init : function(domain, port, namespace) {
        if(typeof namespace == 'string') this.namespace = namespace;
        if(typeof port == 'string') this.port = port;
        if(typeof domain == 'string') this.domain = domain;

        if(this.socket == null){
            this.socket = io.connect('http://' + this.domain + ':' + this.port + this.namespace);
        }
    }
}
