#!/usr/bin/python
# =======================================
#
#  File Name : runbot.py
#
#  Purpose :
#
#  Creation Date : 18-03-2016
#
#  Last Modified : Mon 21 Mar 2016 12:39:16 PM CDT
#
#  Created By : Brian Auron
#
# ========================================

import slackbot.bot

CONFIG = 'config.yml'

def main():
    bot = slackbot.bot.Bot()
    bot.run()

if __name__ == '__main__':
    main()
