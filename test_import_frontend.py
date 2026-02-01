import sys, traceback, os

print('cwd:', os.getcwd())
print('initial sys.path[0]:', sys.path[0])
sys.path.insert(0, 'frontend')
print('sys.path[0] after insert:', sys.path[0])
try:
    import veestores_frontend.wsgi as w
    print('Imported veestores_frontend.wsgi OK')
except Exception as e:
    print('Import failed:', type(e).__name__, e)
    traceback.print_exc()
