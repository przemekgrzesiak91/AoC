import subprocess

year = 2017
path0 = str(year) + '/data/day'

for i in range(1,26):
    path = path0 + str(i)+'.txt'
    command = ('aocd ' + str(i) + ' 2017 > '+ path )

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
