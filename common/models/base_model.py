from django.db import models;

class BaseModel(models.Model):
    """Base model for all models in the application"""
    id = models.AutoField(primary_key=True, db_column='id', name='id');
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
    is_deleted = models.BooleanField(default=False);
    is_active = models.BooleanField(default=True);
