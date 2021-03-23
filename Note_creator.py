from folio_api import organization, requestObject
import json
import requests
#the most important part of this script requires that a custom property be created with the key from coral.  This will be used as the match point to assign the notes
class note(requestObject):
    def __init__(self, url, tenant):
        super(note,self).__init__(url,tenant)
        self.agreement = None

    def typeGetter(self,typeObject):
        self.typeID = typeObject.get(self.type)

    def coral_id(self, coralID):
        #search agreements for the custom property with the coral ID
        headers = {'Content-Type': 'application/json', 'x-okapi-tenant': self.tenant, 'x-okapi-token': self.token}
        r_url = f'{self.url}erm/sas?filters=customProperties.coralID.value=={coralID}'
        response = requests.get(r_url, headers=headers,timeout= .5 )
        try:
            self.agreement = json.loads(response.text)[0]
        except IndexError:
            print (f"{coralID} is not valid")

    def get_noteTypes(self):
        #get note types
        if self.token is None:
            print("get a token!")
            exit()
        headers = {'Content-Type': 'application/json', 'x-okapi-tenant': self.tenant, 'x-okapi-token': self.token}
        r_url = f'{self.url}note-types?limit=100'
        noteTypesR = requests.get(r_url, headers=headers, timeout=.5)
        json_response = json.loads(noteTypesR.text)
        self.noteTypes = {}
        for results in json_response['noteTypes']:
            self.noteTypes[results["name"]] = results['id']

    def serialize(self):
        return json.dumps(self, default=lambda o : o.__dict__)



if __name__ == "__main__":
    credfile = open("5cCredentials.json", 'r')
    credentials = json.load(credfile)
    noteObject= note(credentials['URL'], credentials['tenant'])
    noteObject.getToken(credentials['userName'], credentials["password"])
    #I cannot remember what this line is supposed to do
    noteObject.coral_id("UM9999")
    print (json.dumps(noteObject.agreement, indent=4))
