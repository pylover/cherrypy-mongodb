
import cherrypy
import mongodb_tool as dbtool
from cherrypy._cperror import HTTPRedirect


class Root(object):
    
    @cherrypy.expose
    @cherrypy.tools.mongodb()
    def index(self):
        db = cherrypy.request.mongodb
        for item in db.items.find():
            yield str(item)
            yield '<br />'
    
    @cherrypy.expose
    @cherrypy.tools.mongodb()
    def create_test_data(self, name=None, language=None):
        db = cherrypy.request.mongodb
        if not db.items.find_one({'name':name}):
            db.items.insert({'name':name,
                             'language': language})
        raise HTTPRedirect ('/')
        
        
        

if __name__ == '__main__':
    cherrypy.quickstart(Root(), '', config={
        'global':{
            'tools.mongodb.dbname' :    'demo'
        },
        '/':{}
    })
