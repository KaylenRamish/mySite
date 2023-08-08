from webapp.models import BlogPost

#first blog post
post1 = BlogPost(title="First Post", body="This is my first blog post.", signature="John Doe")
post1.save()

#second blog post
post2 = BlogPost(title="Second Post", body="This is my second blog post.", signature="Jane Smith")
post2.save()
