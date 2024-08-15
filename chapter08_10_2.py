import logging

def devide(a1, a2):
    return a1 / a2

logging.basicConfig(filename='testlog.log', level=logging.WARNING,
                    format='%(levelname)s:%(asctime)s:%(message)s')

try:
    ret = devide(10, 0)
except:
    logging.exception('test exception message')
logging.shutdown()
