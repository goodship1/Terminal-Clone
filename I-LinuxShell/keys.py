import os
from prompt_toolkit.key_binding.defaults import load_key_bindings_for_prompt
from prompt_toolkit.keys import Keys

class KeyBindings(object):
	
	register = load_key_bindings_for_prompt()
	
	@register.add_binding(Keys.ControlE)
	def _(event):
        """control E exits the shell"""
		event.cli.run_in_terminal(os._exit(0))
	
	@register.add_binding(keys.ControlC)
	def _(event):
		""" control c gets current working directory"""
		event.cli.current_buffer.insert_text(os.getcwd())
	
	@register.add_binding(Keys.ControlD)
	def _(event):
		"""control-D for change directory"""
		event.cli.current_buffer.insert_text("cdir")
	
	@register.add_bindings(keys.ControlH)
	def _(event):
		event.cli.current_buffer.insert("h")
	
	
	
	
