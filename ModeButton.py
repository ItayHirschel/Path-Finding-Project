from radiobutton import RadioButton

class WorkMode():
    STERILE = 0
    ON_OFF_MODE = 1
    CHOOSE_START = 2

work_modes = [
    RadioButton.Option("sterile mode", WorkMode.STERILE, 650, 570),
    RadioButton.Option("toggle button", WorkMode.ON_OFF_MODE, 650, 540),
    RadioButton.Option("choose stating point", WorkMode.CHOOSE_START, 650, 510)
]

WORK_MODE = None
def mode_init():
    WORK_MODE = RadioButton(None, None, work_modes, 0)