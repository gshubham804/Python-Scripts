# import subprocess
# cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
# proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# for line in proc.stdout:
#     if line.rstrip():
#         # only print lines that are not empty
#         # decode() is necessary to get rid of the binary string (b')
#         # rstrip() to remove `\r\n`
#         print(line.decode().rstrip())

import subprocess
cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description,Id,Path'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    if not line.decode()[0].isspace():
        print(line.decode().rstrip())

        https://github.com/search?l=Python&q=Track+windows+app+usage+time&type=Repositories