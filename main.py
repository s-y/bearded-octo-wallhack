#!/usr/bin/env python
# encoding: utf-8

import random
import re

import pynotify


def notify(title, message):
    pynotify.init("Basic")
    pynotify.Notification(title, message).show()


def split(s, r='?'):
    s = s.split(r)
    notify("".join(s[1:]) + r, s[0] + r)

with open('phrases.txt', 'r') as phrases:  # .readlines()
    phrases = phrases.readlines()
    while True:
        phrase = re.sub('\s+', ' ', random.choice(phrases))
        if '?' in phrase:
            split(phrase)
        elif '.' in phrase:
            split(phrase, r='.')
        else:
            continue
        break
