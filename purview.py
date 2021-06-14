from os import times
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import AtlasEntity, AtlasProcess
import json
import argparse

from pyapacheatlas.core.client import PurviewClient
import excel
import account
from purview_client import ExtendedPurviewClient

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

def build_all_terms_guid(client):
    termsInfo = list_glossary_terms(client)
    return [i for i in termsInfo]

def main():
    parser = argparse.ArgumentParser(description='Interaction with Purview')
    parser.add_argument("--create-purview", action='store_true')
    parser.add_argument("--delete-purview", action='store_true')
    parser.add_argument("--list-terms", action='store_true')
    parser.add_argument("--upload-entities", action='store_true')
    parser.add_argument("--import-terms", action='store_true')
    parser.add_argument("--delete-term", help="Delete a term from the default Glossary")
    parser.add_argument("--delete-all-terms", action="store_true", help="Delete all terms from the default Glossary")
    args = parser.parse_args()

    configs = get_configuration()
    # Create a client to connect to your service.
    client = ExtendedPurviewClient(
        account_name = configs["Purview-account-name"],
        authentication = build_service_principal()
    )
    if args.create_purview:
        account.create_purview()
        account.assign_roles()
    
    if args.delete_purview:
        account.delete_purview()

    if args.upload_entities:
        upload_entities(client)
    
    if args.list_terms:
        termInfos = list_glossary_terms(client)
        print(json.dumps(termInfos, indent=2))
    
    if args.import_terms:
        results = client.import_terms(csv_path='terms.csv', glossary_name="Glossary", glossary_guid=None)
        print(json.dumps(results, indent=2))

    if args.delete_term:
        res = client.delete_glossary_term(args.delete_term)
        print(json.dumps(res, indent=2))

    if args.delete_all_terms:
        term_guids = build_all_terms_guid(client)
        client.delete_all_terms(term_guids)
        
        
if __name__ == "__main__":
    main()