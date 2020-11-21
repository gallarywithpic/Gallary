from django.views.generic import TemplateView, ListView
from .models import Pictures
from django.db.models import Q

 
class HomePageView(TemplateView):
    template_name = 'index.html'
 

class SearchResultsView(ListView):
    model = Pictures
    template_name = 'search_results.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Pictures.objects.filter(
            Q(name__icontains=query) | Q(culka__icontains=query)
        )
        return object_list