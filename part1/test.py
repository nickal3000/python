import PySimpleGUI as sg

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(window, board):
    for i in range(3):
        for j in range(3):
            window[i, j].update(board[i][j])

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def main():
    sg.theme('DefaultNoMoreNagging')

    board_layout = [
        [sg.Button(' ', size=(4, 2), key=(i, j), pad=(0, 0)) for j in range(3)] for i in range(3)
    ]

    layout = [
        *board_layout,
        [sg.Text('', size=(15, 1), key='-OUTPUT-')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Tic-Tac-Toe', layout)

    board = create_board()
    player_turn = 'X'
    winner = None

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if winner:
            continue

        if isinstance(event, tuple):
            i, j = event
            if board[i][j] == ' ':
                board[i][j] = player_turn
                print_board(window, board)

                if check_winner(board):
                    winner = player_turn
                    window['-OUTPUT-'].update(f'Player {winner} wins!')
                elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                    window['-OUTPUT-'].update('It\'s a draw!')
                else:
                    player_turn = 'O' if player_turn == 'X' else 'X'

    window.close()
main()
