import i3
import time

"""
Shows current window title.

DEPENDENCIES:
    Depends on i3-py!
    pip install i3-py

CONFIG:
    MAX_WIDTH - max title width
    CACHED_TIME - in seconds

If payload from server contains wierd utf-8 (for example one window have something bad in title) - plugin will give empty output UNTIL this window will be closed. I can't fix or workaround that in PLUGIN, problem is in i3-py library. 
"""

MAX_WIDTH = 120
CACHED_TIME = 0.5

def find_focused(tree):
    if type(tree) == list:
        for el in tree:
            res = find_focused(el)
            if res:
                return res

    elif type(tree) == dict:
        if tree["focused"]:
            return tree
        else:
            return find_focused(tree["nodes"] + tree["floating_nodes"])

class Py3status:
    def currentTitle(self, json, i3status_config):
        window = find_focused(i3.get_tree())

        if window and "name" in window: 
            text = len(window["name"]) > MAX_WIDTH and "..." + window["name"][-(MAX_WIDTH-3):] or window["name"]

        return (0, {'full_text': text,
                    'name': 'current-title',
                    'cached_until': time.time() + CACHED_TIME,
                    })
