# -------------------------------------
# Genfetch
# Neofetch, but generic
# Created by VideoToaster, under GPLv2+
# Modified by mugman
# -------------------------------------
import os
import getpass
import distro

ver = "v0.0 ALPHA"

attrib = [
  "=-=-=-=-=-=-=-=-=-=-=-=-",
  getpass.getuser() + "@" + os.uname().nodename,
  "Kernel: " + os.uname().release,
  f"OS: {' '.join(distro.linux_distribution(full_distribution_name=True))}",
  "Version: " + ver,
  "=-=-=-=-=-=-=-=-=-=-=-=-"
]
logo = [
  "|||||||||| ",
  "||         ",
  "||  |||||| ",
  "||      || ",
  "|||||||||| "
]
for i in range(len(logo)):
  print(logo[i] + attrib[i])
