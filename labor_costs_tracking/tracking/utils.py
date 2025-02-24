from django.db.models import Count

from .models import *

menu = [{'title': "Профиль", 'url_name': 'home'},
        {'title': "Проекты", 'url_name': 'project_list'},
        {'title': "Трудозатраты", 'url_name': 'worklog_list'},
        {'title': "Сводка", 'url_name': 'final_list'},
]

class DataMixin:
    paginate_by = 9

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        context['menu'] = user_menu
        return context
