from git_assistant import git_push

command = input("cli>")

if command=="push":
    git_push()

else:
    print(" you entered wrong command, input command must be only push")