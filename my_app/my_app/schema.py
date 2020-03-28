import graphene

from clients.schema import Query, MyMutations


class Query(Query, graphene.ObjectType):
    pass

class Mutation(MyMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
