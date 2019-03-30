from PyInquirer import style_from_dict, Token, prompt, Separator
from enum import Enum
import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

class ConsoleSelectionType(Enum):
	DONE = "done"
	BACK = "back"
	VALUE = "value"
	FORWARD = "forward"

class ConsoleSelection:

	def __init__(self, value, selection_type):
		self._value = value
		self._selection_type = selection_type

	def selection_type(self):
		return self._selection_type

	def value(self):
		return self._value

BACK = {
	'name': "BACK",
	'value': ConsoleSelection("BACK", ConsoleSelectionType.BACK)
}
DONE = {
	'name': "DONE",
	'value': ConsoleSelection("DONE", ConsoleSelectionType.DONE)
}

class Console:

	def __init__(self):
		self._selection = []

	def set_menu(self, menu):
		self._selection = []
		self._menu = menu

	def render(self):
		while True:
			screen = self._menu
			for selection in self._selection:
				screen = screen['options'][selection]
			console_selection = self.render_screen(screen)
			if console_selection.selection_type() == ConsoleSelectionType.FORWARD:
				self._selection.append(console_selection.value())
			elif console_selection.selection_type() == ConsoleSelectionType.BACK:
				self._selection.pop()
			elif console_selection.selection_type() == ConsoleSelectionType.DONE:
				break
		self._menu["confirm"]()

	def render_screen(self, screen):
		console_options = []
		for (key, option) in screen["options"].items():
			if "value" in option:
				value = {
					'name': option["name"],
					'value': ConsoleSelection(option["value"], ConsoleSelectionType.VALUE)
					}
				console_options.append(value)
			else:
				value = {
					'name': option["name"],
					'value': ConsoleSelection(key, ConsoleSelectionType.FORWARD)
					}
				console_options.append(value)
		if len(self._selection) > 0:
			console_options.append(Separator())
			console_options.append(BACK)
		else:
			console_options.append(Separator())
			console_options.append(DONE)
		questions = [{
			'type': 'list',
			'name': 'question',
			'message': screen["name"],
			'choices': console_options
		}]
		answer = prompt(questions)
		sys.stdout.write(CURSOR_UP_ONE)
		sys.stdout.write(ERASE_LINE)
		selection = answer["question"]
		if selection.selection_type() == ConsoleSelectionType.VALUE:
			should_continue = screen["confirm"](selection.value())
			if should_continue:
				return selection
			return DONE["value"]
		return selection
