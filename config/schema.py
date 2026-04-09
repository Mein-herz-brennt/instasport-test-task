import graphene
import apps.training.schema

class Query(apps.training.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
