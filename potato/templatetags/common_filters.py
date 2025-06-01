from django.template import Library

register = Library()

#unhappy with this, complexity I don't understand from stupid claude et al
#probably doing something wrong and uneeded

@register.filter
def values_objects(field):
    """
    problem with selectMultiple, inputSingleFromMany, or other form widgets for manyToMany fields
    is they display {{ field.value }} as [1234] instead of object itself...
    this way {{ field|values_objects }} will display the object instead
    """
    if hasattr(field.field, 'queryset') and field.value():
        value = field.value()
        if not isinstance(value, (list, tuple)):
            obj = field.field.queryset.filter(pk=value).first()
            return str(obj) if obj else ''
        return ', '.join([str(field.field.queryset.filter(pk=pk).first()) for pk in value])
    return field.value()