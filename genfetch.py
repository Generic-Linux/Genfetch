# -------------------------------------
# Genfetch
# Neofetch, but generic
# Created by VideoToaster, under GPLv2+
# -------------------------------------
import os
import getpass
import sys as inf

ver = "v0.0 ALPHA"

attrib = [
  "=-=-=-=-=-=-=-=-=-=-=-=-",
  getpass.getuser() + "@" + os.uname().nodename,
  "[31mKernel:[0m " + inf.platform,
  "[31mVersion:[0m " + ver,
  "=-=-=-=-=-=-=-=-=-=-=-=-"
]
logo = [
  "||[31m||||||||[0m ",
  "||         ",
  "||  [31m|||||| [0m",
  "||      [31m|| [0m",
  "||||||||[31m|| [0m"
]
for i in range(len(logo)):
  print(logo[i] + attrib[i])
