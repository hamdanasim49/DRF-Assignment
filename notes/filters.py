from notes.models import Notes
from django_filters import rest_framework as filters


class NotesArchiveFilter(filters.filterset):
    archive = filters.BooleanFilter(method="filter_is_archive")
    print("In file filter***")

    class Meta:
        model = Notes
        fields = [
            "archive",
        ]

    def filter_is_archive(self, queryset, name, value):
        if value:
            print(value)
            return queryset.filter(archive=True)
        else:
            return queryset.filter(archive=False)
