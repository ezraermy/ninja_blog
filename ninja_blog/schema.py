import graphene
import blogs.schema 
import users.schema

class Query(blogs.schema.Query, users.schema.Query, graphene.ObjectType):
    pass

class Mutation(blogs.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass 

schema = graphene.Schema(query=Query, mutation=Mutation)