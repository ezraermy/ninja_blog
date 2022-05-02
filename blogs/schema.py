import graphene
from graphene_file_upload.scalars import Upload
from graphene_django import DjangoObjectType
from .models import Blog, BlogImage

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        fields ='__all__'

class BlogImageType(DjangoObjectType):
    class Meta:
        model = BlogImage


class Query(graphene.ObjectType):
    all_blogs = graphene.List(BlogType)
    blog = graphene.Field(BlogType, blog_id=graphene.ID())
    image = graphene.Field(BlogImageType, blog_id=graphene.ID())
   
    def resolve_all_blogs(root, info, **kwargs):
        return Blog.objects.all()

    def resolve_blog(root, info, blog_id):
        return Blog.objects.get(id=blog_id)
    
    
class CreateBlog(graphene.Mutation):
    id: graphene.ID()
    title: graphene.String()
    author: graphene.String()
    body: graphene.String()
    data_published: graphene.String()
 
    
    class Arguments:
        title = graphene.String()
        author = graphene.String()
        body = graphene.String()
        data_published = graphene.String() 
    
    blog = graphene.Field(BlogType)
    
    @staticmethod
    def mutate(root, info, title, author, body, data_published, photo):
        blog_instance = Blog.objects.create(
            title = title,
            author = author,
            body = body,
            data_published = data_published
        )
        blog_instance.save()
        return CreateBlog(blog=blog_instance)

#file upload 
class CreateBlogImage(graphene.Mutation):
    class Arguments:
        image = Upload(required=True)
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, image, **data):
        image_file = image
        id = data.get('id')
        return CreateBlogImage(image_file=image_file)



class UpdateBlog(graphene.Mutation):
    
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        author = graphene.String()
        body = graphene.String()
        data_published = graphene.String() 

    blog = graphene.Field(BlogType)


    def mutate(root, info, title, author, body, data_published, id):
        blog_instance = Blog.objects.get(pk = id)
        blog_instance.title = title if title is not None else blog_instance.title
        blog_instance.author = author if author is not None else blog_instance.author
        blog_instance.body = body if body is not None else blog_instance.body
        blog_instance.data_published = data_published if data_published is not None else blog_instance.data_published
        blog_instance.save()
        return UpdateBlog(blog=blog_instance)

class DeleteBlog(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    blog = graphene.Field(BlogType)
    
    @staticmethod
    def mutate(root, info, id):
        blog_instance = Blog.objects.get(pk=id)
        blog_instance.delete()



class Mutation(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    update_blog = UpdateBlog.Field()
    delete_blog = DeleteBlog.Field()
    create_image = CreateBlogImage.Field()
   



schema = graphene.Schema(query=Query, mutation=Mutation)