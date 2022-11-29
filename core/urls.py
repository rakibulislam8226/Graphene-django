from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url


GraphQLView.graphiql_template = "graphene_graphiql_explorer/graphiql.html"
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))), # prevents API clients from POSTing to the graphql endpoint.
    # path("graphql/", GraphQLView.as_view(graphiql=True)), #without restrict any permission
    url(r"^graphql/$", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
