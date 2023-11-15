from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

import re


def number_validator(password):
    regex = re.compile("[0-9]")
    if regex.match(password) == None:
        raise ValidationError(
            _("password must include number"),
            code="password_must_include_number",
        )


def letter_validator(password):
    regex = re.compile("[a-zA-Z]")
    if regex.search(password) == None:
        raise ValidationError(
            _("password must include letter"),
            code="password_must_include_letter",
        )
