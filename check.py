import subprocess

data = subprocess.check_output('last')
print(data)

accessFailed = ['last', '-f', '/var/log/btmp']
af_popen = subprocess.Popen(accessFailed, stdout=subprocess.PIPE).stdout
data1 = af_popen.read().strip()
af_popen.close()
print(data1)

loginIP = ['ls', '/var/log/secure', '|', 'xargs', 'grep', '-E', '"[[:digit:]]+\.[[:digit:]]+\.[[:digit:]]+\.[[:digit:]]+"', '-o', '|', 'sort', '|', 'uniq']
lI_popen = subprocess.Popen(loginIP, stdout=subprocess.PIPE).stdout
data2 = lI_popen.read().strip()
lI_popen.close()
print(data2)
'''
logsuccessedIP = ['cat', '/var/log/secure*', '|', 'grep', 'Accepted', '|', 'awk', ''{print $9"\t"$11"\t$14}'', '|', 'sort', '|', 'uniq']
lsI_popen = subprocess.Popen(logsuccessedIP, stdout=subprocess.PIPE).stdout
data = lsI_popen.read().strip()
lsI_popen.close()
print(data)
'''
