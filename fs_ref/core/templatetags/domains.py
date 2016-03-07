from django.template.base import Library

register = Library()


@register.simple_tag
def domain_for_lang(language_code):
    try:
        return {
            'no': 'lekang.com',
            'se': 'filterteknik.se',
            'dk': 'filterteknik.dk',
        }[language_code]
    except KeyError:
        return 'filtersystem.no'
