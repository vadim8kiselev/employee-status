import subprocess
import sys, os


def daemon(PYTHON_HOME, SCRIPT_HOME):    
    pid = subprocess.Popen('{0}\python.exe {1}\server.py'.format(PYTHON_HOME, SCRIPT_HOME), creationflags=0x00000008).pid
    generate_stop_script(pid)


def generate_stop_script(pid):
    with open('stop_daemon.py', 'w') as script:
        script.write('import sys, os' + '\n'
                   + 'os.system("taskkill /pid {0} /f")'.format(str(pid)) + '\n'
                   + 'os.remove(sys.argv[0])')

def main():
    PYTHON_HOME = 'C:\Python27'
    SCRIPT_HOME = os.path.dirname(sys.argv[0])
    if os.path.exists(PYTHON_HOME) and not os.path.exists('stop_daemon.py'):
        daemon(PYTHON_HOME, SCRIPT_HOME)


if __name__ == '__main__':    
    main()
