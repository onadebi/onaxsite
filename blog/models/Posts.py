# from django.
from django.db import models;
from django.utils import timezone;
import uuid;
import base64

# Generate a random UUID
guid = uuid.uuid4()
# Convert UUID to bytes and encode it using base64
encoded_guid = base64.urlsafe_b64encode(guid.bytes)
# Decode bytes to string and optionally remove padding
short_guid = encoded_guid.decode('utf-8').rstrip('=')

class Posts(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', name='id');
    post_title: str = models.CharField(max_length=255, null=False, blank=False, unique=False);
    post_content: str = models.TextField(max_length=1500, null=False, blank=False, default='');
    post_summary: str = models.CharField(max_length=350, null=False, blank=False);
    featured_image: str = models.CharField(max_length=255, null=True, blank=True, default='default_featured_image.jpg');
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False);

    created_at = models.DateTimeField(default=timezone.now);
    updated_at = models.DateTimeField(auto_now=True);
    is_deleted = models.BooleanField(default=False);
    is_active = models.BooleanField(default=True);
    is_featured_post = models.BooleanField(default=False);
    author = models.CharField(max_length=50, null=False,default='Onaefe')
    # author = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='author_id', name='author_id');

    class Meta:
        db_table = 'Post'
        
    def __str__ (self):
        return f"[{self.id}]-{self.post_title}"
    

    # override save method
    def save(self, *args, **kwargs):
        self.post_summary = self.post_content[:350]
        self.slug = f'{self.post_title.replace(" ", "-").lower()}-{short_guid}'
        super(Posts, self).save(*args, **kwargs)
        # return self.id