from django.views import generic
from django.db.models import (
    Case,
    When,
    Value,
    IntegerField,
    Q
)

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


class ToDoItemSearchMixin(generic.ListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("query")
        if search_query:
            queryset = (
                queryset.annotate(
                    relevance=Case(
                        When(
                            Q(name__icontains=search_query)
                            & Q(description__icontains=search_query),
                            then=Value(15),
                        ),
                        When(name__icontains=search_query, then=Value(10)),
                        When(description__icontains=search_query, then=Value(5)),
                        default=Value(0),
                        output_field=IntegerField(),
                    )
                )
                .filter(relevance__gt=0)
                .order_by("-relevance")
            )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search_form"] = SearchForm()
        return context
