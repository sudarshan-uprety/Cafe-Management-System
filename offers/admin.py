from django.contrib import admin
from offers.models import DrinkOffers,FoodOffers,HukkaOffers,BeakeryOffers
# Register your models here.

class FoodOffersAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_rate','price','offer_price']

class DrinkOfferAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_rate','price','offer_price']

class HukkaOfferAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_rate','price','offer_price']

class BeakeryOfferAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_rate','price','offer_price']

admin.site.register(FoodOffers,FoodOffersAdmin)
admin.site.register(DrinkOffers,DrinkOfferAdmin)
admin.site.register(HukkaOffers,HukkaOfferAdmin)
admin.site.register(BeakeryOffers,BeakeryOfferAdmin)

