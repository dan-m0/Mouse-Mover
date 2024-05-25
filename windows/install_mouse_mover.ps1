# Logging setup
$logFile = "$PWD/logging/installer.log"
function InitializeLog {
    # Create logging directory if it doesn't exist
    if (-not (Test-Path -Path $logDirectory)) {
        New-Item -ItemType Directory -Path $logDirectory -Force
    }

    $logContent = @"
This is the log file for Mouse Mover's installer.

Please see https://github.com/nyxtryx/MouseMover/?tab=readme-ov-file#error-codes for more information.

If your issue is not listed, please go to https://github.com/nyxtryx/MouseMover/issues/new?labels=bug&template=bug-report---.md

Logging started at $(Get-Date -Format "dd/MM/yyyy HH:mm:ss.fff")
___________________________________________
Date Time        Description
___________________________________________
"@
    $logContent | Set-Content -Path $logFile -Force
}

# Initialize log file
InitializeLog

function LogEvent {
    param(
        [string]$message
    )
    $timeStamp = Get-Date -Format "dd/MM/yyyy HH:mm:ss.fff"
    $logContent = "$timeStamp     $message"
    Add-Content -Path $logFile -Value $logContent
}

# Step 1: Prompt user to confirm and log the answer
$confirmation = Read-Host "Do you want to proceed with the installation? (y/n)"
LogEvent "User confirmation: $confirmation"

# User chose not to proceed
if ($confirmation -eq 'n') {
    LogEvent "User chose not to proceed with the installation."
    exit
}

# Log user confirmation if they chose to proceed
LogEvent "User chose to proceed with the installation."

# Step 2: Check if winget is installed
try {
    $wingetInstalled = winget --version
    if ($wingetInstalled) {
        LogEvent "winget already installed."
    }
} catch {
    LogEvent "CRITICAL: Failed to check if winget is installed. Error: $_"
    $wingetInstalled = $false
}

if (-not $wingetInstalled) {
    try {
        # Attempt to install winget automatically using cURL
        curl --output $env:TEMP\winget_installer.msi https://github.com/microsoft/winget-cli/releases/latest/download/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
        msiexec /i $env:TEMP\winget_installer.msi /quiet
        if ($?) {
            LogEvent "Successfully installed winget."
            $wingetInstalled = $true
        } else {
            # Open the installation URL if automatic installation fails
            Start-Process "https://aka.ms/getwinget"
            LogEvent "Failed to install winget automatically. Opening installation URL."
        }
    } catch {
        LogEvent "CRITICAL: Failed to install winget. Error: $_"
    }
}

# Step 3: Check if Python 3.12.3 is installed
try {
    $pythonInstalled = winget list --search Python | Select-String "3.12.3"
} catch {
    LogEvent "CRITICAL: Failed to check if Python 3.12.3 is installed. Error: $_"
    $pythonInstalled = $false
}

if (-not $pythonInstalled) {
    try {
        # Install Python 3.12.3 using winget
        winget install --id Python.Python.3 | Out-Null
        LogEvent "Python 3.12.3 installed successfully."
    } catch {
        LogEvent "CRITICAL: Failed to install Python 3.12.3. Error: $_"
    }
}

# Step 4: Install pyautogui using pip
try {
    python -m pip install pyautogui --trusted-host pypi.org --trusted-host files.pythonhosted.org | Out-Null
    LogEvent "pyautogui installed successfully."
} catch {
    LogEvent "CRITICAL: Failed to install pyautogui. Error: $_"
}

# Step 5: Move file mouse_mover.py to Documents folder
try {
    $sourceFile = "$PWD\\mouse_mover.py"
    if (Test-Path $sourceFile) {
        $destinationFolder = [Environment]::GetFolderPath("MyDocuments")
        Move-Item -Path $sourceFile -Destination $destinationFolder -Force
        LogEvent "Moved mouse_mover.py to Documents folder successfully. Absolute path: $destinationFolder\mouse_mover.py"
    } else {
        LogEvent "CRITICAL: mouse_mover.py not found at $sourceFile."
    }
} catch {
    LogEvent "CRITICAL: Failed to move mouse_mover.py to Documents folder. Error: $_"
}

# Notify user if all steps completed
if (-not $?) {
    [System.Windows.MessageBox]::Show("Installation completed. Please run mouse_mover.py script.", "Installation Completed")
}
