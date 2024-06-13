# from django.
from django.db import models;


class Posts(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', name='id');
    post_title: str = models.CharField(max_length=255, null=False, blank=False, unique=True);
    post_content: str = models.TextField(max_length=1500, null=False, blank=False, default='');
    
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
    is_deleted = models.BooleanField(default=False);
    is_active = models.BooleanField(default=True);
    author = models.CharField(max_length=50, null=False,default='Onaefe')
    # author = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='author_id', name='author_id');

    class Meta:
        db_table = 'Post'
        
    def __str__ (self):
        return self.post_title;