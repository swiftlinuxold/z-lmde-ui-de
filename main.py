#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'	
else:
	dir_develop='/home/'+uname+'/develop'

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR INSTALLING AND SETTING UP ICEWM and ROX FILER

print '======================================='
print 'BEGIN INSTALLING AND CONFIGURING THE DE'
print 'Install IceWM'
# Install IceWM
os.system('apt-get install -y icewm')
# os.system('apt-get install -y icewm icewm-gnome-support')

import shutil
def elim_dir (dir_to_elim): 
	if (os.path.exists(dir_to_elim)):
		shutil.rmtree (dir_to_elim)

print 'Removing excess themes'
# Only default, icedesert, nice, nice2, win95, and yellowmotif remain.
# These themes are easy to read and easy on space.
# IceWM themes options are under Main menu -> Settings -> Themes
themes='/usr/share/icewm/themes/'
elim_dir (themes+'gtk2')
elim_dir (themes+'Infadel2')
elim_dir (themes+'metal2')
elim_dir (themes+'motif')
elim_dir (themes+'warp3')
elim_dir (themes+'warp4')

# Install ROX-Filer and ROXTerm
os.system ('apt-get install -y rox-filer roxterm')

# Activate ROX Pinboard
# os.system ('rox --pinboard=swift')

# print 'Adding/replacing IceWM files'

# src=dir_develop+'/ui-icewm/usr_local_bin/auto-icewm-menu.sh'
# dest='/usr/local/bin/auto-icewm-menu.sh'
# shutil.copyfile(src, dest)

# src=dir_develop+'/ui-icewm/usr_local_bin/icewm-xdg-menu'
# dest='/usr/local/bin/icewm-xdg-menu'
# shutil.copyfile(src, dest)

src=dir_develop+'/ui-de/etc_X11_icewm/keys'
dest='/etc/X11/icewm/keys'
shutil.copyfile(src, dest)

# src=dir_develop+'/ui-icewm/home_user_doticewm/menu'
# dest='/home/'+uname+'/.icewm/menu'
# shutil.copyfile(src, dest)

src=dir_develop+'/ui-de/etc_X11_icewm/preferences'
dest='/etc/X11/icewm/preferences'
shutil.copyfile(src, dest)

# src=dir_develop+'/ui-icewm/home_user_doticewm/startup'
# dest='/home/'+uname+'/.icewm/startup'
# shutil.copyfile(src, dest)

src=dir_develop+'/ui-de/etc_X11_icewm/theme'
dest='/etc/X11/icewm/theme'
shutil.copyfile(src, dest)

# src=dir_develop+'/ui-icewm/home_user_doticewm/toolbar'
# dest='/home/'+uname+'/.icewm/toolbar'
# shutil.copyfile(src, dest)

src=dir_develop+'/ui-de/etc_X11_icewm/winoptions'
dest='/etc/X11/icewm/winoptions'
shutil.copyfile(src, dest)

print 'FINISHED INSTALLING AND CONFIGURING THE DE'







# Configure JWM
# Add /home/(username)/.jwmrc and /home/(username)/.jwmrc-tray

# src = dir_develop + '/ui-wm/user/dot_jwmrc'
# dest = '/home/'+uname+'/.jwmrc'
# shutil.copy2 (src, dest)

# src = dir_develop + '/ui-wm/user/dot_jwmrc-tray'
# dest = '/home/'+uname+'/.jwmrc-tray'
# shutil.copy2 (src, dest)

# Add /home/(username)/.jwm
# src = dir_develop + '/ui-wm/user_dot_jwm'
# dest = '/home/'+uname+'/.jwm'
# if (os.path.exists(dest)):
#	shutil.rmtree (dest)
# shutil.copytree (src, dest)

# Add /usr/local/jwmconfig2
# src = dir_develop + '/ui-wm/usr_local_jwmconfig2'
# dest = '/usr/local/jwmconfig2'
# if (os.path.exists(dest)):
#	shutil.rmtree (dest)
# shutil.copytree (src, dest)

# Replace /etc/xdg
# print 'Replacing /etc/xdg'
# os.mkdir('/etc/xdg')
# src = dir_develop + '/ui-wm/etc_xdg'
# dest = '/etc/xdg'
# if (os.path.exists(dest)):
#	shutil.rmtree (dest)
# shutil.copytree (src, dest)
