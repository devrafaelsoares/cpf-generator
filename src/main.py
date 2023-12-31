import PySimpleGUI as sg
from settings import (
    layout_title,
    layout_input,
    layout_button_submit,
    layout_title_input,
    paht_icon,
)
from validateCpf import validate_cfp

from validateInput import validate

regex = "^([0-9](\d{0,11}))?$"
old = {"CPF": ""}

layout = [[layout_title], [layout_title_input, layout_input], [layout_button_submit]]

window = sg.Window("Validador de CPF", layout, icon=paht_icon, finalize=True)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "CPF":
        element, text = window[event], values[event]
        if validate(regex, text):
            try:
                if len(text) > 11:
                    element.update(old[event])
                    continue
            except ValueError:
                pass
            old[event] = text
        else:
            element.update(old[event])
    elif event == "Verificar":
        if values["CPF"] == "":
            sg.popup("É necessário informar o CPF", title="Validador de CPF")
        elif len(values["CPF"]) < 11:
            sg.popup(
                "CPF inválido. O CPF deve ter 11 dígitos", title="Validador de CPF"
            )
        else:
            result = validate_cfp(values["CPF"])
            sg.popup(
                f"CPF {result['data']}\nStatus: {result['message']}",
                title="Validador de CPF",
                font=10,
            )
