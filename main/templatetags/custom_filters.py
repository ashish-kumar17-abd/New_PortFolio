from django import template

register = template.Library()

@register.filter
def split_sentences(value):
    """
    Splits a string by full stops into a list of sentences.
    """
    if not value:
        return []
    # Ensure stripping and ignore empty strings
    return [sentence.strip() for sentence in value.split('. ') if sentence.strip()]
