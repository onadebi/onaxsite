from django.contrib import admin

from .models.ContactOptions import ContactOptions, ContactMessages;
from .models.PortfolioCategory import PortfolioCategory, PortfolioSubCategory;

# Register your models here.
admin.site.register([PortfolioCategory, PortfolioSubCategory, ContactOptions, ContactMessages]);