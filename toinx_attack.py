import curses
import subprocess
import time
import json
import os

CONFIG_FILE = "tools.json"

ascii_art = [
    " _____       _       __   __  __     _    _   _ ",
    "|_   _|     | |      \\ \\ / / |  \\/  |   | |  | |",
    "  | |  ___  | |_      \\ V /  | \\  / | __| |  | |",
    "  | | / _ \\ | __|      > <   | |\\/| |/ _` |  | |",
    " _| || (_) || |_      / . \\  | |  | | (_| |  |_|",
    " \\___/\\___/  \\__|    /_/ \\_\\ |_|  |_|\\__,_|  (_)"
]

def load_tools():
    if not os.path.isfile(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def splash_screen(stdscr):
    curses.start_color()
    curses.use_default_colors()
    colors = [curses.COLOR_RED, curses.COLOR_YELLOW, curses.COLOR_GREEN, curses.COLOR_CYAN, curses.COLOR_MAGENTA, curses.COLOR_BLUE]
    for i in range(len(colors)):
        curses.init_pair(i + 1, colors[i], -1)
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    start_y = (h // 2) - (len(ascii_art) // 2)
    start_x = (w // 2) - (max(len(line) for line in ascii_art) // 2)

    for i, line in enumerate(ascii_art):
        stdscr.attron(curses.color_pair((i % len(colors)) + 1) | curses.A_BOLD)
        stdscr.addstr(start_y + i, start_x, line)
        stdscr.attroff(curses.color_pair((i % len(colors)) + 1) | curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.2)
    time.sleep(1.5)

def print_menu(stdscr, tools, current_row):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    title = "ToinX AttxK - Hacker Suite"
    stdscr.attron(curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(1, w//2 - len(title)//2, title)
    stdscr.attroff(curses.color_pair(2) | curses.A_BOLD)

    for idx, tool in enumerate(tools):
        x = 3 + idx
        if idx == current_row:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(x, 4, tool)
            stdscr.attroff(curses.color_pair(3))
        else:
            stdscr.addstr(x, 4, tool)

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(h-2, 2, "↑/↓: Navegar  ENTER: Selecionar  ESC: Sair")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

def confirm_screen(stdscr, tool_name):
    h, w = stdscr.getmaxyx()
    msg = f"Executar '{tool_name}'? (S/N)"
    stdscr.clear()
    stdscr.attron(curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(h//2, w//2 - len(msg)//2, msg)
    stdscr.attroff(curses.color_pair(2) | curses.A_BOLD)
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key in [ord('s'), ord('S')]:
            return True
        elif key in [ord('n'), ord('N'), 27]:
            return False

def run_tool(stdscr, command):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    msg = "Executando... Pressione Ctrl+C para cancelar"
    stdscr.addstr(1, w//2 - len(msg)//2, msg)
    stdscr.refresh()
    curses.endwin()
    try:
        ret = subprocess.call(command, shell=True)
        print()
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")
        ret = -1
    time.sleep(1)
    stdscr.clear()
    curses.initscr()
    curses.start_color()
    return ret

def feedback_screen(stdscr, success):
    h, w = stdscr.getmaxyx()
    if success == 0:
        msg = "Sucesso! Pressione qualquer tecla para continuar."
        color = curses.color_pair(4)
    elif success == -1:
        msg = "Execução cancelada. Pressione qualquer tecla para continuar."
        color = curses.color_pair(1)
    else:
        msg = "Erro durante execução. Pressione qualquer tecla para continuar."
        color = curses.color_pair(1)
    stdscr.clear()
    stdscr.attron(color | curses.A_BOLD)
    stdscr.addstr(h//2, w//2 - len(msg)//2, msg)
    stdscr.attroff(color | curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_CYAN, -1)    # instruções e erros
    curses.init_pair(2, curses.COLOR_YELLOW, -1)  # título e confirmações
    curses.init_pair(3, curses.COLOR_GREEN, -1)   # seleção do menu
    curses.init_pair(4, curses.COLOR_MAGENTA, -1) # sucesso

    tools = load_tools()
    if not tools:
        stdscr.addstr(0,0,"Arquivo tools.json não encontrado ou vazio.")
        stdscr.refresh()
        stdscr.getch()
        return

    splash_screen(stdscr)

    current_row = 0
    tools_list = list(tools.keys())

    while True:
        print_menu(stdscr, tools_list, current_row)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(tools_list) - 1:
            current_row += 1
        elif key == ord('\n'):
            tool_name = tools_list[current_row]
            if confirm_screen(stdscr, tool_name):
                ret = run_tool(stdscr, tools[tool_name])
                feedback_screen(stdscr, ret)
        elif key == 27:  # ESC
            break

curses.wrapper(main)
