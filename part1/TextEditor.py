# H.P Compton
# 1/29/24
# a simple text editor that opens a file and can be edited and saved using py
# https://github.com/israel-dryer/Text-Code-Editor/blob/master/text_code_editor.py and chatgbt helped me a lot


import PySimpleGUI as out

def create_file(file_path, name):
    try:
        with open(file_path, 'x') as file:
            file.write(name)
        return True
    except FileExistsError:
        return False

def save_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None

def main():
    saved = False
    out.theme('Amber')  # color obv
    initial_message = "Open a file to begin"

    layout =     [
        [out.Button('Open'), out.Button('Save'), out.Button('New'), out.Button('Exit')],
        [out.Multiline(size=(80, 20), key='-CONTENT-', autoscroll=True, default_text=initial_message)],
    ]

    window = out.Window('.TXT Editor', layout, resizable=True, finalize=True)

    current_file = None

    while True:
        event, values = window.read()

        if event == out.WINDOW_CLOSED or event == 'Exit':
            if saved:
                break
            else:
                response = out.popup_yes_no('Do you want to exit without saving?')
                if response == 'Yes':
                    break

        if event == 'Open':
            file_path = out.popup_get_file('Open File', file_types=(("Text Files", "*.txt"),))
            if file_path:
                current_file = file_path
                content = read_file(file_path)
                window['-CONTENT-'].update(content)

        if event == 'Save':
            if current_file:
                content = values['-CONTENT-']
                save_file(current_file, content)
                saved = True
            else:
                out.popup_error('Please open a file.')

        if event == 'New':
            name = out.popup_get_text('Enter file name:')
            if name:
                file_path = out.popup_get_file('Save File', file_types=(("Text Files", "*.txt"),), save_as=True, default_extension=".txt")
                if file_path:
                    current_file = file_path
                    if create_file(file_path, name):
                        window['-CONTENT-'].update('')
                        saved = False
                    else:
                        out.popup_error('File already exists. Choose a different name or location.')

    window.close()

main()