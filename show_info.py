﻿import os,sys

print("#" * 100, ": os.walk('.')")
a=[print(os.path.join(dp, f)) for dp, dn, filenames in os.walk(".") for f in filenames]

print("#" * 100, ": os.walk(os.environ.get('pythonLocation', ''))")
b=[print(os.path.join(dp, f)) for dp, dn, filenames in os.walk(os.environ.get("pythonLocation", "")) for f in filenames]