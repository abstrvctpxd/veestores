import os
import sys


def _exec_gunicorn(module, port_env='PORT'):
    port = os.environ.get(port_env, '5000')
    args = ['gunicorn', module, '--bind', f'0.0.0.0:{port}', '--pythonpath', '.']
    os.execvp('gunicorn', args)


def backend_entry():
    _exec_gunicorn('backend.run:app')


def frontend_entry():
    _exec_gunicorn('frontend.run:app')


if __name__ == '__main__':
    # allow manual testing
    if len(sys.argv) > 1 and sys.argv[1] == 'frontend':
        frontend_entry()
    else:
        backend_entry()
