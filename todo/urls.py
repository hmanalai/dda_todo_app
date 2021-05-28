from django.conf.urls import url
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

# Question:
# - Q: When going to an endpoint, how does it know when it's post, get, etc.?
# - A: separate endpoints for post, get, etc.

urlpatterns = [
    url(
        r"^tasks/$",
        resource_adapter(post=resources.TodoUpdateDefinition,
                         authentication={None: (NoAuth(),)},),
    ),
]