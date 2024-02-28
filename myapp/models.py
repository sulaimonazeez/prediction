from django.db import models

class Country(models.Model):
  country_name = models.CharField(max_length=255)
  country_image = models.ImageField(upload_to="static")
  
  def __str__(self):
    return self.country_name
  
class Match(models.Model):
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  home_team = models.CharField(max_length=1000)
  away_team = models.CharField(max_length=1000)
  home_logo = models.ImageField(upload_to="static")
  away_logo = models.ImageField(upload_to="static")
  prediction = models.TextField()
  start = models.DateTimeField()
  stadiu_used = models.CharField(max_length=1000)
  
  def __str__(self):
    return home_team + " vs " + away_team
    
    
class Daily(models.Model):
  odd = models.ForeignKey(Match, on_delete=models.CASCADE)
  my_prediction = models.CharField(max_length=500)
  
  def __str__(self):
    return self.my_prediction
    

class MyCountry(models.Model):
  country_name = models.CharField(max_length=255)
  country_image = models.ImageField(upload_to="static")
  
  def __str__(self):
    return self.country_name
  
class MyMatch(models.Model):
  country = models.ForeignKey(MyCountry, on_delete=models.CASCADE)
  home_team = models.CharField(max_length=1000)
  away_team = models.CharField(max_length=1000)
  home_logo = models.ImageField(upload_to="static")
  away_logo = models.ImageField(upload_to="static")
  prediction = models.TextField()
  start = models.DateTimeField()
  
  def __str__(self):
    return home_team + " vs " + away_team
    
class Article(models.Model):
  title = models.CharField(max_length=1000)
  image = models.ImageField(upload_to="static")
  body = models.TextField()
  publish_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title
  