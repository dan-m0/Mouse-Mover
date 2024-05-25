Please follow the below steps

1. Download [these files]()
2. Go to where you saved the files
3. At the bottom of the Finder window, right click on mac
4. Select Open in Terminal
5. Paste this and press enter: /bin/bash 
    5.1. This is temporary!
6. Paste this and press enter: chmod -x mac-installer.bash
    6.1. This allows the installer to run in executable mode (-x)
    6.2. For more information, instead paste this an press enter: man chmod
        6.2.1. Scroll with the arrow keys
        6.2.2. To exit, press control+Z
        6.2.3. When you are ready, go back to step 6.
7. You will be prompted for your password - the installer will need to make changes to setup correctly
8. Paste this and press enter: ./mac-installer.bash
    8.1. The installer will tell you what to do if there are errors.
    8.2. You will be prompted to allow system event access, this is to provide confirmation the installation is complete, and for logging
6. Close the terminal
7. Right click on mouse_mover.py
8. Open With >
9. Python Launcher

To end the program, close the window that opened, or select the window and press contrl+C