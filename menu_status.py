# -*- coding: utf-8 -*-
import subprocess
import sys
import json
from collections import OrderedDict

from Foundation import *
from AppKit import *
from PyObjCTools import AppHelper

__VERSION__ = "0.1.0"

class QuickAccessAppDelegate(NSObject):
    items = {}
    def applicationDidFinishLaunching_(self, sender):
        self.statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)
        self.statusItem.setHighlightMode_(FALSE)
        self.statusItem.setEnabled_(TRUE)
        self.statusItem.setTitle_("Quick Access")

        # menu
        self.menu = NSMenu.alloc().init()

        # Read JSON.
        self.items = json.load(open("menu_contents.json"), object_pairs_hook=OrderedDict)

        # Action
        for item in self.items:
            if item == "separator":
                self.menu.addItem_(NSMenuItem.separatorItem())
            else:
                menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(item, 'clickEvent:', '')
                self.menu.addItem_(menuitem)

        # Separator and Quit action
        self.menu.addItem_(NSMenuItem.separatorItem())
        menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Quit', 'terminate:', '')
        self.menu.addItem_(menuitem)

        self.statusItem.setMenu_(self.menu)

    def clickEvent_(self, notification):
        mode = notification.title()
        run_command(self.items[mode])

def run_command(command):
    return subprocess.Popen(command.split(" "), stdout=subprocess.PIPE).communicate()

def hide_dock_icon():
    NSApplicationActivationPolicyRegular = 0
    NSApplicationActivationPolicyAccessory = 1
    NSApplicationActivationPolicyProhibited = 2
    NSApp.setActivationPolicy_(NSApplicationActivationPolicyProhibited)

app = NSApplication.sharedApplication()
delegate = QuickAccessAppDelegate.alloc().init()
app.setDelegate_(delegate)
hide_dock_icon()
AppHelper.runEventLoop()
