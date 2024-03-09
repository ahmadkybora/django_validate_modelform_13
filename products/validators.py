from django.core.exceptions import ValidationError


def validate_amazing(value):
    """Raise a ValidationError if the value doesn't start with the
    word 'Amazing'.
    """
    if not value.startswith('Amazing'):
        msg = 'Must start with Amazing'
        raise ValidationError(msg)