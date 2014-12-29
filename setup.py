#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
#   LightDM GTK Greeter Settings
#   Copyright (C) 2014 Andrew P. <pan.pav.7c5@gmail.com>, Matko Jun <matko.jun@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License version 3, as published
#   by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranties of
#   MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
#   PURPOSE.  See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import subprocess

try:
    import DistUtilsExtra.auto
except ImportError:
    print(
        'To build lightdm-gtk-greeter-settings you need '
        'python-distutils-extra package')
    sys.exit(1)
assert DistUtilsExtra.auto.__version__ >= '2.18', \
    'needs DistUtilsExtra.auto >= 2.18'


def write_config(libdir, values):
    filename = os.path.join(
        libdir, 'lightdm_gtk_greeter_settings/installation_config.py')
    try:
        f = open(filename, 'w')
        f.write('__all__ = [%s]\n' % ', '.join('"%s"' % k for k in values))
        for k, v in values.items():
            f.write('%s = %s\n' % (k, v))
    except OSError as e:
            print ("ERROR: Can't write installation config: %s" % e)
            sys.exit(1)


class InstallAndUpdateDataDirectory(DistUtilsExtra.auto.install_auto):

    def run(self):
        DistUtilsExtra.auto.install_auto.run(self)

        icons_path = '/usr/share/icons/hicolor'
        if self.root:
            target_data = '/' + os.path.relpath(self.install_data, self.root) + '/'
        else:
            target_data = self.install_data + '/'
        target_pkgdata = target_data + 'share/lightdm-gtk-greeter-settings/'

        values = {'__data_directory__': "'%s'" % (target_pkgdata),
                  '__version__': "%s" % self.distribution.get_version(),
                  '__config_path__': '"/etc/lightdm/lightdm-gtk-greeter.conf"'}
        write_config(self.install_lib, values)
        
        try:
            print ("Updating icon cache ...")
            subprocess.call(['gtk-update-icon-cache', icons_path])
        except OSError as e:
            print ("WARNING: Icon cache update failed: %s" % e)
            print (
                'Try to update icon cache manually by running (as root): '
                'gtk-update-icon-cache ' + icons_path)

DistUtilsExtra.auto.setup(
    name='lightdm-gtk-greeter-settings',
    version='1.0',
    license='GPL-3',
    author='Matko Jun',
    author_email='matko.jun@gmail.com',
    description='Settings editor for LightDM GTK+ Greeter',
    long_description='Settings editor for LightDM GTK+ Greeter',
    url='https://github.com/mjun/lightdm-gtk-greeter-settings',
    cmdclass={'install': InstallAndUpdateDataDirectory},
)
