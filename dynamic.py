import subprocess

command=input("enter git command:")
allowed=["branch","log"]


if command in allowed:

 result = subprocess.run(["git",command],capture_output=True,text=True)

 if result.returncode==0:
     print("command executed")
     print(result.stdout)
 else:
     print("error")
     print(result.stderr)

else:
   print("invalid command")