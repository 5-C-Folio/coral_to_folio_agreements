import folio_api
import json
from csv import DictReader
from uuid import uuid4
from datetime import datetime

def string_to_dict(string):
    #smith uses , to split- umass ;
    sp_string = string.split(',')
    altList = []
    for row in sp_string:
        sprow = row.split(':')
        altname = {"value" : sprow[1].lstrip(), "description":sprow[0]}
        altList.append(altname)
    return altList

class agreement():
    def __init__(self,**kwargs):

        self.coralID = None
        self.orgCode = None
        self.name = None
        self.description = None
        self.startDate = None
        self.endDate = None
        self.isPerpetual = None
        self.renewalPriority = None
        self.orgs = []
        self.periods = []
        self.alias = None
        self.periodNote = None
        self.__dict__.update(kwargs)

    def orgGetter(self, orgObject):
        # query the org object for a uuid
        self.org = {"org": {"orgsUuid": orgObject.get("UM" + self.orgCode)}, "role": "content_provider"}
        self.orgs.append(self.org)


    def serialize(self):
        if self.endDate is not None and len(self.endDate) > 1:
            self.periods.append({"startDate": datetime.strptime(self.startDate,"%m/%d/%Y"), "endDate": self.endDate.date()})
        else:
            self.periods.append({"startDate": str(datetime.strptime(self.startDate,"%m/%d/%Y").isoformat()), "note": self.periodNote})

        if self.alias is not None:
            self.alias = string_to_dict(self.alias)

        self.id = str(uuid4())

        return json.dumps({
          "id" : self.id,
          "name": self.name,
          "description": self.description,
          "periods" : self.periods,
          "isPerpetual": self.isPerpetual,
          "renewalPriority": self.renewalPriority,
          "orgs" : self.orgs,
          "agreementStatus": "Active"

        }, indent = 4)



if __name__ == "__main__":
    x = open("credentials.json", "r")
    credentials = json.load(x)
    print (credentials)
    orgObject = folio_api.organization( credentials['URL'], credentials['tenant'])
    orgObject.getToken(credentials['userName'], credentials['password'])
    orgObject.get_orgs('UM')
    orgObject.get_noteTypes()
    with open ("orgs/Coral/agreements/umResources3.csv" ,"r", encoding='utf8') as coralResource:
         coralDict = DictReader(coralResource)
         for row in coralDict:
             workingAgreement = agreement(coralID = row['resourceID'],
                                          orgCode = row['orgCode'],
                                          name = row['titleText'],
                                          description = row['descriptionText'],
                                          startDate = row['currentStartDate'],
                                          endDate = row['currentEndDate'],
                                          periodNote = "order#: " +row["orderNumber"] + ", system#: " + row['systemNumber'])
             workingAgreement.orgGetter(orgObject.org_key)
             print (workingAgreement.serialize())