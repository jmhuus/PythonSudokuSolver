import subprocess
p = subprocess.Popen(["python", "misc2.py"], stdout=subprocess.PIPE)
print("print output: {}".format(p.communicate()))