#              error handling

import subprocess
result = subprocess.run(["git","wrongcommand"],
                        capture_output=True,text=True,)

if result.returncode==0:
    print("command executed successfully")
    print(result.stdout)
else:
    print("something went wrong")
    print(result.stderr)