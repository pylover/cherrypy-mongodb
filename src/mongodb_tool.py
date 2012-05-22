
import cherrypy
import pymongo  

CP_REQUEST_ATTR_NAME = "_mongodb"

def mongodb_loader(dbname, host=None, port=27017, max_pool_size=10, network_timeout=None,
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
    
cherrypy.tools.mongodb = cherrypy.Tool('on_start_resource', mongodb_loader)
