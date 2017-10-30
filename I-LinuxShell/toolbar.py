from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict


class ToolBar(object):
    
    toolBarStyle = style_from_dict({
		Token.Toolbar: '#gggggg bg:#444444',
		})
    
    def get_bottom_toolbar_tokens(self,cli):
      return [(Token.Toolbar,"Control-E [Exit] Control-S [SH] Control-T [tod] Control-A [shows all commands]")]
