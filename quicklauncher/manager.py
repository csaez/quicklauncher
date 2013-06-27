import os
import json
from collections import OrderedDict
from wishlib.si import si


LIMIT = 5  # maximum number of items
SCRIPT_DIR = os.path.join(os.path.dirname(__file__), "scripts")
CACHE_FILE = os.path.join(os.path.dirname(__file__), "config", "cache.json")


def get_data(from_disk=True):
    if from_disk:
        f = file(CACHE_FILE)
        data = json.load(f)
        f.close()
    else:
        data = dict()
        # get cmds
        for cmd in si.Commands:
            # filter commands without arguments or with default values
            if not cmd.Arguments.Count or all([arg.Value for arg in cmd.Arguments]):
                cmd_name = str(cmd.Name)
                data[cmd_name] = cmd_name
        # get custom scripts
        for script in os.listdir(SCRIPT_DIR):
            name = script
            script = os.path.join(SCRIPT_DIR, script)
            if os.path.isfile(script):
                data[name] = script
        f = file(CACHE_FILE, "w+")
        json.dump(data, f, indent=4)
        f.close()
    return OrderedDict(sorted(data.items(), key=lambda x: x[0].lower()))


def find(word):
    index = 0
    result = list()
    for k in get_data().keys():
        if word.lower() in k.lower():
            result.append(k)
            index += 1
        if index >= LIMIT:
            break
    return result
