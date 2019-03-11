import CeleryPy
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
cmd='ls {}'.format(dir_path)
url='https://bootstrap.pypa.io/get-pip.py'
try:
    from urllib import request
    request.urlretrieve(url, '{}/get-pip.py'.format(dir_path))
    f = os.popen(cmd)
    out = f.read()
    CeleryPy.send_message(message=str(out), message_type='success', channel='toast')
except ImportError:
    CeleryPy.send_message(message='Module error', message_type='error', channel='toast')





