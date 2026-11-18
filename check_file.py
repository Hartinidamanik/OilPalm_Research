import sys
with open(sys.argv[1], 'r') as f:
    content = f.read()
    print("FILE LENGTH:", len(content))
    print("\n\n=== LINES 78-83 ===")
    lines = content.split('\n')
    for i in range(max(0, 75), min(len(lines), 85)):
        print(f"{i}: {repr(lines[i])}")