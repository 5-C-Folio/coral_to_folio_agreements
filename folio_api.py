import requests
import json


class requestObject():
    def __init__(self, url, tenant):
        if url[-1] == '/':
            self.url = url
        else:
            self.url = url + '/'
        self.tenant = tenant
        self.token = None

    def getToken(self, userName, Password):

        headers = {'Content-Type': 'application/json',
                   'x-okapi-tenant': self.tenant}
        payload = {"username" : userName,
                   "password": Password}
        connection_url = self.url + "authn/login"
        login = requests.post(connection_url, headers=headers, data=json.dumps(payload))

        try:
            self.token = login.headers['x-okapi-token']

        except KeyError:
            print (login.text)

class organization(requestObject):

    def get_orgs(self, orgCode):
        if self.token is None:
            print("get a token!")
            exit()
        headers = {'Content-Type': 'application/json', 'x-okapi-tenant': self.tenant, 'x-okapi-token': self.token}
        r_url = f'{self.url}organizations-storage/organizations?query=code=="{orgCode}*"&limit=1200'
        orgs = requests.get(r_url, headers = headers, timeout= .5)
        json_response = json.loads(orgs.text)
        self.org_key = {}
        for results in json_response['organizations']:

            self.org_key[results["code"]] = results['id']



if __name__ == '__main__':
    x = open("credentials.json", "r")
    credentials = json.load(x)

