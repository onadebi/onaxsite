from django.db import models;


class PortfolioCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, max_length=250);
    created_by: str = models.CharField(max_length=100, default='system', null=False);
    updated_by: str = models.CharField(max_length=100, default='system', null=False);
    isActive = models.BooleanField(default=True);
    isDeleted: bool = models.BooleanField(default=False);
    image_path: str = models.CharField(max_length=250, null=True);
    url_path: str = models.CharField(max_length=250, null=True);
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'PortfolioCategory';

    def __str__(self):
        return f"{self.id} - {self.category_title}"
    
class PortfolioSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(PortfolioCategory, on_delete=models.RESTRICT, related_name='fkey_sub_categories',db_column='category_id')
    sub_category_title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, max_length=250);
    created_by: str = models.CharField(max_length=100, null=False, default='system');
    updated_by: str = models.CharField(max_length=100, null=False, default='system');
    isActive = models.BooleanField(default=True);
    isDeleted: bool = models.BooleanField(default=False);
    image_path: str = models.CharField(max_length=250, null=True);
    url_path: str = models.CharField(max_length=250, null=True);
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'PortfolioSubCategory';

    def __str__(self):
        return f"{self.id} - {self.sub_category_title}"