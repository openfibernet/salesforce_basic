# salesforce_basic

Simple Python API client library for Salesforce

## Installation

To install run `pip install salesforce_basic`.

## Running

This is a simple wrapper to the salesforce REST API (https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest_resources.htm) which includes oauth authentication.

To use:

```python
from salesforce_basic import SalesforceBasicConnector

connector = SalesforceBasicConnector(sandbox = False, **kwargs)
```

The kwargs to create the connector set up the url to talk to and the oauth related tokens.  The oauth tokens can either by read from an AWS ssm parameter (if 'region_name' and 'name' keywords are passed) or passed directly via the keywords 'client_id', 'client_secret', 'access_token' 'refresh_token' and 'request_url'.









