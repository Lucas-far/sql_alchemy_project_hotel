

def ink(the_text: str):
    from random import choice

    box: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m',
        '\033[1:37m', '\033[1:38m',
    )

    return f"{choice(box)}{the_text}{box[-1]}"


def i(the_text: str, color: str):

    inks = {
        'b': '\033[1:30m' + the_text + '\033[1:38m',
        'r': '\033[1:31m' + the_text + '\033[1:38m',
        'g': '\033[1:32m' + the_text + '\033[1:38m',
        'y': '\033[1:33m' + the_text + '\033[1:38m',
        'bl': '\033[1:34m' + the_text + '\033[1:38m',
        'p': '\033[1:35m' + the_text + '\033[1:38m',
        'c': '\033[1:36m' + the_text + '\033[1:38m',
        'gy': '\033[1:37m' + the_text + '\033[1:38m',
    }

    for key_ in inks:
        if key_ == color:
            return inks[key_]


def menu_creator(paint, move_to_right, right_px, menu_content,):

    for data in menu_content:
        if paint and not move_to_right:
            print(ink(data))
        if paint and move_to_right:
            print(ink(data.center(right_px)))
        if not paint and move_to_right:
            print(data.center(right_px))
        if not paint and not move_to_right:
            print(data)


def code_block_init(*args) -> None:

    for content in args:
        print(content)


if __name__ == '__main__':
    pass
