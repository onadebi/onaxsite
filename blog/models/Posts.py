# from django.
from django.db import models;
from django.utils import timezone;


class Posts(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', name='id');
    post_title: str = models.CharField(max_length=255, null=False, blank=False, unique=True);
    post_content: str = models.TextField(max_length=1500, null=False, blank=False, default='');
    post_summary: str = models.CharField(max_length=350, null=False, blank=False);
    featured_image: str = models.CharField(max_length=255, null=True, blank=True, default='default_featured_image.jpg');
    
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
        super(Posts, self).save(*args, **kwargs)
        # return self.id