from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import DataMixin
from .models import Project, WorkLog, User
from .forms import (ProjectForm, WorkLogForm, RegisterUserForm,
                    LoginUserForm, UserProfileForm, AdditionalCostsForm)


class ProjectList(LoginRequiredMixin, DataMixin, ListView):
    model = Project
    template_name = 'tracking/project_list.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.resolver_match.url_name == 'project_list':
            c_def = self.get_user_context(title="Список проектов")
        else:
            c_def = self.get_user_context(title="Итоговый список")
            for project in context['items']:
                project.profit_or_loss = project.calculate_profit_or_loss()
        return {**context, **c_def}

    def get_queryset(self):
        return Project.objects.all()


class WorkLogList(LoginRequiredMixin, DataMixin, ListView):
    model = WorkLog
    template_name = 'tracking/worklog_list.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Трудозатраты")
        return {**context, **c_def}

    def get_queryset(self):
        return WorkLog.objects.filter(user=self.request.user)


class AddProject(LoginRequiredMixin, DataMixin, CreateView):
    form_class = ProjectForm
    template_name = 'tracking/add_item.html'
    success_url = reverse_lazy('project_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление проекта")
        return {**context, **c_def}

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class AddWorkLog(LoginRequiredMixin, DataMixin, CreateView):
    form_class = WorkLogForm
    template_name = 'tracking/add_item.html'
    success_url = reverse_lazy('worklog_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление трудозатрат")
        return {**context, **c_def}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Home(LoginRequiredMixin, DataMixin, View):
    template_name = 'tracking/profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        form = UserProfileForm(instance=user)
        context = self.get_user_context()
        c_def = {
            'form': form,
            'title': "Профиль",
            'profile': user
        }
        return render(request, self.template_name, {**context, **c_def})

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        return self.get(request, *args, **kwargs)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'tracking/auth.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return {**context, **c_def}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'tracking/auth.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ProjectStatistics(LoginRequiredMixin, DataMixin, DetailView):
    model = Project
    template_name = 'tracking/project_statistics.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        work_logs = project.work_logs.all()
        aggregated_data = {}
        for log in work_logs:
            if log.user.full_name in aggregated_data:
                aggregated_data[log.user.full_name]["hours_spent"] += log.hours_spent
            else:
                aggregated_data[log.user.full_name] = {"hours_spent": log.hours_spent, "salary": log.user.salary}
        work_logs = [
            {
                "name": name, 
                "hours_spent": data["hours_spent"], 
                "salary": data["salary"],
                "labor_cost":  data["hours_spent"]*data["salary"]
            }
            for name, data in aggregated_data.items()
        ]
        labor_costs = sum(
            log["hours_spent"] * log["salary"]
            for log in work_logs
        )
        profit_or_loss = project.amount - labor_costs - project.additional_costs
        context['work_logs'] = work_logs
        context['labor_costs'] = labor_costs
        context['additional_costs'] = project.additional_costs
        context['profit_or_loss'] = profit_or_loss
        context.update(self.get_user_context(title="Статистика по проекту"))
        return context

    def get_queryset(self):
        return Project.objects.all()



class AddAdditionalCosts(LoginRequiredMixin, DataMixin, UpdateView):
    model = Project
    form_class = AdditionalCostsForm
    template_name = 'tracking/additional_costs.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Project, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('project_statistics', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        return super().form_valid(form)
