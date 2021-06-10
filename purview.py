from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient, AtlasEntity, AtlasProcess
import json

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

def foo(client):
    # Create two entities with AtlasEntity
    # You must provide a name, typeName, qualified_name, and guid
    # the guid must be a negative number and unique in your batch
    # being uploaded.
    input01 = AtlasEntity(
        name="input01",
        typeName="DataSet",
        qualified_name="pyapacheatlas://demoinput01",
        guid=-100
    )
    output01 = AtlasEntity(
        name="output01",
        typeName="DataSet",
        qualified_name="pyapacheatlas://demooutput01",
        guid=-101
    )

    # The Atlas Process is the lineage component that links the two
    # entities together. The inputs and outputs need to be the "header"
    # version of the atlas entities, so specify minimum = True to
    # return just guid, qualifiedName, and typeName.
    process = AtlasProcess(
        name="sample process",
        typeName="Process",
        qualified_name="pyapacheatlas://democustomprocess",
        inputs=[input01],
        outputs=[output01],
        guid=-102
    )

    # Convert the individual entities into json before uploading.
    results = client.upload_entities(
        batch=[output01, input01, process]
    )

    print(json.dumps(results, indent=2))

def main():
    configs = get_configuration()
    # Create a client to connect to your service.
    client = PurviewClient(
        account_name = configs["Purview-account-name"],
        authentication = build_service_principal()
    )
    foo(client=client)

if __name__ == "__main__":
    main()