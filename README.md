# weppy-FBAuth

weppy-FBAuth is an extension for [weppy framework](http://weppy.org) providing a simple interface to manage logins with Facebook authentication.

## Installation

You can install weppy-FBAuth using pip:

    pip install weppy-FBAuth

And add it to your weppy application:

```python
def get_facebook_user(user):
    # code to process the user from oauth service

from weppy_fbauth import FBAuth

app.config.FBAuth.client_id = "<your app id>"
app.config.FBAuth.client_secret = "<your app secret>"
app.config.FBAuth.get_user = get_facebook_user

app.use_extension(FBAuth)
```

## Documentation

The documentation will be soon available.
