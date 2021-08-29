def core_page_message_handler(func):
    def wrapper(*args, **kwargs):
        updater, update, context = args
        query = update.callback_query
        if query:
            message = query.message
        else:
            message = update.message
        return func(*args, **kwargs)

    return wrapper


def core_handlers_decorator(func):
    def wrapper(*args, **kwargs):
        updater = args[0]
        return updater.get_core_handlers() + func(*args, **kwargs)

    return wrapper


def main_menu_handlers_decorator(func):
    def wrapper(*args, **kwargs):
        updater = args[0]
        return updater.get_main_menu_handlers() + func(*args, **kwargs)

    return wrapper


def simple_message_handler(func):
    def wrapper(*args, **kwargs):
        updater, update, context = args
        query = update.callback_query
        if query:
            message = query.message
        else:
            message = update.message
        return func(*args, **kwargs)

    return wrapper
