# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _, get_language
from sorl.thumbnail import get_thumbnail
from fs_ref.app.references.util import FLOW_UNITS, COUNTRIES, FILTERING_LEVEL, FLUIDS, VISCOSITY_TYPES
from fs_ref.util import slugify


class Customer(models.Model):
    name = models.CharField(max_length=140, verbose_name=_('name'))
    website = models.URLField(blank=True, verbose_name=_('customer website'))
    industry = models.CharField(max_length=140, blank=True, verbose_name=_('customer industry'))
    country = models.IntegerField(choices=COUNTRIES, verbose_name=_('country'))

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'website': self.website,
            'industry': self.industry,
        }


class Manufacturer(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('name'))
    code = models.CharField(max_length=120, unique=True, verbose_name=_('code'))

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class FilteringModel(models.Model):
    en = models.CharField(max_length=50, verbose_name=_('English'))
    no = models.CharField(max_length=50, verbose_name=_('Norwegian'))
    dk = models.CharField(max_length=50, verbose_name=_('Danish'))
    sv = models.CharField(max_length=50, verbose_name=_('Swedish'))

    class Meta:
        abstract = True
        ordering = ('en',)

    def __unicode__(self):
        if get_language() in self.to_dict():
            return self.to_dict()[get_language()]
        else:
            return self.en

    def to_dict(self):
        return {
            'id': self.id,
            'en': self.en,
            'no': self.no,
            'dk': self.dk,
            'sv': self.sv,
        }


class Market(FilteringModel):
    """
    Model for the data in the filteringform on the front-page
    """
    pass


class Type(FilteringModel):
    """
    Model for the data in the filteringform on the front-page
    """
    pass


class FilterSolution(FilteringModel):
    """
    Model for the data in the filteringform on the front-page
    """
    pass


class Reference(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    slug = models.SlugField(max_length=200, unique=True, editable=False)

    date_created = models.DateTimeField(editable=False)
    date_saved = models.DateTimeField(editable=False)
    created_by = models.ForeignKey(User, related_name='created_reference', editable=False)
    saved_by = models.ForeignKey(User, related_name='saved_reference', editable=False)
    is_approved = models.BooleanField(default=False, verbose_name=_('approved'))
    is_published = models.BooleanField(default=False, verbose_name=_('published'))

    country = models.PositiveIntegerField(choices=COUNTRIES, verbose_name=_('country'))
    market = models.ForeignKey(Market, related_name='references', verbose_name=_('market'))
    type = models.ForeignKey(Type, related_name='references', verbose_name=_('application'))
    filter_solution = models.ForeignKey(FilterSolution, related_name='references', verbose_name=_('filter solution'))
    manufacturer = models.ForeignKey(Manufacturer, related_name='references', verbose_name=_('filter manufacturer'))

    customer = models.ForeignKey(Customer, related_name='references', verbose_name=_('customer'))
    customer_contact = models.CharField(max_length=200, blank=True, verbose_name=_('customer contact'))
    is_customer_public = models.BooleanField(default=False, verbose_name=_('view customer in public'))
    has_borrowed_products_before_purchase = models.BooleanField(verbose_name=_('borrowed products before purchase'))
    salesman = models.ForeignKey(User, null=True, blank=True, verbose_name=_('salesman'))

    date_installed = models.DateField(null=True, blank=True, verbose_name=_('install date'))

    application = models.TextField(verbose_name=_('subtitle'))
    machine = models.CharField(max_length=240, blank=True, verbose_name=_('machine'))
    machine_type = models.CharField(max_length=240, blank=True, verbose_name=_('machine type'))

    fluid = models.CharField(max_length=40, blank=True, verbose_name=_('fluid'))
    fluid_manufacturer = models.CharField(max_length=40, blank=True, verbose_name=_('fluid manufacturer'))
    fluid_type = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('fluid type'))
    filtering_level = models.CharField(max_length=30, blank=True, verbose_name=_('filtering level'))
    filtering_standard = models.IntegerField(blank=True, null=True, choices=FILTERING_LEVEL,
                                             verbose_name=_('filtering standard'))
    flow = models.IntegerField(null=True, blank=True, verbose_name=_('flow'))
    flow_unit = models.IntegerField(default=1, choices=FLOW_UNITS)
    pressure = models.IntegerField(null=True, blank=True, verbose_name=_('pressure (bar)'))
    system_volume = models.IntegerField(null=True, blank=True, verbose_name=_('system volume'))
    temp = models.IntegerField(null=True, blank=True, verbose_name=_('temperature (C)'))
    viscosity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name=_('viscosity'))
    viscosity_type = models.IntegerField(max_length=50, choices=VISCOSITY_TYPES, default=1,
                                         verbose_name=_('viscosity type'))
    cost_reductions = models.CharField(max_length=50, blank=True, verbose_name=_('cost reductions'))

    filter = models.TextField(verbose_name=_('filter'))
    filter_element = models.TextField(blank=True, verbose_name=_('filter element'))

    analysis_before = models.TextField(blank=True, verbose_name=_('analysis before'))
    analysis_after = models.TextField(blank=True, verbose_name=_('analysis after'))

    problem = models.TextField(blank=True, verbose_name=_('problem'))
    solution = models.TextField(blank=True, verbose_name=_('solution'))

    illustration1 = models.ImageField(upload_to='references/illustrations/', null=True, blank=True,
                                      verbose_name=_('illustration 1'),
                                      help_text='This illustration must be at least 800px wide')
    illustration2 = models.ImageField(upload_to='references/illustrations/', null=True, blank=True,
                                      verbose_name=_('illustration 2'))
    illustration3 = models.ImageField(upload_to='references/illustrations/', null=True, blank=True,
                                      verbose_name=_('illustration 3'))

    file = models.FileField(upload_to='references/files/', null=True, blank=True, verbose_name=_('file'))

    class Meta:
        permissions = (
            ("approve_reference", "Can approve references"),
            ("publish_reference", "Can publish references"),
            ("administrate_filters", "Can administrate filters"),
        )
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        from fs_ref.core.auth import get_current_user

        if self.slug is None or self.slug == '':
            self.slug = slugify(self.title)

        if not self.pk:
            self.date_created = datetime.now()
            self.created_by = get_current_user()

        self.date_saved = datetime.now()
        self.saved_by = get_current_user()
        super(Reference, self).save(*args, **kwargs)

    def has_translation(self):
        return bool(self.englishtranslation)

    def to_dict(self):
        dict = {
            'title': self.title,
            'date_created': str(self.date_created),
            'date_saved': str(self.date_saved),
            'market': unicode(self.market),
            'filter_solution': unicode(self.filter_solution),
            'application': self.application,
            'machine': self.machine,
            'machine_type': self.machine_type,
            'filter': self.filter,
            'filter_element': self.filter_element,
            'manufacturer': str(self.manufacturer),
            'is_published': self.is_published,
            'is_approved': self.is_approved,
            'problem': self.problem,
            'solution': self.solution,
            'url': reverse('view_reference', args=[self.slug]),
        }

        if self.illustration1:
            dict['list_image'] = get_thumbnail(self.illustration1, "200x200", crop='center').url
        elif self.illustration2:
            dict['list_image'] = get_thumbnail(self.illustration2, "200x200", crop='center').url

        if self.is_customer_public:
            dict['customer'] = self.customer.to_dict()
        return dict

    def comments_count(self):
        return self.comments.all().count()


