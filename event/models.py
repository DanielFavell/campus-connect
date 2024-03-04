from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    # Name of the event
    title = models.CharField(max_length=200, unique=True)
    # URL field
    slug = models.SlugField(max_length=200, unique=True)
    # The date the event is held
    event_host_date = models.DateTimeField()
    # Where the event is held
    venue = models.CharField(max_length=200)
    # Organizer is the user account that created event post
    organizer = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="event_posts")
    # Cloudinary image field
    featured_image = CloudinaryField('image', default='placeholder')
    # Main content
    content = models.TextField()
    # Max people event can hold
    max_people = models.IntegerField(null=True)
    # Attendance tracker for users
    attendance_count = models.IntegerField(default=0)
    # When was the event posted
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on", "organizer"]

    # Returns title of post in admin panel instead of "Object(n)"
    def __str__(self):
        return f"{self.title} | posted by {self.organizer}"