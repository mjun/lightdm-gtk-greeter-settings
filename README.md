Settings editor for LightDM GTK+ Greeter
========================================

![Settings editor for LightDM GTK+ Greeter](screenshot.png?raw=true "Settings editor for LightDM GTK+ Greeter")

Settings editor for LightDM GTK+ Greeter is a small GUI written in Python which lets you modify various LightDM GTK+ Greeter settings, such as the theme, font, background, window position and more, settings which otherwise can only be set by modifying the greeter configuration files.

This is a port of [(Debian/Ubuntu based) lightdm-gtk-greeter-settings project](https://launchpad.net/lightdm-gtk-greeter-settings) for Enterprise Linux 7 based distributions (CentOS7/RedHat7).

Features
--------
 *  Appearance: change LightDM GTK+ Greeter theme, icons, font (with DPI/antialias/subpixel rendering and hinting settings), change the background image or set it to a color, enable user wallpaper if available or change the default user image;
 *  Panel: change the clock format and redefine indicators (enable/disable indicators or reorder them);
 *  Window position: change the login dialog window position (supported in lightdm versions >= 1.7.0)
 *  Misc: enable/disable onscreen keyboard, set the timeout until the screen blanks.

Prerequisites
-------------
 *  python-distutils-extra >= 2.18

Installation
------------
In project root run (as root):
    python setup.py install
    
Optionally, if gtk icon cache update fails, run (as root):
    gtk-update-icon-cache /usr/share/icons/hicolor

Authors
-------
Matko Jun <matko.jun@gmail.com> EL7 port
Andrew P. <pan.pav.7c5@gmail.com> original project

References
----------
[EL7 port page] (https://github.com/mjun/lightdm-gtk-greeter-settings)
[Original project page] (https://launchpad.net/lightdm-gtk-greeter-settings)
[Original project description] (http://www.webupd8.org/2014/10/lightdm-gtk-greeter-settings-gui.html)

License
-------
[GNU General Public License version 3](LICENSE?raw=true "LICENSE")

Support or Contact
------------------
If you have and questions or problems with this application feel free to contact me at: matko.jun@gmail.com