class EnglishTranslation(models.Model):
    reference = models.OneToOneField(Reference, verbose_name=_('reference'))
    title = models.CharField(max_length=200, verbose_name=_('title'))

    date_created = models.DateTimeField(editable=False)
    date_saved = models.DateTimeField(editable=False)
    created_by = models.ForeignKey(User, related_name='created_englishtranslation', editable=False)
    saved_by = models.ForeignKey(User, related_name='saved_englishtranslation', editable=False)

    application = models.TextField(verbose_name=_('subtitle'))
    machine = models.CharField(max_length=240, blank=True, verbose_name=_('machine'))
    machine_type = models.CharField(max_length=240, blank=True, verbose_name=_('machine type'))

    fluid = models.CharField(max_length=40, blank=True, verbose_name=_('fluid'))
    fluid_manufacturer = models.CharField(max_length=40, blank=True, verbose_name=_('fluid manufacturer'))
    fluid_type = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('fluid type'))
    filtering_level = models.CharField(max_length=30, blank=True, verbose_name=_('filtering level'))
    cost_reductions = models.CharField(max_length=50, blank=True, verbose_name=_('cost reductions'))

    filter = models.TextField(verbose_name=_('filter'))
    filter_element = models.TextField(blank=True, verbose_name=_('filter element'))

    analysis_before = models.TextField(blank=True, verbose_name=_('analysis before'))
    analysis_after = models.TextField(blank=True, verbose_name=_('analysis after'))

    problem = models.TextField(blank=True, verbose_name=_('problem'))
    solution = models.TextField(blank=True, verbose_name=_('solution'))

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        from fs_ref.core.auth import get_current_user

        if not self.pk:
            self.date_created = datetime.now()
            self.created_by = get_current_user()

        self.date_saved = datetime.now()
        self.saved_by = get_current_user()
        super(EnglishTranslation, self).save(*args, **kwargs)

    def to_dict(self):
        dict = {
            'title': self.title,
            'date_created': str(self.date_created),
            'date_saved': str(self.date_saved),
            'market': unicode(self.reference.market),
            'filter_solution': unicode(self.reference.filter_solution),
            'application': self.application,
            'machine': self.machine,
            'machine_type': self.machine_type,
            'filter': self.filter,
            'filter_element': self.filter_element,
            'manufacturer': str(self.reference.manufacturer),
            'problem': self.problem,
            'solution': self.solution,
            'url': reverse('view_reference', args=[self.reference.slug]),
        }

        if self.reference.illustration1:
            dict['list_image'] = get_thumbnail(self.reference.illustration1, "200x200", crop='center').url
        elif self.reference.illustration2:
            dict['list_image'] = get_thumbnail(self.reference.illustration2, "200x200", crop='center').url

        if self.reference.is_customer_public:
            dict['customer'] = self.reference.customer.to_dict()
        return dict

    def comments_count(self):
        return self.reference.comments.all().count()