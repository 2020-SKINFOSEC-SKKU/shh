import os
import paramiko

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cli.connect('115.145.212.130', username = '2019314656', password = '******', port=8080)

stdin, stdout, stderr = cli.exec_command("cat access.log | awk '{print $4}' | awk -F":" '{arr [$2]+=1} END {for(i in arr) {print i "\t"":"arr[i]}}' | sort")
output = (stdout.read())
save = open('weblog.txt', 'w')
save.write(output)
save.close()
cli.close()


