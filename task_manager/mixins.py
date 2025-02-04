from django.views import generic

from task_manager.forms import SearchForm


class NameSearchMixin(generic.ListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("query")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search_form"] = SearchForm()
        return context
