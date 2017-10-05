import os
from prompt_toolkit.key_binding.defaults import load_key_bindings_for_prompt
from prompt_toolkit.keys import Keys

class KeyBindings(object):
	
	register = load_key_bindings_for_prompt()
	
	@register.add_binding(Keys.ControlE)
	def _(event):
        """control E exits the shell"""
		event.cli.run_in_terminal(os._exit(0))
	
