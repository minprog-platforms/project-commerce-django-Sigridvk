from django.contrib import admin

from .models import *

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "starting_bid", "category")
# Register your models here.
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid)
admin.site.register(Comment)