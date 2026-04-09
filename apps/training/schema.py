import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import TrainingSession

class TrainingSessionType(DjangoObjectType):
    class Meta:
        model = TrainingSession
        fields = ("id", "title", "start_time", "end_time", "description")

class Query(graphene.ObjectType):
    trainings = graphene.List(
        TrainingSessionType, 
        start_time=graphene.DateTime(), 
        end_time=graphene.DateTime()
    )
    training = graphene.Field(TrainingSessionType, id=graphene.ID(required=True))

    def resolve_trainings(self, info, start_time=None, end_time=None):
        if not getattr(info.context, 'user', None) or not info.context.user.is_authenticated:
            raise GraphQLError("Authentication credentials were not provided.")
        qs = TrainingSession.objects.all()
        if start_time:
            qs = qs.filter(start_time__gte=start_time)
        if end_time:
            qs = qs.filter(end_time__lte=end_time)
        return qs

    def resolve_training(self, info, id):
        if not getattr(info.context, 'user', None) or not info.context.user.is_authenticated:
            raise GraphQLError("Authentication credentials were not provided.")
        try:
            return TrainingSession.objects.get(pk=id)
        except TrainingSession.DoesNotExist:
            return None
