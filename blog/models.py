from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Creating model managers
class PublishedManager(models.Manager):
    def get_queryset(set):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    # Adding a status field
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # Adding a many-to-one relationship
    body = models.TextField()

    # Adding datetime fields
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Adding a status field
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)


    objects = models.Manager()   # The default manager.
    published = PublishedManager() # Our custom manager .  



    # Defining a default sort order
    class Meta:
        ordering = ['-publish']

    # Adding a database index
    indexes = [
        models.Index(fields=['-publish'])
    ]


    '''
        We have also added a __str__() method to the model class. This is the default Python method to
        return a string with the human-readable representation of the object. Django will use this method to
        display the name of the object in many places, such as the Django administration site.
    '''
    def __str__(self):
        return self.title
    