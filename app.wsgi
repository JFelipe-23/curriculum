import sys
import os
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

base_dir = os.path.dirname(os.path.abspath(__file__))
logging.debug('Base directory: ' + base_dir)

src_path = os.path.join(base_dir, 'src')
sys.path.insert(0, src_path)
logging.debug('Python path added: ' + src_path)

try:
    from curriculum.run import app
    logging.debug('Flask app imported successfully')
    application = app
    logging.debug('Application object created')
except Exception as e:
    logging.error('Error importing Flask app: ' + str(e), exc_info=True)
    raise