import subprocess

result = subprocess.run(["python","--version"],
capture_output= True,
shell=True,
text = True
)

print(result.stdout)
print(type(result.stdout))