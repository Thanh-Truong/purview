from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient, AtlasEntity, AtlasProcess
import json
import excel
import account

def get_configuration():
    with open('configs.json') as json_file:
        return json.load(json_file)

def build_service_principal():
    with open('auth.json') as json_file:
        data = json.load(json_file)
        auth = ServicePrincipalAuthentication(
            tenant_id = data["tenant_id"],
            client_id = data["client_id"], 
            client_secret = data["client_secret"],
            )
        return auth

def upload_entities(client):
    entities = excel.parse_excel_file_to_entities()
    if not entities and len(entities) > 0:
        return client.upload_entities(entities)

def list_glossary_terms(client):
    glossary = client.get_glossary(name="Glossary", guid=None, detailed=True)
    try:
        return glossary["termInfo"]
    except KeyError:
        print("Your default glossary appears to be empty.")
        exit(3)

def main():
    configs = get_configuration()
    # Create a client to connect to your service.
    client = PurviewClient(
        account_name = configs["Purview-account-name"],
        authentication = build_service_principal()
    )

    upload_entities(client)
    termInfos = list_glossary_terms(client)
    print(json.dumps(termInfos, indent=2))
    
    results = client.import_terms(csv_path='terms.csv', glossary_name="Glossary", glossary_guid=None)
    print(json.dumps(results, indent=2))
    #account.


if __name__ == "__main__":
    account.create_purview()