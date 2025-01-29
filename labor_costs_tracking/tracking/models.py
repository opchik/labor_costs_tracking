from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class Project(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    def calculate_profit_or_loss(self):
        labor_costs = sum(
            log.hours_spent * log.user.salary
            for log in self.work_logs.all()
        )
        additional_expenses = 0
        return self.amount - labor_costs - additional_expenses


class WorkLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_logs')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='work_logs')
    date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    task = models.CharField(max_length=255)
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.full_name} - {self.project.name} - {self.date}"

    def calculate_labor_costs(self):
        return self.hours_spent * self.user.salary

