import PySimpleGUI as sg
import time
import threading
import random


def main_menu():
    layout = [
        [sg.Button("Start"), sg.Button("Quit")]
    ]

    window = sg.Window("Main Menu", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Quit":
            break

        if event == "Start":
            window.close()
            secondary_menu()

    window.close()


def secondary_menu():
    layout = [
        [sg.Graph(canvas_size=(200, 200), graph_bottom_left=(0, 0), graph_top_right=(200, 200), key="graph")],
        [sg.Button("Back")]
    ]

    window = sg.Window("Secondary Menu", layout)

    graph_elem = window["graph"]

    # Start a thread for updating the color of the circle
    threading.Thread(target=update_circle_color, args=(graph_elem,), daemon=True).start()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Back":
            break

    window.close()
    main_menu()


def update_circle_color(graph_elem):
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]

    while True:
        time.sleep(2)
        new_color = random.choice(colors)

        # Clear the graph before drawing the new colored circle
        graph_elem.draw_circle((100, 100), 50, line_color="black", fill_color="white")
        graph_elem.draw_circle((100, 100), 50, line_color="black", fill_color=new_color)


if __name__ == "__main__":
    main_menu()
