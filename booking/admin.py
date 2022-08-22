from django.contrib import admin
from .models import Ticket, TicketType, PurchaseHistory, Booking, PayMethod, Order


class TicketEditAdmin(admin.ModelAdmin):
    readonly_fields = ("price",)
    exclude = ("price",)


class PurchaseHistoryEditAdmin(admin.ModelAdmin):
    readonly_fields = ("total_costs",)
    exclude = ("total_costs",)


admin.site.register(Ticket, TicketEditAdmin)
admin.site.register(PurchaseHistory, PurchaseHistoryEditAdmin)
admin.site.register((TicketType, Booking, PayMethod, Order))
