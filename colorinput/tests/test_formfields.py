from ..forms.fields import ColorField

def test_formfield_clean():
    formfield = ColorField()
    cleaned_value = formfield.clean('#abcdef')
    assert cleaned_value == 'abcdef'
