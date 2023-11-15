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