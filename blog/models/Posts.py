from common.models.base_model import BaseModel
from django.db import models;


class Posts(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', name='id');
    post_title: str = models.CharField(max_length=255, null=False, blank=False, unique=True);
    post_content: str = models.TextField(max_length=1500, null=False, blank=False, default='');
    
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
    is_deleted = models.BooleanField(default=False);
    is_active = models.BooleanField(default=True);

    class Meta:
        db_table = 'Posts'