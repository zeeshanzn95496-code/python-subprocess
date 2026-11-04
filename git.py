import subprocess

commands= [
    ["git","status"],
    ["git","--version"],
    ["git","branch"],
    ["git","log","--oneline"]
    ]

for command in commands:
    result= subprocess.run(command,capture_output=True,text=True)
    print(result.stdout)

