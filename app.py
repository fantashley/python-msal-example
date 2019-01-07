from flask import Flask
from msal import PublicClientApplication
import os

class PythonMSAL:
    
    def __init__(self, client_id, authority, username, password, scopes):
        self.client_id = client_id
        self.authority = authority
        self.username = username
        self.password = password
        self.scopes = scopes


    def msal_connect(self):

        app = PublicClientApplication(self.client_id, authority=self.authority)
        
        result = None
        
        accounts = app.get_accounts()
        if accounts:
            # If so, you could then somehow display these accounts and let end user choose
            print("Pick the account you want to use to proceed:")
            for a in accounts:
                print(a["username"])
            # Assuming the end user chose this one
            chosen = accounts[0]
            # Now let's try to find a token in cache for this account
            result = app.acquire_token_silent(config["scope"], account=chosen)
        
        if not result:
            # So no suitable token exists in cache. Let's get a new one from AAD.
            result = app.acquire_token_by_username_password(self.username, self.password, scopes=self.scopes)
        return result


flapp = Flask(__name__)

@flapp.route("/")
def test_connection():
    msal_obj = PythonMSAL(os.environ['CLIENT_ID'],
                          os.environ['AUTHORITY'],
                          os.environ['USERNAME'],
                          os.environ['PASSWORD'],
                          ["user.read"])

    result = msal_obj.msal_connect()

    if "access_token" in result:
        return result["access_token"]
    else:
        return result.get("error") + " " + \
               result.get("error_description") + " " + \
               result.get("correlation_id")

