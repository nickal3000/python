import PySimpleGUI as sg

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Error"

layout = [
    [sg.InputText("", key="display", size=(20, 1), justification="right", font=("Helvetica", 20))],
    [sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("/"), sg.Button("C")],
    [sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("*"), sg.Button("<-")],
    [sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("-"), sg.Button("(")],
    [sg.Button("0"), sg.Button("."), sg.Button("="), sg.Button("+"), sg.Button(")")],
]

window = sg.Window("Calculator", layout)

expression = ""

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event in "01234567089.+-*/()":
        expression += event
        window["display"].update(expression)

    elif event == "=":
        result = evaluate_expression(expression)
        window["display"].update(result)
        expression = str(result)

    elif event == "C":
        expression = ""
        window["display"].update("")

    elif event == "<-":
        expression = expression[:-1]
        window["display"].update(expression)

window.close()
