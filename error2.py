import subprocess

try:
    subprocess.run(
        ["git", "wrongcommand"],
        check=True
    )

    print("Success!")

except subprocess.CalledProcessError:
    print("Git command failed!")