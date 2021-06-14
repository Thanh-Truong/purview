from pyapacheatlas.core import PurviewClient
import requests

class ExtendedPurviewClient(PurviewClient):
    """
    Provides communication between your application and the Azure Purview
    service. Simplifies the requirements for knowing the endpoint url and
    requires only the Purview account name.

    :param str account_name:
        Your Purview account name.
    :param authentication:
        The method of authentication.
    :type authentication:
        :class:`~pyapacheatlas.auth.base.AtlasAuthBase`
    """

    def __init__(self, account_name, authentication=None):
        super().__init__(account_name, authentication)
    
    # def delete_glossary_term(self, termguid):
    #     """
    #     Delete one or many termguid from your Apache Atlas server.

    #     :param termguid: The termguid you want to remove.
    #     :type guid: Union(str,list(str))
    #     :return:
    #         204 No Content OK. If glossary term delete was successful.
    #         404 Not Found
    #         If glossary term guid in invalid.
    #     :rtype: int
    #     """
    #     results = None

    #     atlas_endpoint = self.endpoint_url + \
    #         "/glossary/term/{termguid}".format(termguid)
    #     response = requests.delete(
    #         atlas_endpoint,
    #         headers=self.authentication.get_authentication_headers())

    #     results = self._handle_response(response)

    #     return results