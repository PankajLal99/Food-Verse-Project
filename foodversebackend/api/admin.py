from django.contrib import admin
# Register your models here.
from .models import *

class MarketAreaClusterAdmin(admin.ModelAdmin):
    list_display = ('title','slug','location')
    search_fields = ['title','location']

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug',)
    search_fields = ['title',]

class BrandAdmin(admin.ModelAdmin):
    list_display = ('market_area_cluster','get_brands_name','license_number','location','serving_options',)
    search_fields = ['market_area_cluster','location','serving_options']

class BrandMenuAdmin(admin.ModelAdmin):
    list_display = ('brand','item_name','item_category','item_selling_price','item_promotion_value')
    search_fields = ['brand','item_name','item_category']

admin.site.register(MarketAreaCluster,MarketAreaClusterAdmin)
admin.site.register(MenuCategory,MenuCategoryAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(BrandMenu,BrandMenuAdmin)