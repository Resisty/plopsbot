# -*- coding: utf-8 -*-
#!/usr/bin/python
# =======================================
#
#  File Name : plugins.py
#
#  Purpose :
#
#  Creation Date : 18-03-2016
#
#  Last Modified : Tue 12 Apr 2016 05:36:45 PM CDT
#
#  Created By : Brian Auron
#
# ========================================

import slackbot.bot
import re
import random
import traceback
import six

def user(msg):
    return msg._client.users[message._get_user_id()]['name']

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

GROUPSTRING = r'''^roll\sdice
                  $|\s
                  ((\s*[\d]+d[\d]+)+)
                  (\swith\s.*\smodifier(|s)\s((\s*[\+-]\d+)+))?'''
GROUPS = re.compile(GROUPSTRING, re.IGNORECASE | re.VERBOSE)
@slackbot.bot.respond_to(GROUPS)
def roll_dice(message, *groups):
    try:
        dice = groups[0]
        try:
            modifiers = groups[4].split()
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

SPINSTRING = r'''spin\sthe\swheel'''
SPIN = re.compile(SPINSTRING, re.IGNORECASE | re.VERBOSE)
@slackbot.bot.respond_to(SPIN)
def spin_wheel(message):
    values = range(5, 105, 5)
    message.reply(str(random.choice(values)))

FINESTRING = '''this\sis\sfine'''
FINE = re.compile(FINESTRING, re.IGNORECASE)
@slackbot.bot.listen_to(FINE)
def this_is_fine(message):
    message.reply('http://gunshowcomic.com/648')

MANATEESTRING = '''[A-Z]{3}'''
MANATEE = re.compile(MANATEESTRING)
@slackbot.bot.listen_to(MANATEE)
def manatee_maybe(message):
    msg = message.body['text']
    nicks = [j['name'] for i,j in message._client.users.items()]
    nickids = [j['id'] for i,j in message._client.users.items()]
    if msg == msg.upper() and len(msg) > 4 and msg.lower() not in nicks:
        manatee = random.randint(1, 34)
        if manatee == 34:
            reply = 'http://i.imgur.com/jxvgPhV.jpg'
        else:
            reply = 'http://calmingmanatee.com/img/manatee%s.jpg' % manatee
    else:
        return
    message.reply(reply)

CLEVELANDSTRING = r'''tell\s(.+)\sto\scome\sto\sCleveland'''
CLEVELAND = re.compile(CLEVELANDSTRING, re.I)
@slackbot.bot.respond_to(CLEVELAND)
def come_to_cleveland(message, *groups):
    who = groups[0]
    message.send('@'+who+': https://www.youtube.com/watch?v=ysmLA5TqbIY')

ENHANCESTRING = r'''enhance'''
ENHANCE = re.compile(ENHANCESTRING, re.I)
@slackbot.bot.listen_to(ENHANCE)
def enhance(message):
    message.send('/me types furiously. "Enhance."')

@slackbot.bot.respond_to(re.compile('h[ae]lp', re.I))
def explore(message, *groups):
    udi = message._get_user_id()
    name = message._client.users[udi]['name']
    (message
     ._client
     .send_message('@%s' % name,
                   'Respond to:'))
    (message
     ._client
     .send_message('@%s' % name,
                   message.docs_reply()))
    (message
     ._client
     .send_message('@%s' % name,
                   'Listen to:'))
    reply = [u'    • `{0}` {1}'.format(v.__name__, v.__doc__ or '')
             for _, v in six.iteritems(message._plugins.commands['listen_to'])]
    (message
     ._client
     .send_message('@%s' % name,
                   u'\n'.join(reply)))

