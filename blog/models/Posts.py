# from django.
from django.db import models;
from django.utils import timezone;
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField;

import re;
import uuid;
import base64

# Generate a random UUID
guid = uuid.uuid4()
# Convert UUID to bytes and encode it using base64
encoded_guid = base64.urlsafe_b64encode(guid.bytes)
# Decode bytes to string and optionally remove padding
short_guid = encoded_guid.decode('utf-8').rstrip('=')


class PostsManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        if queryset.exists() and queryset is not None:
            for post in queryset:
                post.post_summary = re.sub(r'[<>]', '', post.post_summary)
        return queryset

class Posts(models.Model):

    # overide of objects manager
    objects = PostsManager();

    id = models.AutoField(primary_key=True, db_column='id', name='id');
    post_title: str = models.CharField(max_length=255, null=False, blank=False, unique=False, verbose_name='Post Title');
    # post_content: str = models.TextField(max_length=1500, null=False, blank=False, default='');
    post_content = RichTextUploadingField(verbose_name='Post Content', default='---');
    post_summary: str = models.CharField(max_length=350, null=False, blank=False, default='------');
    # featured_image: str = models.CharField(max_length=255, null=True, blank=True, default='default_featured_image.jpg');
    post_image = models.ImageField(upload_to='',max_length=255, null=True, blank=True,verbose_name='Post Image',default='default_featured_image.jpg');
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False,default='------');
    categories = models.CharField(max_length=255, choices=[('software-development', 'Software Development'), ('machine-learning-ai', 'Machine Learning/AI'), ('freebies', 'Freebies'), ('programming-languages', 'Programming Languages'), ('Tutorials', 'tutorials')], default='software-development');

    created_at = models.DateTimeField(auto_now=True);
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
        self.post_summary = remove_html_tags(self.post_content[:350]);
        self.slug = f'{self.post_title.replace(" ", "-").lower()}-{short_guid}'
        super(Posts, self).save(*args, **kwargs)
        # return self.id


#region helpers
def remove_html_tags(text):
     # Replace </p> and <br/> tags with new lines
    text = re.sub(r'</p>', '&#10;', text)
    text = re.sub(r'<br\s*/?>', '&#10;', text)
    
    # Remove all other HTML tags
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
#endregion