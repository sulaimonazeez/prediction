from . import views
from django.urls import path


urlpatterns = [
  path("", views.Home.as_view(), name="home"),
  path("dailyodds", views.Dailys.as_view(), name="daily"),
  path("tennis", views.Tenniss.as_view(), name="tennis"),
  path("article", views.Articles.as_view(), name="article"),
  path("article-capcha/<int:id>", views.ArticleId.as_view(), name="reader"),
  path("<int:id>", views.HomeId.as_view(), name="home_id"),
  path("tennis/<int:id>", views.TennisId.as_view(), name="tennis_id"),
  path("search", views.Search.as_view(), name="search"),
]