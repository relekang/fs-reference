# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name='name')),
                ('website', models.URLField(verbose_name='customer website', blank=True)),
                ('industry', models.CharField(max_length=140, verbose_name='customer industry', blank=True)),
                ('country', models.IntegerField(verbose_name='country', choices=[(45, 'Denmark'), (46, 'Sweden'), (47, 'Norway')])),
            ],
        ),
        migrations.CreateModel(
            name='EnglishTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_saved', models.DateTimeField(editable=False)),
                ('application', models.TextField(verbose_name='subtitle')),
                ('machine', models.CharField(max_length=240, verbose_name='machine', blank=True)),
                ('machine_type', models.CharField(max_length=240, verbose_name='machine type', blank=True)),
                ('fluid', models.CharField(max_length=40, verbose_name='fluid', blank=True)),
                ('fluid_manufacturer', models.CharField(max_length=40, verbose_name='fluid manufacturer', blank=True)),
                ('fluid_type', models.CharField(max_length=50, null=True, verbose_name='fluid type', blank=True)),
                ('filtering_level', models.CharField(max_length=30, verbose_name='filtering level', blank=True)),
                ('cost_reductions', models.CharField(max_length=50, verbose_name='cost reductions', blank=True)),
                ('filter', models.TextField(verbose_name='filter')),
                ('filter_element', models.TextField(verbose_name='filter element', blank=True)),
                ('analysis_before', models.TextField(verbose_name='analysis before', blank=True)),
                ('analysis_after', models.TextField(verbose_name='analysis after', blank=True)),
                ('problem', models.TextField(verbose_name='problem', blank=True)),
                ('solution', models.TextField(verbose_name='solution', blank=True)),
                ('created_by', models.ForeignKey(related_name='created_englishtranslation', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='FilterSolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('en', models.CharField(max_length=50, verbose_name='English')),
                ('no', models.CharField(max_length=50, verbose_name='Norwegian')),
                ('dk', models.CharField(max_length=50, verbose_name='Danish')),
                ('sv', models.CharField(max_length=50, verbose_name='Swedish')),
            ],
            options={
                'ordering': ('en',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('code', models.CharField(unique=True, max_length=120, verbose_name='code')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('en', models.CharField(max_length=50, verbose_name='English')),
                ('no', models.CharField(max_length=50, verbose_name='Norwegian')),
                ('dk', models.CharField(max_length=50, verbose_name='Danish')),
                ('sv', models.CharField(max_length=50, verbose_name='Swedish')),
            ],
            options={
                'ordering': ('en',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(unique=True, max_length=200, editable=False)),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_saved', models.DateTimeField(editable=False)),
                ('is_approved', models.BooleanField(default=False, verbose_name='approved')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('country', models.PositiveIntegerField(verbose_name='country', choices=[(45, 'Denmark'), (46, 'Sweden'), (47, 'Norway')])),
                ('customer_contact', models.CharField(max_length=200, verbose_name='customer contact', blank=True)),
                ('is_customer_public', models.BooleanField(default=False, verbose_name='view customer in public')),
                ('has_borrowed_products_before_purchase', models.BooleanField(verbose_name='borrowed products before purchase')),
                ('date_installed', models.DateField(null=True, verbose_name='install date', blank=True)),
                ('application', models.TextField(verbose_name='subtitle')),
                ('machine', models.CharField(max_length=240, verbose_name='machine', blank=True)),
                ('machine_type', models.CharField(max_length=240, verbose_name='machine type', blank=True)),
                ('fluid', models.CharField(max_length=40, verbose_name='fluid', blank=True)),
                ('fluid_manufacturer', models.CharField(max_length=40, verbose_name='fluid manufacturer', blank=True)),
                ('fluid_type', models.CharField(max_length=50, null=True, verbose_name='fluid type', blank=True)),
                ('filtering_level', models.CharField(max_length=30, verbose_name='filtering level', blank=True)),
                ('filtering_standard', models.IntegerField(blank=True, null=True, verbose_name='filtering standard', choices=[(1, 'mu. abs. ISO16889  Beta 200'), (2, 'mu. abs. ISO16889  Beta1000'), (3, 'mu. nominell'), (4, 'mu. abs. Beta 5000'), (5, 'mu.'), (20, 'EN 60335-2-69'), (40, 'EN 779')])),
                ('flow', models.IntegerField(null=True, verbose_name='flow', blank=True)),
                ('flow_unit', models.IntegerField(default=1, choices=[(1, 'l/min'), (2, 'm^3/h')])),
                ('pressure', models.IntegerField(null=True, verbose_name='pressure (bar)', blank=True)),
                ('system_volume', models.IntegerField(null=True, verbose_name='system volume', blank=True)),
                ('temp', models.IntegerField(null=True, verbose_name='temperature (C)', blank=True)),
                ('viscosity', models.DecimalField(null=True, verbose_name='viscosity', max_digits=5, decimal_places=2, blank=True)),
                ('viscosity_type', models.IntegerField(default=1, max_length=50, verbose_name='viscosity type', choices=[(1, 'mm^2/s'), (2, 'cP')])),
                ('cost_reductions', models.CharField(max_length=50, verbose_name='cost reductions', blank=True)),
                ('filter', models.TextField(verbose_name='filter')),
                ('filter_element', models.TextField(verbose_name='filter element', blank=True)),
                ('analysis_before', models.TextField(verbose_name='analysis before', blank=True)),
                ('analysis_after', models.TextField(verbose_name='analysis after', blank=True)),
                ('problem', models.TextField(verbose_name='problem', blank=True)),
                ('solution', models.TextField(verbose_name='solution', blank=True)),
                ('illustration1', models.ImageField(help_text=b'This illustration must be at least 800px wide', upload_to=b'references/illustrations/', null=True, verbose_name='illustration 1', blank=True)),
                ('illustration2', models.ImageField(upload_to=b'references/illustrations/', null=True, verbose_name='illustration 2', blank=True)),
                ('illustration3', models.ImageField(upload_to=b'references/illustrations/', null=True, verbose_name='illustration 3', blank=True)),
                ('file', models.FileField(upload_to=b'references/files/', null=True, verbose_name='file', blank=True)),
                ('created_by', models.ForeignKey(related_name='created_reference', editable=False, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(related_name='references', verbose_name='customer', to='references.Customer')),
                ('filter_solution', models.ForeignKey(related_name='references', verbose_name='filter solution', to='references.FilterSolution')),
                ('manufacturer', models.ForeignKey(related_name='references', verbose_name='filter manufacturer', to='references.Manufacturer')),
                ('market', models.ForeignKey(related_name='references', verbose_name='market', to='references.Market')),
                ('salesman', models.ForeignKey(verbose_name='salesman', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('saved_by', models.ForeignKey(related_name='saved_reference', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
                'permissions': (('approve_reference', 'Can approve references'), ('publish_reference', 'Can publish references'), ('administrate_filters', 'Can administrate filters')),
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('en', models.CharField(max_length=50, verbose_name='English')),
                ('no', models.CharField(max_length=50, verbose_name='Norwegian')),
                ('dk', models.CharField(max_length=50, verbose_name='Danish')),
                ('sv', models.CharField(max_length=50, verbose_name='Swedish')),
            ],
            options={
                'ordering': ('en',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='reference',
            name='type',
            field=models.ForeignKey(related_name='references', verbose_name='application', to='references.Type'),
        ),
        migrations.AddField(
            model_name='englishtranslation',
            name='reference',
            field=models.OneToOneField(verbose_name='reference', to='references.Reference'),
        ),
        migrations.AddField(
            model_name='englishtranslation',
            name='saved_by',
            field=models.ForeignKey(related_name='saved_englishtranslation', editable=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
