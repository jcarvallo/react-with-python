from reactpy import component, html
from components.count import Count

@component
def App():
    return html._(Count())