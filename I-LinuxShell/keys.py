from prompt_toolkit.key_binding.defaults import load_key_bindings_for_prompt
from prompt_toolkit.keys import Keys

class  Keybindings(object):
    register = load_key_bindings_for_prompt()
    
  @register.add_bindings(Keys.H)
  def _(event):
        pass
