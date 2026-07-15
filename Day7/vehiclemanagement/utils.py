def log_action(func):
    """
    A decorator that logs when a method is called and finished.
    """
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__}")
        return result
    return wrapper