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
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR INSTALLING AND SETTING UP ICEWM, ROX, AND CONKY

print '======================================='
print 'BEGIN INSTALLING AND CONFIGURING THE DE'

import shutil

def elim_dir (dir_to_elim): 
	if (os.path.exists(dir_to_elim)):
		shutil.rmtree (dir_to_elim)

def create_dir (dir_to_create):
    if (os.path.exists(dir_to_create)):
        shutil.rmtree (dir_to_create)


# Install and configure Conky
os.system ('apt-get install -y conky')
src = dir_develop + '/ui-de/dotconkyrc/conkyrc-regular'
dest = '/home/' + uname + '/.conkyrc'
shutil.copyfile(src, dest)

print 'Install IceWM'
# Install IceWM
os.system('apt-get install -y icewm')
# os.system('apt-get install -y icewm icewm-gnome-support')

# Install ROX-Filer
os.system ('apt-get install -y rox-filer')

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

# Remove background wallpapers for GNOME to save space
print "Removing excess wallpapers"
backgrounds='/usr/share/backgrounds/'
elim_dir (backgrounds+'linuxmint')
elim_dir (backgrounds+'linuxmint-debian')
elim_dir (backgrounds+'linuxmint-katya')
elim_dir (backgrounds+'linuxmint-katya-extra')

print "Adding Swift Linux wallpaper"
# Create directory for Swift Linux wallpaper
dir_wallpaper='/usr/share/backgrounds/swift'
if not (os.path.exists(dir_wallpaper)):
	os.mkdir(dir_wallpaper)

# Copy the wallpaper file to the Swift Linux wallpaper directory
src = dir_develop + '/ui-de/usr_share_backgrounds_swift/rox-regular.jpg'
dest = dir_wallpaper + '/swift.jpg'
shutil.copyfile(src, dest)    

print "Configuring ROX"
# Create the directories for the ROX desktop files
dir_to_create (dir_user + '/.config/rox.sourceforge.net/')
dir_to_create ('/etc/skel/.config/rox.sourceforge.net/')
dir_to_create (dir_user + '/.config/rox.sourceforge.net/ROX-Filer')
dir_to_create ('/etc/skel/.config/rox.sourceforge.net/ROX-Filer')

# Copy the ROX desktop file to the necessary directories
src = dir_develop+'/ui-de/ROX-Filer/pb_swift'
dest = dir_user + '/.config/rox.sourceforge.net/ROX-Filer/pb_swift'
shutil.copyfile(src, dest)
dest = '/etc/skel/.config/rox.sourceforge.net/ROX-Filer/pb_swift'
shutil.copyfile(src, dest)

# Copy the ROX Options file to the necessary directories
src = dir_develop + '/ui-de/ROX-Filer/Options'
dest = dir_user + '/.config/rox.sourceforge.net/ROX-Filer/Options'
shutil.copyfile (src, dest)
dest = '/etc/skel/.config/rox.sourceforge.net/ROX-Filer/Options'
shutil.copyfile (src, dest)

# Copy the ROX globicons file to the necessary directories
src = dir_develop + '/ui-de/ROX-Filer/globicons'
dest = dir_user + '/.config/rox.sourceforge.net/ROX-Filer/globicons'
shutil.copyfile (src, dest)
dest = '/etc/skel/.config/rox.sourceforge.net/ROX-Filer/globicons'
shutil.copyfile (src, dest)

print "Adding/reoplacing IceWM configuration files"
create_dir (dir_user + '/.icewm')
create_dir ('/etc/skel/.icewm')

# theme: carried over from antiX-based Swift Linux
src = dir_develop + '/ui-de/etc_X11_icewm/theme'
dest = dir_user + '/.icewm/theme'
shutil.copyfile (src, dest)
dest = '/etc/X11/icewm/theme'
shutil.copyfile (src, dest)
dest = '/etc/skel/.icewm/theme'
shutil.copyfile (src, dest)

# preferences: carried over from antiX Linux
src = dir_develop + '/ui-de/etc_X11_icewm/preferences'
dest = dir_user + '/.icewm/preferences'
shutil.copyfile(src, dest)
dest = '/etc/X11/icewm/preferences'
shutil.copyfile(src, dest)
dest = '/etc/skel/.icewm/preferences'
shutil.copyfile(src, dest)

# startup: carried over from antiX-based Swift Linux
src = dir_develop + '/ui-de/etc_X11_icewm/startup'
dest = dir_user + '/.icewm/startup'
shutil.copyfile(src, dest)
os.system ('chmod a+rwx ' + dest)
dest = '/etc/X11/icewm/startup'
shutil.copyfile(src, dest)
os.system ('chmod a+rwx ' + dest)
dest = '/etc/skel/.icewm/startup'
shutil.copyfile(src, dest)
os.system ('chmod a+rwx ' + dest)

# keys: carried over from antiX Linux
src = dir_develop + '/ui-de/etc_X11_icewm/keys'
dest = dir_user + '/.icewm/keys'
shutil.copyfile(src, dest)
dest = '/etc/X11/icewm/keys'
shutil.copyfile(src, dest)
dest = '/etc/skel/.icewm/keys'
shutil.copyfile(src, dest)

# winoptions: carried over from antiX Linux
src = dir_develop + '/ui-de/etc_X11_icewm/winoptions'
dest = dir_user + '/.icewm/winoptions'
shutil.copyfile(src, dest)
dest = '/etc/X11/icewm/winoptions'
shutil.copyfile(src, dest)
dest = '/etc/skel/.icewm/winoptions'
shutil.copyfile(src, dest)

# toolbar: carried over from antiX Linux, updated
src = dir_develop + '/ui-de/etc_X11_icewm/toolbar'
dest = dir_user + '/.icewm/toolbar'
shutil.copyfile(src, dest)
dest = '/etc/X11/icewm/toolbar'
shutil.copyfile(src, dest)
dest = '/etc/skel/.icewm/toolbar'
shutil.copyfile(src, dest)

print 'FINISHED INSTALLING AND CONFIGURING THE DE'
print '=========================================='
