from django.db import models


class TicketBusiness(models.Model):
    ticket_code = models.CharField(max_length=255, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ticket_business'
        app_label = 'tickets'


class TicketGovernment(models.Model):
    ticket_code = models.CharField(max_length=255, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ticket_government'
        app_label = 'tickets'


class TicketInfo(models.Model):
    ticket_code = models.CharField(max_length=255, blank=True, null=True)
    ticket_status = models.IntegerField(blank=True, null=True)
    ticket_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ticket_info'
        app_label = 'tickets'