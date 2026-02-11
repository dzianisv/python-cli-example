import subprocess

def test_hello():
    result = subprocess.run(["python3", "hello.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, World!", "Output is not as expected"