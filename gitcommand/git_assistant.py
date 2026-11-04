import subprocess

def git_push():
    subprocess.run(["git","add","."])

    message = input("enter commit message:")

    subprocess.run(["git","commit","-m",message])

    subprocess.run(["git","push"]) 