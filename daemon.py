import subprocess
import sys, os


def daemon(PYTHON_HOME):
    SCRIPT_HOME = os.path.dirname(sys.argv[0])
    subprocess.Popen('{0}\python.exe {1}\server.py'.format(PYTHON_HOME, SCRIPT_HOME), creationflags=0x00000008)


def main():
    PYTHON_HOME = 'C:\Python27'
    if os.path.exists(PYTHON_HOME):
        daemon(PYTHON_HOME)


if __name__ == '__main__':    
    main()
    
