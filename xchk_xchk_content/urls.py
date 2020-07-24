from django.urls import path

from . import contentviews

urlpatterns = [
    path('xchk_concept_1', contentviews.XchkConceptView.as_view(), name=f'{contentviews.XchkConceptView.uid}_view'),
]
# kunnen we hier aan bij include??
# waarschijnlijk niet als we include doen van de hele module, zie https://docs.djangoproject.com/en/3.0/topics/http/urls/#url-namespaces-and-included-urlconfs ("not the list of urlpatterns itself") → als we de module meegeven, wordt de appname gebruikt?
# "this will include... **into the given application namespace**
# er is ook een "instance namespace"
# verschil?
# instance namespace is voor wanneer meerdere instanties van één app aanwezig zijn in een project
# niet het geval voor xchk, dus niet te veel zorgen over maken
# maar lost het probleem nog niet helemaal op
