from django.contrib import admin
from .models import Country, Match, Daily, MyMatch, MyCountry, Article

admin.site.register(Country)
admin.site.register(Match)
admin.site.register(Daily)
admin.site.register(MyMatch)
admin.site.register(MyCountry)
admin.site.register(Article)
