from folio_api import organization, requestObject
import json

class note(requestObject):

    def __init__(self, requestObject, type, title, content, coralID, linkID):
        requestObject.__init__(self, requestObject)
        self.domain = 'agreements'
        self.title = title
        self.content=content
        self.links = None
        self.type = type
        self.coralID = coralID



    def typeGetter(self,typeObject):
        self.typeID = typeObject.get(self.type)

    def serialize(self):
        return json.dumps(self, default=lambda o : o.__dict__)

if __name__ == "__main__":
    credfile = open("credentials.json", 'r')
    credentials = json.loads(credfile)
    noteObject= note