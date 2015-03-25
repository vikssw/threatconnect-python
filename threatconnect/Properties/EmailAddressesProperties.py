""" custom """
from threatconnect.Config.ResourceType import ResourceType
from threatconnect.Properties.IndicatorsProperties import IndicatorsProperties


class EmailAddressesProperties(IndicatorsProperties):
    """
    URIs:
    /<api version>/indicators/emailAddresses
    /<api version>/groups/adversaries/<ID>/indicators/emailAddresses
    /<api version>/groups/emails/<ID>/indicators/emailAddresses
    /<api version>/groups/incidents/<ID>/indicators/emailAddresses
    /<api version>/groups/signatures/<ID>/indicators/emailAddresses
    /<api version>/groups/threats/<ID>/indicators/emailAddresses
    /<api version>/securityLabels/<security label>/indicators/emailAddresses
    /<api version>/tags/<tag name>/indicators/emailAddresses
    /<api version>/victims/<ID>/indicators/emailAddresses

    JSON Data:
    {"id" : 1784795,
     "ownerName" : "Acme Corp",
     "dateAdded" : "2015-03-18T15:28:57Z",
     "lastModified" : "2015-03-18T15:28:57Z",
     "rating" : 1.0,
     "confidence" : 25,
     "webLink" : "https://app.threatconnect.com/tc/auth/indicators/
         details/emailaddress.xhtml?emailaddress=elder.gudiel%40telefonica.com&owner=Acme+Corp",
     "address" : "elder.gudiel@telefonica.com"}

    """
    def __init__(self):
        """ """
        super(EmailAddressesProperties, self).__init__()

        # resource properties
        self._resource_key = 'emailAddress'
        self._resource_pagination = True
        self._resource_type = ResourceType.EMAIL_ADDRESSES
        self._resource_uri_attribute += '/emailAddresses'

        # update data methods
        self._data_methods.pop('summary')
        self._data_methods['address'] = {
            'get': 'get_indicator',
            'set': 'set_address',
            'var': '_indicator'}
