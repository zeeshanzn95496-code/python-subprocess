from git_assistant import git_push

command = input("zeeshan cli>")

if command=="push":
    git_push()

else:
    print("unknown command")