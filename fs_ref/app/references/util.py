from django.utils.translation import ugettext_lazy as _


FLOW_UNITS = (
    (1, _('l/min')),
    (2, _('m^3/h')),
)

FILTERING_LEVEL = (
    (1, u'mu. abs. ISO16889  Beta 200'),
    (2, u'mu. abs. ISO16889  Beta1000'),
    (3, u'mu. nominell'),
    (4, u'mu. abs. Beta 5000'),
    (5, u'mu.'),
    (20, u'EN 60335-2-69'),
    (40, u'EN 779'),

)

VISCOSITY_TYPES = (
    (1, u'mm^2/s'),
    (2, u'cP'),
)

FLUIDS = (
    ('1', _('1')),
)

COUNTRIES = (
    (45, _('Denmark')),
    (46, _('Sweden')),
    (47, _('Norway')),
)

COUNTRY_LANGUAGE = {
    '45': 'dk',
    '46': 'sv',
    '47': 'no',
}