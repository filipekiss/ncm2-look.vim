# -*- coding: utf-8 -*-

import vim
from ncm2 import Ncm2Source, getLogger
import re
from os.path import isfile
import subprocess

logger = getLogger(__name__)


class Source(Ncm2Source):
    def __init__(self, nvim):
        super(Source, self).__init__(nvim)
        self.executable_look = nvim.call('executable', 'look')
        self.use_vim_spellfile = self.nvim.eval(
            'g:ncm2_look_use_spell') or None

    def on_complete(self, ctx):

        query = ctx['base']

        if not self.executable_look:
            return

        matches = []

        try:
            matches = [
                word.decode('utf-8', errors='ignore')
                for word in self._query_look(query)
            ]

            if re.match('[A-Z][a-z0-9_-]*$', query):
                matches = [word[0].upper() + word[1:] for word in matches]
            elif re.match('[A-Z][A-Z0-9_-]*$', query):
                matches = [word.upper() for word in matches]
        except subprocess.CalledProcessError:
            pass

        if self.use_vim_spellfile:
            try:
                spell_words = [
                    word.decode('utf-8', errors='ignore')
                    for word in self._query_spell(query)
                ]
                if re.match('[A-Z][a-z0-9_-]*$', query):
                    spell_words = [
                        word[0].upper() + word[1:] for word in spell_words
                    ]
                elif re.match('[A-Z][A-Z0-9_-]*$', query):
                    spell_words = [word.upper() for word in spell_words]
                if spell_words:
                    matches = matches + spell_words
            except subprocess.CalledProcessError:
                pass

        if matches:
            self.complete(ctx, ctx['startccol'], matches)
        else:
            return

    def _query_look(self, querystring):
        logger.debug('Running look')
        command = ['look', querystring]

        return subprocess.check_output(command).splitlines()

    def _query_spell(self, querystring):
        logger.debug('Running spell')
        vim_spellfile = self.nvim.eval('&spellfile') or None

        if not self.use_vim_spellfile or not vim_spellfile:
            return []

        spell_words = []
        spellfiles = vim_spellfile.split(',')

        for spellfile in spellfiles:
            if isfile(spellfile):
                logger.debug('Checking Spellfile {}'.format(spellfile))
                command = ['look', querystring, spellfile]
                spell_words = spell_words + subprocess.check_output(
                    command).splitlines()

        return spell_words


source = Source(vim)

on_complete = source.on_complete
