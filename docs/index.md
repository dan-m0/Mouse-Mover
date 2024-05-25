<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** 
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO 
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
-->
<div>
  <h3 align="center">Idle Blocker</h3>

  <p align="center">
    A  program to prevent idle mode in applications, such as MS Teams
    <br />
    <a href="https://nyxtryx.github.io/Mouse-Mover/guides/guides">User Guides</a>
    ·
    <a href="https://nyxtryx.github.io/mouse-mover/guides/report-a-bug">Report Bug</a>
    ·
    <a href="https://nyxtryx.github.io/mouse-mover/guides/report-a-bug">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#setup">Setup</a></li>
    <ul>
        <li><a href='#windows-setup'>Windows</a></li>
        <li><a href='#macos-setup'>MacOS</a></li>
    </ul>
    <li><a href="#usage">Usage</a></li>
    <li><a href='#log-codes'>Log Codes</a></li>
    <li><a href='#compatibility'>Compatibility</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<br />

## About

This started because of [this Reddit post](https://www.reddit.com/r/workfromhome/comments/1cx7ayd/how_do_i_know_if_my_screen_time_is_monitored/) - I'd been looking for something to prevent my own work laptop showing me idle on MS Teams whenever I walked away for 5 minutes, and the post prompted me to create this.

The program will automatically move your mouse, within your screen, every minute.

If you move the mouse, the program pauses.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<br />


# Setup

Please follow the below steps for your system

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Windows Setup

### Command line
<br />

Please see [here][windows-cli-install-guide]

<br />
<br />

### Graphical User Interface

Coming soon!

<br />
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## MacOS Setup

### Command line
<br />

Coming soon!
<br />
<br />
### Graphical User Interface
<br/>
Coming soon!

<br />
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<br />

# Usage

Please see below for usage instructions

## Windows Usage
### Command line
<br />

Coming soon!
<br />
<br />
### Graphical User Interface
<br/>
Coming soon!

## MacOS Usage
<br />
  ### Command line
<br />

Coming soon!
<br />
<br />
### Graphical User Interface
<br/>
Coming soon!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Log Codes

If you encounter an error, you will find the error code and a brief description in the log file.

Please see the below table for the full list and an explanation.

If the error code isn't here, please [report a bug][report-a-bug-url]

|Code   |Name   |Explanation   |
|---|---|---|
|0   |Log setup   |The logging file has been created in PWD/logging   |
|1  |Undefined error   |An unexpected error occured, please [report this][bug-reporting]   |
|2  |Installer aborted | You cancelled the installer when asked if you wanted to continue  |
|3  |winget fails   |The Windows installer failed to automatically install winget - follow the prompt on screen   |  
|4  |Python fails   |The Windows installer failed to automatically install python, this may be related to Code:2 - follow the prompt on screen   |
|5   |Keyboard interrupt   |You pressed Ctrl+C to close the program   |
|6   |Loop started   |The main program loop has started - the program will run until closed   |
|7   |Loop stopped   |The loop stopped  |
|8   |Cursor moved   |The cursor has been moved because you weren't using it, so you're probably not there   |
|9   |Cursor not moved   |The cursor hasn't been moved, because you were using it, so you're probably there   |
|10   |Cursor moved to new position   |Related to Code:8 - this indicates that the specific part of the code to move the mouse worked   |
|11  |Cursor moved to last position   |Related to Code:8 - this indicates that the specific part of the code to move the mouse worked   |
|12   |Variables set   |Part of the initial startup   |
|13   |datetime formatting   |Part of the initial startup   |
|14   |autogui import failure   |pyautogui isn't installed - this is essential for the program. Please see [the setup][setup] section   |

## Compatibility

Coming soon!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
<!-- ❌   ✅  �-->

Items will be marked with ✅ when either I, or someone else, has confirmed they work correctly.

If a feature cannot be implimented it will be marked with ❌

If a feature has been superseded by a better feature, it will be marked with �


If a feature doesn't work as expected, please [report this here][bug-reporting]

<details><summary>Windows</summary>
- [x] Windows CLI Mouse Mover
<br />
<br />
- [ ] Windows GUI to start/stop without killing the script
<br />
<br />
- [x] Windows instaler by PowerShell script
  - [x] Move script if not in C:/users/%Username%/Documents - this will allow an updating tool later
  - [x] Install Python if not found
  - [ ] pip install pyautogui
    - [ ] Use --trusted-host pip flag to override SSL certificate issues (this may be necessary in some environments, notably corporate managed networks may strip the SSL certificates)
  - [ ] Offer to create desktop and start menu shortcuts
  - [ ] Cleanup installer
<br />
<br />
- [ ] Windows updating tool
<br />
<br />
</details>

<br />
<br />

<details><summary>MacOS</summary>
- [ ] MacOS CLI Mouse Mover
<br />
<br />
- [ ] MacOS GUI to start/stop without killing the script
<br />
<br />
- [ ] MacOS installer
  - [ ] Move script if not in /users/%Username%/Documents - this will allow an updating tool later
  - [ ] Install Python if not found
  - [ ] pip install pyautogui
    - [ ] Use --trusted-host pip flag to override SSL certificate issues (this may be necessary in some environments, notably corporate managed networks may strip the SSL certificates)
  - [ ] Offer to create desktop and start menu shortcuts
  - [ ] Cleanup installer
<br />
<br />
- [ ] MacOS updating tool
</details>

<br />
<br />

See the [open issues](https://github.com/nyxtryx/Mouse-Mover/issues) for a full list of suggested features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE.txt](https://github.com/othneildrew/MouseMover/blob/master/LICENSE.txt) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

<a href=nyxtryx@dontsp.am> Email me</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<br />
<br />
<br />
<br />

Please also see https://github.com/nyxtryx/mouse-mover/blob/master/images/credit.csv

<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/nyxtryx/mouse-mover.svg?style=for-the-badge
[contributors-url]: https://github.com/nyxtryx/mouse-mover/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nyxtryx/mouse-mover.svg?style=for-the-badge
[forks-url]: https://github.com/nyxtryx/mouse-mover/network/members
[stars-shield]: https://img.shields.io/github/stars/nyxtryx/mouse-mover.svg?style=for-the-badge
[stars-url]: https://github.com/nyxtryx/mouse-mover/stargazers
[issues-shield]: https://img.shields.io/github/issues/nyxtryx/mouse-mover.svg?style=for-the-badge
[issues-url]: https://github.com/nyxtryx/mouse-mover/issues
[license-shield]: https://img.shields.io/github/license/nyxtryx/mouse-mover.svg?style=for-the-badge
[license-url]: https://github.com/nyxtryx/mouse-mover/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dan-mcc/
[windows-cli-install-guide]: https://nyxtryx.github.io/Mouse-Mover/guides/windows-cli-installer/windows-cli-install
[bug-reporting]: https://nyxtryx.github.io/Mouse-Mover/guides/report-a-bug/report-a-bug
[setup]: https://nyxtryx.github.io/Mouse-Mover#setup