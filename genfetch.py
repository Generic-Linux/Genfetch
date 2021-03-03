# -------------------------------------
# Genfetch
# Neofetch, but generic
# Created by VideoToaster, under GPLv2+
# -------------------------------------
import os
import getpass
import sys as inf


with open("/etc/os-release") as os_rel:
	release_info_raw = os_rel.read().strip()

release_info = {}

for info in release_info_raw.split("\n"):
	release_info.update({info.split("=")[0]:info.split("=")[1]})

ver = "v0.0 ALPHA"

attrib = [
  "=-=-=-=-=-=-=-=-=-=-=-=-",
  getpass.getuser() + "@" + os.uname().nodename,
  "Kernel: " + inf.platform,
  "Version: " + ver,
  "OS: " + release_info['NAME'][1:-1],
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
