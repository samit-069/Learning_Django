#username: admin password: admin
from django.contrib import admin
from .models import Expense

class ExpenseAdmin (admin.ModelAdmin):
    fields = ["title","amount","category"]
    readonly_fields = ["date_added"]

    list_display = ('id', 'title', 'amount', 'category', 'date_added')

    list_filter = ('category','date_added')

    search_fields = ('title', 'id')
# Register your models here.
admin.site.register(Expense, ExpenseAdmin)

