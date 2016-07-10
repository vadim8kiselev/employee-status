import SimpleHTTPServer
import SocketServer
import ctypes
import sys, os

    
def destop_is_unlocked():
    user = ctypes.windll.User32
    return user.SwitchDesktop(user.OpenDesktopA("default", 0, False, 0x0100))
    

def check_desktop_status():
    desktop_username = os.getenv('username')
    if destop_is_unlocked():
        response = '{0}<br/>is in the workplace'.format(desktop_username)
    else:
        response = '{0}<br/>is <b>not</b> in the workplace'.format(desktop_username)
        
    with open('index.html', 'w') as page:
        template_file = '{0}\\template.html'.format(os.path.dirname(sys.argv[0]))
        try:
            with open(template_file) as template:
                page.write(template.read().replace('$', response))
        except IOError, err:
            page.write('<h1>{0}<br/><a href="https://github.com/vadim8kiselev/employee-status/">Download</a></h1>'.format(response))


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        check_desktop_status()
        if self.path.startswith('/'):
            self.path = '/index.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


def main():
    try:
        server = SocketServer.TCPServer(('', 8888), Handler)
        server.serve_forever()
    except BaseException, err:
        os.remove('index.html')
        print err

if __name__ == '__main__':    
    main()
