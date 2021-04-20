from .decorators import *


class HelpersHandler:
    @simple_message_handler
    def undefined_cmd_msg(self, update, context):
        msg = update.message.reply_text(
            self.reply_manager.get_message('undefined_cmd_msg'),
            parse_mode='HTML', )
        self.add_message_to_history(context, msg)
