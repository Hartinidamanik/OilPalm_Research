# Package install commands extracted from notebook cell
PACKAGES = ['torch', 'torchvision', 'matplotlib']

# Run pip install
import subprocess, sys
result = subprocess.run([sys.executable, '-m', 'pip', 'install'] + PACKAGES)
print(f"Installation returned code: {result.returncode}")
print(result.stderr[-1000:] if result.stderr else "")