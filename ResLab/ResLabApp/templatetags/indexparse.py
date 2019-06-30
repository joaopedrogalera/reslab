from django import template

register = template.Library()

@register.filter
def indexparse(lista, indice):
    return lista[indice-1]
