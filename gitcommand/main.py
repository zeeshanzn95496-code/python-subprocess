from git_assistant import git_push

command = input("zeeshan cli>")

if command=="push":
    git_push()

else:
    print(" you entered wrong command, command must be push")