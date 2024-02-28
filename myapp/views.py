from django.views.generic import ListView,DetailView, View
from django.http import Http404
from .models import Country, Match, Daily, MyMatch, MyCountry, Article
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages


class Home(ListView):
    model = Country
    template_name = 'home.html'
    context_object_name = 'matches_by_country'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countries_with_matches = {}

        for country in Country.objects.all():
            matches = Match.objects.filter(country=country)
            if matches.exists():
                countries_with_matches[country] = matches

        context[self.context_object_name] = countries_with_matches
        return context


class Dailys(ListView):
  model = Daily
  template_name = "daily_odds.html"
  context_object_name = "daily_odds"
  
class Tenniss(ListView):
  model = MyMatch
  template_name = "tennis.html"
  context_object_name = "tennis_prediction"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countries_with_matches = {}

        for country in MyCountry.objects.all():
            matches = MyMatch.objects.filter(country=country)
            if matches.exists():
                countries_with_matches[country] = matches

        context[self.context_object_name] = countries_with_matches
        return context
        
        
class Articles(ListView):
  model = Article
  template_name = "article.html"
  context_object_name = "my_article"

class ArticleId(DetailView):
    model = Article
    template_name = 'article_id.html'
    context_object_name = 'my_article_id'
    pk_url_kwarg = 'id'
    
    def get_object(self, queryset=None):
        try:
            queryset = self.get_queryset()  # Get the queryset for the view
            # Get the object using the primary key from the URL kwargs
            obj = queryset.get(pk=self.kwargs.get(self.pk_url_kwarg))
            return obj
        except Article.DoesNotExist:
            # Redirect to another URL if the object does not exist
            return redirect("/")
            
            
            
            
class HomeId(DetailView):
    model = Match
    template_name = 'home-detail.html'
    context_object_name = 'matches'
    pk_url_kwarg = 'id'
    def get_object(self, queryset=None):
        try:
            queryset = self.get_queryset()
            obj = queryset.get(pk=self.kwargs.get(self.pk_url_kwarg))
            return obj
        except Match.DoesNotExist:
            # redirect me to another url
            return redirect("/")
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by("-publish_date")[0:5]
        return context
        
        
class TennisId(DetailView):
    model = MyMatch
    template_name = 'tennis_id.html'
    context_object_name = 'matches'
    pk_url_kwarg = 'id'
    
    def get_object(self, queryset=None):
        try:
            queryset = self.get_queryset()
            obj = queryset.get(pk=self.kwargs.get(self.pk_url_kwarg))
            return obj
        except MyMatch.DoesNotExist:
            # redirect me to another url
            return redirect("/")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by("-publish_date")[0:5]
        return context
            
            
class Search(View):
  def post(self, request):
    query = request.POST.get("q")
    if query and len(query) >= 2:
      result = Match.objects.filter(Q(home_team__icontains=query) | Q(away_team__icontains=query))
      if result:
        countries_with_matches = {}
        for country in Country.objects.all():
            matches = result.filter(country=country)
            if matches.exists():
              countries_with_matches[country] = matches
        messages.success(request, "Matches found for the query")
        return render(request, "search_result.html", {"matches_by_country": countries_with_matches, "query": query})
      else:
        countries_with_matches = {}
        for country in Country.objects.all():
            matches = Match.objects.filter(country=country)
            if matches.exists():
                countries_with_matches[country] = matches
        messages.error(request, "No matches found for the query")
        return render(request, "search_result.html", {"countries_with_matches":countries_with_matches})
    else:
      messages.error(request, "Query length should be at least 2 characters")
      return redirect("/")