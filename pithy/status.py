# -*- coding: utf-8 -*-
# Copyright (C) 2009, 2010  Roman Zimbelmann <romanz@lavabit.com>
# This software is licensed under the GNU GPLv3; see COPYING for details.
"""
This file contains the Hooks and Status classes which store the status
and settings of the program.  Focus your effort on modifying these when
customizing this program with the configuration file.

The predefined values are just failsafe defaults in case the settings file
is missing or doesn't specify all variables/hooks.
"""

from pithy.actions import Actions
from pithy.ext.color import blue, reverse, normal, default, bold

class Hooks(object):
	"""The Hooks Container
	Hooks are functions which get called at specific points in the
	program.  Override them in your config to customize the behaviour.
	"""
	def filename(self, basename, fileobj, level, width):
		return basename

	def get_color(self, file, context):
		"""A very simple colorscheme"""
		attr = reverse if context.selected else normal
		if file.is_dir:
			return blue, default, attr | bold
		return default, default, attr

	def filter(self, filename, path):
		return True  # display all files

	def statusbar(self):
		pass  # never modify the statusbar

	def reload_hook(self):
		pass


class Status(Actions):
	"""The Status Object
	* contains the current status and settings of the program
	* inherits methods for manipulating the status from pithy.actions.Actions
	* can be used as a container for global variables in custom scripts
	"""
	classify = False  # append indicator (one of */=>@|) to entries
	directories_first = True
	draw_bookmarks = False
	hooks = Hooks()
	keymap = None
	ls_l_mode = False
	columns = ([-1, 1],  # [level, width]
	           [ 0, 3],
	           [ 1, 4])
	sort_key = None