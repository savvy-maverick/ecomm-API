from django.contrib import admin
from .models import Cart, CartItem, User, Category, Product, ProductRating, Review, Wishlist
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
admin.site.register(User, CustomUserAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'featured')

admin.site.register(Product, ProductAdmin )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image')

admin.site.register(Category, CategoryAdmin)

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review)
admin.site.register(ProductRating)
admin.site.register(Wishlist)


 
