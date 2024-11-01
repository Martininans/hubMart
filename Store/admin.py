from django.contrib import admin

from .models import Product, Collection

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "description", "collections"]
    list_per_page = 10
    list_editable = ["price", "description"]
    search_fields = ('title', 'description')

    @admin.display(ordering='inventory')
    def inventory_status(self,product: Product):
        if product.inventory < 20:
            return 'Low'
        return 'Ok'

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "id", 'productCount']
    list_per_page = 10


    def productCount(self, collection: Collection):
        return collection.product_set.count()
