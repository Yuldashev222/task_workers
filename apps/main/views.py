from django.views.generic import TemplateView

from apps.main.models import Department


class MainTemplateView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'departments': Department.objects.filter(parent__isnull=True).prefetch_related(
            'workers',

            'children',
            'children__workers',

            'children__children',
            'children__children__workers',

            'children__children__children',
            'children__children__children__workers',

            'children__children__children__children',
            'children__children__children__children__workers',

            'children__children__children__children__children',
            'children__children__children__children__children__workers',
        ).order_by('id')
    }
