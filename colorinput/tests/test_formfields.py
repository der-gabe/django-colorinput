# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.forms import Form
from django.test import SimpleTestCase
from hypothesis import example, given
from hypothesis.strategies import text
import pytest

from ..forms.fields import ColorField


HEX_ALPHABET = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}


@given(value=text())
@example('d0d0d0d0')
@example('00000000')
def test_formfield_clean_error(value):
    formfield = ColorField()
    with pytest.raises(ValidationError):
        formfield.clean(value)

@given(value=text(alphabet=HEX_ALPHABET, min_size=6, max_size=6))
@example('d0d0d0')
def test_formfield_clean_success(value):
    formfield = ColorField()
    cleaned_value = formfield.clean('#' + value)
    assert cleaned_value == value

@given(value=text(alphabet=HEX_ALPHABET, min_size=6, max_size=6))
@example('d0d0d0')
def test_formfield_prepare_value(value):
    formfield = ColorField()
    prepared_value = formfield.prepare_value(value)
    assert prepared_value == '#' + value

@given(value=text(alphabet=HEX_ALPHABET, min_size=6, max_size=6))
@example('d0d0d0')
def test_formfield_rendering(value):
    class TestForm(Form):
        color = ColorField(initial=value)
    test_form = TestForm()
    html_output = test_form.as_p()
    testcase = SimpleTestCase()
    testcase.assertInHTML(
        '<input type="color" name="color" value="#{}" '
        'required id="id_color">'.format(value),
        html_output
    )
