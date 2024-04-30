from django.contrib import admin

from .models.ContactOptions import ContactOptions, Messages;
from .models.PortfolioCategory import PortfolioCategory, PortfolioSubCategory;

# Register your models here.
admin.site.register([PortfolioCategory, PortfolioSubCategory, ContactOptions, Messages]);