# -*- encoding: utf-8 -*-
# Copyright P. Christeas <xrg@hellug.gr> 2012
# Only a few rights reserved

from django.db import models
from django.utils.translation import ugettext_lazy as _
from dynamic_search.api import register

class Partner(models.Model):
    name = models.CharField(max_length=128, unique=True)
    active = models.BooleanField(verbose_name=_("active"), default=False)
    web = models.CharField(max_length=128, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    # category = 

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("contact"))
    partner = models.ForeignKey(Partner, db_index=True)
    address = models.TextField(blank=True, null=True)
    active = models.BooleanField(verbose_name=_("active"), default=False)
    phone1 = models.CharField(max_length=32, verbose_name=_("phone"), blank=True, null=True)
    phone2 = models.CharField(max_length=32, verbose_name=_("phone 2"), blank=True, null=True)


    def __unicode__(self):
        return self.name

class Location(models.Model):
    """
    
        The usage is modelled after the OpenERP values.
        inventory is a virtual location, used to correct stock levels
    """
    name = models.CharField(max_length=32, verbose_name=_("name"))
    address = models.TextField(null=True, blank=True, verbose_name=_(u'address'))
    
    phone_number1 = models.CharField(max_length=32, null=True, blank=True, verbose_name=_(u'phone number'))
    phone_number2 = models.CharField(max_length=32, null=True, blank=True, verbose_name=_(u'phone number'))
    usage = models.CharField(max_length=32, verbose_name=_("location type"),
            choices=[('customer','Customer'), ('procurement', 'Procurement'), ('internal', 'Internal'),
                    ('inventory', 'Inventory'), ('supplier', 'Supplier Location')])

    class Meta:
        ordering = ['name']
        verbose_name = _(u"location")
        verbose_name_plural = _(u"locations")

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('location_view', [str(self.id)])

class Supplier(Partner):
    #TODO: Contact, extension
    vat_number = models.CharField(max_length=32, null=True, blank=True, verbose_name=_("VAT number"))

    class Meta:
        ordering = ['name']
        verbose_name = _(u"supplier")
        verbose_name_plural = _(u"suppliers")


    @models.permalink
    def get_absolute_url(self):
        return ('supplier_view', [str(self.id)])

register(Location, _(u'locations'), ['name', 'address_line1', 'address_line2', 'address_line3', 'address_line4', 'phone_number1', 'phone_number2'])
register(Supplier, _(u'supplier'), ['name', 'address_line1', 'address_line2', 'address_line3', 'address_line4', 'phone_number1', 'phone_number2', 'notes'])


#eof