Please follow the below steps for MacOS - this has **ONLY** been tested as a user with sudo access.

Feel free to fork and update if this doesn't work without sudo access and you know a way around that.

-----

# WARNING

<strong>
It is YOUR responsibility to check your company's IT policy allows you to install programs.

Please read the license; contributors to this program are NOT liable in the event of any losses.
</strong>

-----

1. Download [these files](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fnyxtryx%2FMouse-Mover%2Ftree%2Fmain%2Fmac)
    1. You will need a GitHub account for this
    2. Alternatively, you can download individual files [here](https://github.com/nyxtryx/Mouse-Mover/tree/main/mac) - you will need ALL of these files
2. Go to where you saved the files
3. At the bottom of the Finder window, right click on mac
4. Select Open in Terminal
5. Paste this and press enter: /bin/bash 
    1. This is temporary!
6. Paste this and press enter: chmod -x mac-installer.bash
    1. This allows the installer to run in executable mode (-x)
    2. For more information, instead paste this and press enter: man chmod
        1. Scroll with the arrow keys
        2. To exit, press control+Z
        3. When you are ready, go back to step 6.
7. You will be prompted for your password - the installer will need to make changes to setup correctly
8. Paste this and press enter: ./mac-installer.bash
    1. The installer will tell you what to do if there are errors.
    2. You will be prompted to allow system event access, this is  for logging the installer process
6. Close the terminal
7. Right click on mouse_mover.py
8. Open With >
9. Python Launcher

To end the program, close the window that opened, or select the window and press contrl+C
