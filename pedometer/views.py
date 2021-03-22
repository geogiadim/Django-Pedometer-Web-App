from django.shortcuts import render
from .forms import LogStepsForm, ChartDateForm
from .models import Pedometer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model


User = get_user_model()


# view for the home page
def home_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "pedometer/home.html", my_context)


# view for the log page
def log_steps_view(request, *args, **kwargs):
    form = LogStepsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LogStepsForm(None)
    context = {
        "form": form
    }
    return render(request, "pedometer/log.html", context)


# view for the history page
def history_steps_view(request, *args, **kwargs):
    queryset = Pedometer.objects.all()
    my_context = {
        'object_list': queryset
    }
    return render(request, "pedometer/history.html", my_context)


# view for the charts page
def chart_steps_view(request, *args, **kwargs):
    form = ChartDateForm()
    my_context = {
        "form": form
    }

    if request.method == "POST":
        form = ChartDateForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            print(form.cleaned_data)
            my_context['from_date'] = str(from_date)
            my_context['to_date'] = str(to_date)
        else:
            print(form.erros)
    print(my_context)
    return render(request, "pedometer/chart.html", my_context)


# Rest Api for chart's data
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        from_date = None
        to_date = None
        if 'from' in self.request.query_params.keys():
            from_date = self.request.query_params.get('from')

        if 'to' in self.request.query_params.keys():
            to_date = self.request.query_params.get('to')

        if to_date and from_date:
            queryset = Pedometer.objects.filter(date__range=[from_date, to_date]).all()
        else:
            queryset = Pedometer.objects.all()

        labels = [item.date for item in queryset]
        default_items = [item.steps for item in queryset]

        #list = [item.date for item in queryset if item.steps > 100]

        dict = {str(item.date): item.steps for item in queryset}

        data = {
            'labels': labels,
            "default": default_items,
            'dict': dict
        }
        return Response(data)
