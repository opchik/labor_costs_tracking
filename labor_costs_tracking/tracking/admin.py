from django.contrib import admin
from .models import (User, Project, WorkLog, 
					Department, Client, Position, Task)

admin.site.register(User)
admin.site.register(Project)
admin.site.register(WorkLog)
admin.site.register(Department)
admin.site.register(Client)
admin.site.register(Position)
admin.site.register(Task)
