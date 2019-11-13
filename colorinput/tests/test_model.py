from ..models import ColorField

def test_colorfield_deconstruct():
    color_field = ColorField()
    name, path, args, kwargs = color_field.deconstruct()
    assert 'max_length' not in kwargs
