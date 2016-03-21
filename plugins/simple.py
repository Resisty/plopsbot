#!/usr/bin/python
# =======================================
#
#  File Name : plugins.py
#
#  Purpose :
#
#  Creation Date : 18-03-2016
#
#  Last Modified : Mon 21 Mar 2016 04:41:35 PM CDT
#
#  Created By : Brian Auron
#
# ========================================

import slackbot.bot
import re
import random
import traceback

SHENANISTRING = '''what's the name of that place you like with all the goofy\
 shit on the walls?'''
SHENANIGANS = [SHENANISTRING, re.IGNORECASE]
@slackbot.bot.respond_to(*SHENANIGANS)
def shenanigans(message):
    message.reply('You mean Shenanigans? You guys talkin\' \'bout\
 shenanigans?')

HI = re.compile(r'hi(|!)$', re.IGNORECASE)
@slackbot.bot.respond_to(HI)
def hi(message, groups):
    message.reply('Yo!')

TOWELSTRING = '''you're a towel'''
TOWEL = re.compile(TOWELSTRING, re.IGNORECASE)
@slackbot.bot.listen_to(TOWEL)
def towel(message):
    message.reply('''YOU'RE a towel!''')

PYTHONTOWELSTRING = '''you're a (bot|python|robot) towel'''
PYTHONTOWEL = re.compile(PYTHONTOWELSTRING, re.IGNORECASE)
@slackbot.bot.listen_to(PYTHONTOWEL)
def towel(message):
    message.reply('''What did you say?!''')

MARTINSTRING = '''martin'''
MARTIN = re.compile(MARTINSTRING, re.IGNORECASE)
@slackbot.bot.listen_to(MARTIN)
def martin(message):
    message.reply('''s/Martin/1950's newscast guy/g''')

GROUPSTRING = r'''^roll\sdice($|\s((\s*[\d]+d[\d]+)+)($|\swith\s.*\smodifier(|s)\s((\s*[\+-]\d+)+)))'''
GROUPS = re.compile(GROUPSTRING, re.IGNORECASE | re.VERBOSE)
@slackbot.bot.respond_to(GROUPS)
def roll_dice(message, *groups):
    try:
        dice = groups[1]
        try:
            modifiers = groups[5].split()
            modifiers = [int(m) for m in modifiers]
        except AttributeError as e:
            modifiers = [0]
        if not dice:
            total = random.randint(1,6)
            results = ['1d6: %d' % total]
        else:
            dice_sets = dice.split()
            total = 0
            results = []
            for dice_set in dice_sets:
                nums = dice_set.split('d')
                number = int(nums[0])
                size = int(nums[1])
                val = sum([random.randint(1, size) for i in range(number)])
                val += sum(modifiers)
                total += val
                results.append('%s: %d' % (dice_set, val))
        results = ', '.join(results)
        message.reply('''Got dice sets: %s\nTotal: %s''' % (results, total))
    except:
        print traceback.format_exc()

PINGSTRING = r'''^([^\w\s]*|_*)
                  ([a-zA-Z]+)
                  ING
                  ([^\w\s]*|_*)
                  ( ME( {nick})?)?$'''
PING = re.compile(PINGSTRING, re.IGNORECASE | re.VERBOSE)
@slackbot.bot.listen_to(PING)
def ping(message, *groups):
    letter = groups[1]
    pre, suf = groups[0], groups[2]
    msg = 'ong' if letter[-1].islower() else 'ONG'
    msg = pre+letter+msg+suf
    message.reply(msg)

WHELPSTRING = '''whelps'''
WHELPS = re.compile(WHELPSTRING, re.IGNORECASE)
@slackbot.bot.listen_to(WHELPS)
def martin(message):
    for i in ['WHELPS','LEFT SIDE','EVEN SIDE',
              'MANY WHELPS','NOW','HANDLE IT!']:
        message.reply(i)


#@slackbot.bot.listen_to('.*')
#def explore(message):
#    udi = message._get_user_id()
#    name = message._client.users[udi]['name']
#    print 'Found message from %s' % name
#    #message.send('@%s: found your name!' % name)
