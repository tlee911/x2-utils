# This script prints out all your Steam Workshop mods for XCOM2 and
# sorts them by name or ID.  Useful for locating the source code of
# an installed mod.

# Configuration
# ==================================================

STEAM_PATH = 'C:\Program Files (x86)\Steam'
WS_SUB_DIR = 'steamapps\workshop\content'
X2_ID = '268500'
SORT_BY_NAME = True

# ==================================================


import os, glob

ws_mods_path = os.path.join(STEAM_PATH, WS_SUB_DIR, X2_ID, '*')
mods = glob.glob(ws_mods_path)

mapping = {}
for mod in mods:
    id = os.path.basename(mod)
    mod_file = glob.glob(os.path.join(mod, '*.XComMod'))
    if mod_file:
        with open(mod_file[0], 'r') as file:
            data = {}
            for line in file.readlines():
                if line.startswith('Title'):
                    title = ''.join(line.split('=')[1:]).strip()
                    mapping[id] = title
                    break

mapping = sorted(mapping.items())
if SORT_BY_NAME:
    mapping = sorted(mapping, key=lambda item: item[1])

for key, value in mapping:
    print(key, value)
