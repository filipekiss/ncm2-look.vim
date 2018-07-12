# -*- coding: utf-8 -*-

import vim
from ncm2 import Ncm2Source, getLogger
import re
from os.path import expanduser, expandvars
import subprocess

logger = getLogger(__name__)


class Source(Ncm2Source):
    def __init__(self, nvim):
        super(Source, self).__init__(nvim)
        self.executable_look = nvim.call('executable', 'look')

    def on_complete(self, ctx):

        query = ctx['base']

        if not self.executable_look:
            return

        try:
            matches = [
                word.decode('utf-8', errors='ignore')
                for word in self._query_look(query)
            ]
            if re.match('[A-Z][a-z0-9_-]*$', query):
                matches = [word[0].upper() + word[1:] for word in matches]
            elif re.match('[A-Z][A-Z0-9_-]*$', query):
                matches = [word.upper() for word in matches]
            self.complete(ctx, ctx['startccol'], matches)
        except subprocess.CalledProcessError:
            return

    def _query_look(self, querystring):
        command = ['look', querystring]

        # if self.words is not None:
        #     command.append(self.words)

        return subprocess.check_output(command).splitlines()


source = Source(vim)

on_complete = source.on_complete
