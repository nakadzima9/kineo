from django.db import models
from django.conf import settings
from cinema.models import ShowTime, Seat


class Ticket(models.Model):
    ticket_type = models.ForeignKey(
        "TicketType", on_delete=models.PROTECT, verbose_name="Тип билета"
    )
    showtime = models.ForeignKey(
        ShowTime, on_delete=models.PROTECT, verbose_name="Время показа"
    )
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT, verbose_name="Место")
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name="Цена")

    def save(self, *args, **kwargs):
        if self.ticket_type.name.lower() == "adult":
            self.price = (
                self.showtime.movie_format.price_for_adult
                + self.showtime.room_format.price_for_adult
                + self.showtime.price_for_adult
            )
            super(Ticket, self).save(*args, **kwargs)
        elif self.ticket_type.name.lower() == "child":
            self.price = (
                self.showtime.movie_format.price_for_child
                + self.showtime.room_format.price_for_child
                + self.showtime.price_for_child
            )
            super(Ticket, self).save(*args, **kwargs)
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return f"Ticket: {self.ticket_type} seat: {self.seat.seat_number}"

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"


class TicketType(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Тип билета")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Тип билетов"


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец"
    )
    ticket = models.ForeignKey("Ticket", on_delete=models.CASCADE, verbose_name="Билет")
    when_reserved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Бронирование"


class Order(models.Model):
    purchase_history = models.ForeignKey(
        "PurchaseHistory", on_delete=models.PROTECT, verbose_name="История покупок"
    )
    ticket = models.OneToOneField(
        "Ticket", on_delete=models.CASCADE, verbose_name="Билет"
    )
    pay_method = models.ForeignKey(
        "PayMethod", on_delete=models.PROTECT, verbose_name="Метод оплаты"
    )

    # def save(self,*args, **kwargs):
    #     old_pk= self.purchase_history.pk
    #     super(Order, self).save(*args, **kwargs)
    #     PurchaseHistory.objects.get(pk=self.purchase_history.pk).save()

    def __str__(self):
        return self.purchase_history.owner.email

    class Meta:
        verbose_name_plural = "Заказ"


class PurchaseHistory(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="Владелец"
    )
    total_costs = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Общая стоимость"
    )

    # def save(self, *args, **kwargs):
    #     if self.checker():
    #         self.total_costs=0
    #         buff = PurchaseHistory.objects.get(pk=self.pk).order_set.all()
    #         for order in buff:
    #             self.total_costs += order.ticket.price
    #         super(PurchaseHistory, self).save(*args, **kwargs)
    #     else:
    #         super(PurchaseHistory, self).save(*args, **kwargs)
    #
    # def checker(self):
    #     try:
    #         PurchaseHistory.objects.get(pk=self.pk)
    #         return True
    #     except PurchaseHistory.DoesNotExist:
    #         return False

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "История покупок"


class PayMethod(models.Model):
    name = models.CharField(max_length=255, verbose_name="Метод оплаты")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Метод оплаты"
