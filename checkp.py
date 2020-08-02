#경유 접속 짜면서 새로 했던 거라서 필요없을 것 같긴한데 그냥 같이 올렸습니다
import paramiko
import sshtunnel

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

'''
with sshtunnel.open_tunnel(
    (REMOTE_SERVER_IP, 443),
    ssh_username="",
    ssh_pkey="/var/ssh/rsa_key",
    ssh_private_key_password="secret",
    remote_bind_address=(PRIVATE_SERVER_IP, 22),
    local_bind_address=('0.0.0.0', 10022)
) as tunnel:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('127.0.0.1', 10022)
    # do some operations with client session
    client.close()
'''

'''
import subprocess
import time
import threading

class SshTunnel(threading.Thread):
    def __init__(self, localport, remoteport, remoteuser, remotehost):
        threading.Thread.__init__(self)
        self.localport = localport 
        self.remoteport = remoteport    
        self.remoteuser = remoteuser    
        self.remotehost = remotehost    
        self.daemon = True              

    def run(self):
        if subprocess.call([
            'ssh', '-N',
                   '-L', str(self.localport) + ':' + self.remotehost + ':' + str(self.remoteport),
                   self.remoteuser + '@' + self.remotehost ]):
            raise Exception ('ssh tunnel setup failed')


if __name__ == '__main__':
    tunnel = SshTunnel(1368, 22, '...', 'localhost')
    tunnel.start()
    time.sleep(1)
    subprocess.call(['curl', 'http://...'])
'''
c.connect( hostname = ip, username = '', password = '', port = '' )

commandLines = "last -f /var/log/btmp"
stdin, stdout, stderr = cli.exec_command(";".join(commandLines))
lines = stdout.readlines()
resultData = ''.join(lines)
for line in stdout.read().splitlines():
	print(line.decode())

commandLines = "ls /var/log/secure | xargs grep -E '[[:digit:]]+\.[[:digit:]]+\.[[:digit:]]+\.[[:digit:]]+' -o | sort | uniq"
stdin, stdout, stderr = cli.exec_command(";".join(commandLines))
lines = stdout.readlines()
resultData = ''.join(lines)
for line in stdout.read().splitlines():
	print(line.decode())

c.close()
