from django.contrib import admin
from finance.models import Transaction, Goal
from import_export import resources
from import_export.admin import ExportMixin

# Register your models here.

class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        fields = ('date','title','amount','transaction_type')

class TransactionAdmin(ExportMixin,admin.ModelAdmin):
    resource_class = TransactionResource
    list_display = ('date','title','amount','transaction_type')
    search_fields = ('title',)

admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Goal)