import graphene 
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required
import graphql_jwt

# Create your type here
User = get_user_model() #create

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password', )

# Create query class here
class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    current_user = graphene.Field(UserType)

    def resolve_all_users (root, info):
        return User.objects.all()

    @login_required
    def resolve_current_user(root, info):
        user = info.context.user 
        return user

# Create your mutation here 
class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
    
    user = graphene.Field(UserType)

    def mutate(root, info, username, password, email):
        user = User(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
