import subprocess
import sys, os
import time

def daemon(PYTHON_HOME, SCRIPT_HOME):
    pid = subprocess.Popen('{0}\python.exe "{1}\server.py"'.format(PYTHON_HOME, SCRIPT_HOME), creationflags=0x00000008).pid
    generate_stop_script(SCRIPT_HOME, pid)


def generate_stop_script(HOME, pid):
    with open('{0}\stop_daemon.py'.format(HOME), 'w') as script:
        script.write('import sys, os' + '\n'
                   + 'os.system("taskkill /pid {0} /f")'.format(str(pid)) + '\n'
                   + 'os.remove(sys.argv[0])' + '\n'
                   + 'os.remove("index.html")')

def main():
    PYTHON_HOME = sys.exec_prefix
    SCRIPT_HOME = os.path.dirname(sys.argv[0])
    
    if os.path.exists(PYTHON_HOME) and not os.path.exists('{0}\stop_daemon.py'.format(SCRIPT_HOME)):
        daemon(PYTHON_HOME, SCRIPT_HOME)


if __name__ == '__main__':
    main()
