import subprocess
import tempfile
import time


def run_python(code: str, timeout: int = 10) -> dict:
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
        fname = f.name

    start = time.time()
    try:
        p = subprocess.run(
            ["python", fname],
            capture_output=True,
            timeout=timeout,
            text=True
        )
        return {
            "stdout": p.stdout,
            "stderr": p.stderr,
            "returncode": p.returncode,
            "runtime": round(time.time() - start, 2)
        }
    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out"}
