import subprocess
bashcommand = "git"
arg = "diff"
path = "."
process = subprocess.Popen([bashcommand, arg, path], stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
print("*"*50)
print(error)
