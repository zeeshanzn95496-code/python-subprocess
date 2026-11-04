import subprocess

result = subprocess.run(["git","status"],capture_output=True,text=True
                        )

if result.returncode==0:
    print("git is working")
    print(result.stdout)
else:
    print("git command failed")
    print(result.stderr)