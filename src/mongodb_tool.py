
import cherrypy
import pymongo  

CP_REQUEST_ATTR_NAME = "_mongodb"


def _attach_mongodb_loader(dbname, host=None, port=27017, max_pool_size=10, network_timeout=None,
                   tz_aware=False, property_name='mongodb'):
    def _get_mongodb(request):
        if not hasattr(request, CP_REQUEST_ATTR_NAME) or not getattr(request, CP_REQUEST_ATTR_NAME):
            connection = pymongo.Connection(
                host=host,
                port=port,
                max_pool_size=max_pool_size,
                network_timeout=network_timeout,
                document_class=dict,
                tz_aware=tz_aware,
                _connect=False)
            
            db = getattr(connection, dbname)
            setattr(request, CP_REQUEST_ATTR_NAME, db)
        return getattr(request, CP_REQUEST_ATTR_NAME)
    setattr(cherrypy.request.__class__, property_name, property(_get_mongodb))


class MongoDBTool(cherrypy.Tool):
   
    def __init__(self):
        cherrypy.Tool.__init__(self, 'on_start_resource', self.on_start_resource, "mongodb", 50)

    def on_start_resource(self, **kwargs):
        _attach_mongodb_loader(**kwargs)
        cherrypy.request.hooks.attach('on_end_resource', self.on_end_resource)
        
    def on_end_resource(self, **kwargs):
        if hasattr(cherrypy.request, CP_REQUEST_ATTR_NAME) and getattr(cherrypy.request, CP_REQUEST_ATTR_NAME):
            c = getattr(cherrypy.request, CP_REQUEST_ATTR_NAME).connection
            c.close()
            c.disconnect()

    def _setup(self):
        if cherrypy.request.config.get('tools.staticdir.on', False) or \
            cherrypy.request.config.get('tools.staticfile.on', False):
                return
        cherrypy.Tool._setup(self)
    
cherrypy.tools.mongodb = MongoDBTool()
