import os
import time
from datetime import datetime

# Setup the log
log_path = "logging/mouse_mover.log"

if os.path.exists(log_path):
    mode = "a"  # If the file exists, append mode (adds to the file)
else:
    mode = "w"  # If the file doesn't exist, write mode (creates a new file)

# Open the file in the determined mode
with open(file=log_path, mode=mode) as f:
    # Write log information
    if mode == "w":
        # If it's a new file, write initial setup
        f.write(f"""This is the log file for Mouse Mover.
        
Please see https://github.com/nyxtryx/MouseMover/?tab=readme-ov-file#error-codes for more information.

If your issue is not listed, please go to https://github.com/nyxtryx/MouseMover/issues/new?labels=bug&template=bug-report---.md

Logging started: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[
        :-3]}
___________________________________________

Date Time \t\t\t Code \t Message
___________________________________________

""")
    else:
        # If the file exists, append current timestamp
        f.write(
            f"""
\nLogging started: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[
:-3]}
___________________________________________
Date Time \t\t Code\tMessage
___________________________________________\n"""
        )


def log_message(date_time: datetime, log_code: int, message: str) -> None:
    """A  function to write log data to mouse_mover.log
    This can be used to debug the program if there are problems.

    ARGS
        date_time: datetime: The current date and time
        log_code: int: The code for the log message
        message: str: The message to write to the log file
    RETURNS
        None
    """
    with open(log_path, "a") as f:
        f.write(f"{date_time} \t {log_code} \t {message} \n")


log_message(
    date_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[
        :-3
    ],  # Get milliseconds with 3 decimal places
    log_code=0,
    message="""Logging setup successful! Checking imports...""",
)

# putting an import inside ANY code is not recommended, but this is a special case - this program is designed for any user to work with, so it must handle the user not having pyautogui installed, and correctly prompt them as to how to fix this - in this case, by running the installer install_mouse_mover.ps1

try:
    import pyautogui  # type: ignore

    log_message(
        date_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
        log_code=12,
        message="""Import successful!""",
    )

    print("\n To exit, close this window or press Ctrl+C\n")

    """Log codes
    This comment block provides context to co-pilot

    0 - Log setup
    1 - Error code for undefined errors
    2 - User aborts installer
    3 - winget fails to install
    4 - python fails to install
    5 - Keyboard interrupt

    6 - Loop started
    7 - Loop stopped
    8 - Cursor moved
    9 - Cursor not moved
    10 - Cursor moved to new position
    11 - Cursor moved to last position
    12 - variables set
    13 - datetime formatting
    """

    def get_date_time() -> str:
        """Returns the current date and time in the format YYYY-MM-DD HH:MM:SS

        RETURNS
            str: The current date and time
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[
            :-3
        ]  # Get milliseconds with 3 decimal places

    log_message(
        date_time=get_date_time(),
        log_code=0,
        message="""datetime formatting successful! Setting variables...""",
    )

    last_cursor_position = pyautogui.position()
    last_move_time = time.time()
    run = True

    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()
    move_to = (screen_width - 500, screen_height - 500)

    moved_already = False
    last_position = (screen_width / 2, screen_height / 2)

    log_message(
        date_time=get_date_time(),
        log_code=12,
        message="""Variable setting successful! Starting loop...""",
    )

    print(f"""\n\nScreen size: {screen_width}x{screen_height}""")
    print(f"""\n\nMouse will move to {move_to}""")

    def move_cursor() -> None:
        """
        Moves the cursor to a new position, within your screen size.

        Pause moving if the user manually moves the cursor.
        RETURNS
            None
        """
        global moved_already
        global last_position

        # Get the current position of the cursor
        current_position = pyautogui.position()

        # Move the cursor
        if moved_already:
            log_message(
                date_time=get_date_time(),
                log_code=11,
                message="""Cursor moved to last position""",
            )
            pyautogui.moveTo(move_to)
            moved_already = False
            last_position = current_position
        else:
            log_message(
                date_time=get_date_time(),
                log_code=10,
                message="""Cursor moved to new position""",
            )
            pyautogui.moveTo(last_position)
            moved_already = True

        # This keeps running the script until you stop it

    log_message(
        date_time=get_date_time(),
        log_code=6,
        message="""Loop started successfully! Program running...""",
    )
    while run:
        # Check if the cursor has moved
        current_position = pyautogui.position()
        if current_position != last_cursor_position:
            # Cursor has moved, update the last cursor position and reset the timer

            log_message(
                date_time=get_date_time(),
                log_code=9,
                message="""Cursor  moved""",
            )

            last_cursor_position = current_position
            last_move_time = time.time()

        else:
            # Check if the cursor is idle

            log_message(
                date_time=get_date_time(),
                log_code=8,
                message="Cursor not moved",
            )

            if time.time() - last_move_time >= 2:
                move_cursor()
                last_move_time = time.time()

        # Add a small sleep to reduce CPU usage
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n\nExiting...")
    log_message(
        date_time=get_date_time(),
        log_code=7,
        message="""Loop stopped successfully! Program exiting...""",
    )

    log_message(
        date_time=get_date_time(),
        log_code=5,
        message=f"""User exited program by keyboard interrupt.
Logging ended: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[
:-3
]},  
End of log""",
    )

except ImportError:
    import_help_message = """!RELAX THIS ISN'T A VIRUS, YOU JUST DIDN'T FOLLOW THE INSTRUCTIONS CORRECTLY!



What's wrong then?    

    pyautoGUI failed to import!

What is pyautoGUI?

    pyautoGUI is a library (see https://www.linkedin.com/pulse/python-libraries-comprehensive-guide-most-widely-used-ajay-tiwari-8o5ic/)

    In this program, it is what moves the mouse around the screen.

Okay... How do I get it?

    Press and hold the windows key, at the same time press R, then type in "powershell" and press enter.
    
    Paste the following command into the powershell window and press enter:
    
    PowerShell.exe -ExecutionPolicy Bypass -File .\\install_mouse_mover.ps1
    
    Please run install_mouse_mover.ps1 which can be found in the same directory as this script, as it was downloaded.
    
    If you cannot find 

    The installer is designed to run in many Windows environments, and should fully setup this program to be run as expected.

    The installer is designed to run in corporate environments, where there may be complications to installing software.

    It will also run as expected on a personal computer.

    This program will NOT run correctly without running the installer."""

    log_message(
        date_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[
            :-3
        ],  # Get milliseconds with 3 decimal places,
        log_code=14,
        message=f"""{import_help_message}
\n
Logging ended: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[
    :-3
]}
End of log""",
    )
    print(import_help_message)

    with open("run_the_installer!.txt", "w") as file:
        file.write(import_help_message)

    # Open the file
    import os

    os.startfile("run_the_installer!.txt")

except Exception as e:
    log_message(
        date_time=get_date_time(),
        log_code=1,
        message=f"""Unhandled error! Exception: {e}.
Program exiting... 
    
Please report this here: https://github.com/nyxtryx/MouseMover/issues/new?labels=bug&template=bug-report---.md
    \n
Logging ended: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[
    :-3
]}
    End of log""",
    )
