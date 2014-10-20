from facepy import GraphAPI

from weppy import session
from weppy_oauth2 import Oauth2, LoginHandler


class FBAuth(Oauth2):
    config_mandatory = ['client_id', 'client_secret']
    auth_url = "https://graph.facebook.com/oauth/authorize"
    token_url = "https://graph.facebook.com/oauth/access_token"

    def load(self, auth):
        self.config_default.update(
            scope=["email", "user_about_me"],
            fields=["first_name", "last_name", "username", "email"]
        )
        self.config.auth_url = self.auth_url
        self.config.token_url = self.token_url
        Oauth2.load(self, auth)
        self.graph = None

    def _add_action(self):
        self.auth.register_action('facebook', self.fb)

    def fb(self, *args):
        return self.auth._login_with_handler(FBHandler, self.config)


class FBHandler(LoginHandler):
    def get_user(self):
        if not self.accessToken():
            return None
        if not self.graph:
            self.graph = GraphAPI(self.accessToken())
        user = None
        try:
            fields = ",".join(self.env.fields)
            user = self.graph.get("me?fields="+fields)
        except GraphAPI.FacebookError:
            session.token = None
            self.graph = None
        if user:
            return self.env.get_user(user)
        return None
