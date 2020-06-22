from django.templatetags.static import static
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = "horizontal"
