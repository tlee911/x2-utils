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
mod_paths = glob.glob(ws_mods_path)

mapping = {}
for mod_path in mod_paths:
    mod_id = os.path.basename(mod_path)
    mod_file = glob.glob(os.path.join(mod_path, '*.XComMod'))
    if mod_file:
        with open(mod_file[0], 'r') as file:
            data = {}
            for line in file.readlines():
                if line.startswith('Title'):
                    title = ''.join(line.split('=')[1:]).strip()
                    mapping[mod_id] = title
                    break

mapping = sorted(mapping.items())
if SORT_BY_NAME:
    mapping = sorted(mapping, key=lambda item: item[1])

for mod_id, name in mapping:
    print('{id} {name}'.format(id=mod_id, name=name))
