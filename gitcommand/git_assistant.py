import subprocess

def git_push():
    subprocess.run(["git","add","."])

    message = input("enter message to commit:")

    subprocess.run(["git","commit","-m",message])

    subprocess.run(["git","push"]) 