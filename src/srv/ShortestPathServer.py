import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"


if __name__ == '__main__':
	# cherrypy.config.update({'log.screen': False,
 #                        'log.access_file': '',
 #                        'log.error_file': ''})
    cherrypy.quickstart(HelloWorld(), '/')
