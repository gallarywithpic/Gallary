from django.views.generic import TemplateView, ListView
 
from .models import Pictures
 
 
class HomePageView(TemplateView):
    template_name = 'index.html'
 
class SearchResultsView(ListView):
    model = Pictures
    template_name = 'search_results.html'