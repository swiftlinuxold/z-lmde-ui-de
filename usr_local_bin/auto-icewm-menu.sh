# Filename:      auto-icewm-menu.sh
# Purpose:       automate icewm menu in conjunction with icewm-xdg-menu
# Authors:       anticapitalista for antiX
# Latest change: 05 December 2010
# Thanks to secipolla
################################################################################

#!/bin/sh

icewm-xdg-menu --terminal "roxterm -e %s" --default-entry-icon /usr/share/icons/Buuf-Deuce/128x128/apps/alacarte.png --with-theme-paths --theme Buuf-Deuce --entire-menu > ~/.icewm/application  
