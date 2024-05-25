#!/bin/bash

# Logging setup
logFile="$PWD/logging/installer.log"
function InitializeLog {
    # Create logging directory if it doesn't exist
    if [ ! -d "$logDirectory" ]; then
        mkdir -p "$logDirectory"
    fi

    logContent="\
This is the log file for Mouse Mover's installer.

Please see https://github.com/nyxtryx/MouseMover/?tab=readme-ov-file#error-codes for more information.

If your issue is not listed, please go to https://github.com/nyxtryx/MouseMover/issues/new?labels=bug&template=bug-report---.md

Logging started at $(date +"%d/%m/%Y %H:%M:%S.%3N")
___________________________________________
Date Time        Description
___________________________________________
"
    echo "$logContent" > "$logFile"
}

# Initialize log file
InitializeLog

function LogEvent {
    message="$1"
    timeStamp=$(date +"%d/%m/%Y %H:%M:%S.%3N")
    logContent="$timeStamp     $message"
    echo "$logContent" >> "$logFile"
}

# Step 1: Prompt user to confirm and log the answer
read -p "Do you want to proceed with the installation? (y/n)" confirmation
LogEvent "User confirmation: $confirmation"

# User chose not to proceed
if [ "$confirmation" != "y" ]; then
    LogEvent "User chose not to proceed with the installation."
    exit
fi

# Log user confirmation if they chose to proceed
LogEvent "User chose to proceed with the installation."

# Step 2: Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    LogEvent "Homebrew is not installed."
    # Install Homebrew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    LogEvent "Homebrew installed successfully."
else
    LogEvent "Homebrew already installed."
fi

# Step 3: Check if Python 3.12.3 is installed
if ! command -v python3.12.3 &> /dev/null; then
    LogEvent "Python 3.12.3 is not installed."
    # Install Python 3.12.3 using Homebrew
    brew install python@3.12.3
    LogEvent "Python 3.12.3 installed successfully."
else
    LogEvent "Python 3.12.3 already installed."
fi

# Step 4: Install pyautogui using pip
if ! python3 -m pip show pyautogui &> /dev/null; then
    LogEvent "pyautogui is not installed."
    python3 -m pip install pyautogui --trusted-host pypi.org --trusted-host files.pythonhosted.org
    LogEvent "pyautogui installed successfully."
else
    LogEvent "pyautogui already installed."
fi

# Notify user if all steps completed
if [ $? -eq 0 ]; then
    osascript -e 'tell app "System Events" to display dialog "Installation completed. Please see https://nyxtryx.github.io/Mouse-Mover/guides/mac for next steps" with title "Installation Completed"'
fi
