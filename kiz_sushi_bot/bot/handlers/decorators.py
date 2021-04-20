def core_page_message_handler(func):
    """Decorator adds received message to history and clears old message history"""

    def wrapper(*args, **kwargs):
        updater, update, context = args
        query = update.callback_query
        if query:
            message = query.message
        else:
            message = update.message
        # updater.clear_messages(context, message.chat.id)
        # updater.add_message_to_history(context, message)
        return func(*args, **kwargs)

    return wrapper


def core_handlers_decorator(func):
    """Decorator adds core handlers to list"""

    def wrapper(*args, **kwargs):
        updater = args[0]
        return updater.get_core_handlers() + func(*args, **kwargs)

    return wrapper


def main_menu_handlers_decorator(func):
    """Decorator adds main menu handlers to list"""

    def wrapper(*args, **kwargs):
        updater = args[0]
        return updater.get_main_menu_handlers() + func(*args, **kwargs)

    return wrapper


def simple_message_handler(func):
    """Decorator adds received message to history"""

    def wrapper(*args, **kwargs):
        updater, update, context = args
        query = update.callback_query
        if query:
            message = query.message
        else:
            message = update.message
        # updater.add_message_to_history(context, message)
        return func(*args, **kwargs)

    return wrapper
