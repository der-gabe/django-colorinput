from django.forms import Form

from ..forms.fields import ColorField


def test_formfield_clean():
    formfield = ColorField()
    cleaned_value = formfield.clean('#abcdef')
    assert cleaned_value == 'abcdef'

def test_formfield_rendering():
    class TestForm(Form):
        color = ColorField(initial='d0d0d0')
    test_form = TestForm()
    html_output = test_form.as_p()
    assert('<input type="color" name="color" '
           'value="#d0d0d0" required id="id_color">' in html_output)
