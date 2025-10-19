import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8 or len(password) > 16:
            raise ValidationError(_("The password must be between 8 and 16 characters."))

        if not re.search(r"[A-Z]", password):
            raise ValidationError(_("The password must contain at least one uppercase letter."))

        if not re.search(r"[a-z]", password):
            raise ValidationError(_("The password must contain at least one lowercase letter."))

        if not re.search(r"\d", password):
            raise ValidationError(_("The password must contain at least one digit."))

    def get_help_text(self):
        return _(
            "Your password must be between 8 and 16 characters long, including at least "
            " one uppercase letter, one lowercase letter, and one number."
        )
