from django.conf.urls import url
from todo import handlers

uuid4_regex = r"[0-9]{1}"

urlpatterns = [
    url(
        r"^tasks/$",
        handlers.TodoEndpoint,
    ),
    url(
        r"^tasks/(?P<id>{0})/$".format(uuid4_regex),
        handlers.TodoDetailEndpoint,
        ),
]