#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import chain
import random
from errbot import BotPlugin

CONFIG_TEMPLATE = {
  'FLAG': 'heyyou',
  'PREFIX': '',
  'SUFFIX': '',
}

class HeyYou(BotPlugin):
    def callback_message(self, mess):
        if self.config['FLAG'] in mess.body:
          room = self.query_room(mess.frm.channelid)
          occupants = list(set([ii.username for ii in room.occupants]) - set(self.bot_identifier.username))
          person = random.choice(occupants)
          response = '{0} @{1}{2}'.format(self.config['PREFIX'], person, self.config['SUFFIX'])
          response = response.strip()
          self.send(self.build_identifier('#{0}'.format(mess.frm.channelname)), response)

    def get_configuration_template(self):
        """Defines the configuration structure this plugin supports

        You should delete it if your plugin doesn't use any configuration like this"""
        return CONFIG_TEMPLATE

    def configure(self, configuration):
        if configuration is not None and configuration != {}:
            config = dict(chain(CONFIG_TEMPLATE.items(),
                                configuration.items()))
        else:
            config = CONFIG_TEMPLATE
        super().configure(config)