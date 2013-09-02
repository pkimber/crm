from django.contrib.auth.models import User
from django.db import models

import reversion

from base.model_utils import TimeStampedModel


class Contact(TimeStampedModel):
    """ Contact """
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    slug = models.SlugField()
    url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True)
    mail = models.EmailField(blank=True)
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['slug']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __unicode__(self):
        return unicode('{}'.format(self.name))

reversion.register(Contact)


class Priority(models.Model):
    """Level 0 will exclude the ticket from normal reminder lists"""
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField()

    class Meta:
        ordering = ['-level', 'name']
        verbose_name = 'Priority'
        verbose_name_plural = 'Priorities'

    def __unicode__(self):
        return unicode('{}'.format(self.name))

reversion.register(Priority)


class Ticket(TimeStampedModel):
    """ Contact """
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.ForeignKey(Priority)
    date_due = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __unicode__(self):
        return unicode('{}'.format(self.name))

reversion.register(Ticket)
