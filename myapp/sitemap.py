from django.contrib import sitemaps
from .models import Country, Match,Daily,MyCountry,MyMatch,Article

class MyFirstOne(sitemaps.Sitemap):
  changefreq = "weekly"
  priority = 0.9
  
  def items(self):
    return Country.objects.all()
  
  def lastmod(self, obj):
    return obj.country_image
    

class MySecondOne(sitemaps.Sitemap):
  changefreq = "weekly"
  priority = 0.9
  
  def items(self):
    return Match.objects.all()
    
  def lastmod(self, obj):
    return obj.start
    
    
class MyThirdOne(sitemaps.Sitemap):
  changefreq = "weekly"
  priority = 0.9
  
  def items(self):
    return Daily.objects.all()
    
  def lastmod(self, obj):
    return obj.my_prediction
    
class MyFourthOne(sitemaps.Sitemap):
  changefreq = "weekly"
  priority = 0.9
  
  def items(self):
    return MyCountry.objects.all()
    
  def lastmod(self, obj):
    return obj.country_image
    
    
class MyFifthOne(sitemaps.Sitemap):
  changefreq = "weekly"
  priority = 0.9
  
  def items(self):
    return MyMatch.objects.all()
    
  def lastmod(self, obj):
    return obj.start
    
    
class MySixtyOne(sitemaps.Sitemap):
  changefreq = "weekly"
  priority = 0.9
  
  def items(self):
    return Article.objects.all()
    
  def lastmod(self, obj):
    return obj.publish_date