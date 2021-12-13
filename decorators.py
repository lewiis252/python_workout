# define a decorator

def log(original_func):
    def new_func(*args, **kwargs):
        with open('log.txt', 'w') as logfile:
            logfile.write()