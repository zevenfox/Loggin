"""
Examples of using Python's logging facility.
Run this file in Python and observe:
Which messages are actually printed on the console or to a file?
What information is in the message?
For details, see: https://docs.python.org/3/library/logging.html
"""
import logging

def log_demo(logger):
    """Log messages using each of the standard logging levels.
       :param logger: a logging.Logger object for log messages.
    """ 

    # TODO write a log message that uses each of these log levels,
    # debug
    logger.debug('Debug message.')
    # info
    logger.info('User login Successfully.')
    # warning
    logger.warning('Got some problems. Login fail')
    level = logging.WARN + 5  # (custom log level between WARN and ERROR)
    logger.log(level, "User can't login.")
    # error
    logger.error("Error message")
    # critical or fatal
    logger.critical("Alert!!!")


# def console_config():
#     """Configure logging for messages sent to the console.
#     You should call this before creating any logging objects.
#     You can call basicConfig only once.   
#     Subsequent calls have no effect.
#     named attributes you can set using basicConfig are:
#     filename = name of a file to send log messages to
#     filemode = 'a' (append), 'w' (truncate & open for writing)
#     format = a string describing format of log messages
#     stream = name of a StreamHandler to use, cannot use with filename attribute
#     level = the threshold level for log messages
#     See:  help(logging.basicConfig)
#     Ref:  https://docs.python.org/3/library/logging.html#logging.basicConfig
#     """
#     # define a custom format for log messages (use it in your
#     # call to basicConfig)
#     FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
#     logging.basicConfig(level=logging.WARNING, format=FORMAT)


# def file_config():
#     """Configure logging to a file."""
#     # TODO specify a log file, threshold level, format, 
#     #      and append mode so log files are not overwritten
#     # Format should be "(asctime) (logger_name) (levelname) (funcName): (message)"
#     # don't actually print the parenthesis in log messages!
#     #
#     # See: https://docs.python.org/3/library/logging.html#logrecord-attributes
#     FORMAT = '%(asctime)s %(name)s %(levelname)s %(funcName)s %(lineno)s: %(message)s'
#     logging.basicConfig(format=FORMAT, level=logging.WARN, filename="demo.log", filemode='a')


def configure():
    """Configure loggers and log handlers."""
    # write all messages to a file.
    # For a real app, use a configurable absolute path to log file.
    filehandler = logging.FileHandler("demo.log")
    filehandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    filehandler.setFormatter(formatter)
    # add the handler to the root logger, it will handle all log msgs
    root = logging.getLogger()
    root.setLevel(logging.NOTSET)
    root.addHandler(filehandler)

    # Define a console handler for messages of level WARNING or higher
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter(fmt="%(levelname)-8s %(name)s: %(message)s")
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)


if __name__ == "__main__":

    # Call basicConfig with the default settings
    #logging.basicConfig()

    # Call basicConfig with a threshold logging level
    #logging.basicConfig(level=logging.ERROR)  -- fix this

    # Instead of the above, call your own config function:
    # console_config()
    #
    # or:
    # file_config()
    #
    # or:
    configure()
    
    # After configuring logging, 
    # Log some messages to the root logger & observe the output.
    logger = logging.getLogger()
    print("Logging to ", str(logger))
    log_demo(logger)

    #TODO (last exercise) create a logger named "demo" instead
    # of the root logger.