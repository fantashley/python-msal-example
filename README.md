# python-msal-example
Basic Azure AD username password login example using Microsoft Authentication Library

Once you have your python environment set up with the included requirements.txt, use this command to run the test:
```bash
FLASK_APP=app.py CLIENT_ID=<client_id> AUTHORITY=<authority> USERNAME=<azure_ad_username> \
PASSWORD=<azure_ad_password> flask run -h localhost -p <callback_uri_port>
```
