from reactpy import component, html, hooks
from components.button import Button


def increment(last_count):
    return last_count + 1


@component
def Count():
    count, set_count = hooks.use_state(0)
    return html._(html.h1(f"Count: {count}"),
                  html.br(),
                  Button({"color": 'primary',
                          "variant": 'contained',
                          "on_click": lambda event: set_count(increment)}, 
                          "Increment"))
