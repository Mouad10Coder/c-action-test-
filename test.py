import os, subprocess

# Settings
TEST_DIR = os.getcwd()        # Use current directory instead of hardcoded /tests
CODE_FILE = "main.c"
COMPILER_TIMEOUT = 10.0
RUN_TIMEOUT = 10.0

code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

print("Building...")
try:
    ret = subprocess.run(["gcc", code_path, "-o", app_path],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          timeout=COMPILER_TIMEOUT)
except subprocess.TimeoutExpired:
    print("Compilation timed out!")
    exit(1)

if ret.returncode != 0:
    print("Compilation failed!")
    print(ret.stderr.decode())
    exit(1)

print("Build successful!")

print("Running...")
try:
    run_ret = subprocess.run([app_path],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              timeout=RUN_TIMEOUT)
except subprocess.TimeoutExpired:
    print("Execution timed out!")
    exit(1)

print("Output:")
print(run_ret.stdout.decode())

if run_ret.returncode != 0:
    print("Program exited with an error:")
    print(run_ret.stderr.decode())
    exit(1)

print("Success!")
