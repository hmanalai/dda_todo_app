from django_declarative_apis import authentication
from django_declarative_apis.adapters import resource_adapter
from todo import resources

class NoAuth(authentication.Authenticator):
    """A custom NoAuth class to treat all requests as authenticated
    By default, django-declarative-apis requires authentication. This allows us to get around that.
    """

    @staticmethod
    def is_authenticated(request):
        return True

    def challenge(self, error):
        super().challenge(error)


TodoEndpoint = resource_adapter(
    post=resources.TodoUpdateDefinition,
    get=resources.TodoDefinition,
    authentication={None: (NoAuth(),)},
)


TodoDetailEndpoint = resource_adapter(
    get=resources.TodoSingleTaskDefinition,
    delete=resources.TodoDeleteSingleTaskDefinition,
    post=resources.TodoUpdateSingleTaskDefinition,   # put
    authentication={None: (NoAuth(),)},
)