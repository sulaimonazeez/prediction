from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemap import MyFirstOne,MySecondOne,MyThirdOne,MyFourthOne,MyFifthOne,MySixtyOne

sitemaps = {
    'country': MyFirstOne,
    'match': MySecondOne,
    'daily': MyThirdOne,
    "tennis_country": MyFourthOne,
    "tennis_match": MyFifthOne,
    "article":MySixtyOne,
}


urlpatterns = [
  path("", views.Home.as_view(), name="home"),
  path("dailyodds", views.Dailys.as_view(), name="daily"),
  path("tennis", views.Tenniss.as_view(), name="tennis"),
  path("article", views.Articles.as_view(), name="article"),
  path("article-capcha/<int:id>", views.ArticleId.as_view(), name="reader"),
  path("<int:id>", views.HomeId.as_view(), name="home_id"),
  path("tennis/<int:id>", views.TennisId.as_view(), name="tennis_id"),
  path("search", views.Search.as_view(), name="search"),
  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]