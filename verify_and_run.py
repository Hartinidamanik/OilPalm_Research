#!/usr/bin/env python3
import json, sys, subprocess, re, os

NB_PATH = r"d:/S2/Research/OilPalm_Research/OilPalm_UCFF_Experiments.ipynb"

def main():
    print("="*60)
    print("OILPALM NOTEBOOK VERIFICATION SCRIPT")
    print("="*60)
    
    try:
        with open(NB_PATH, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        print(f"✓ Loaded notebook ({len(nb['cells'])} cells)\n")
        
    except FileNotFoundError:
        print(f"✗ File not found: {NB_PATH}")
        return 1
    
    pip_found, torch_avail = False, False
    
    for i, cell in enumerate(nb['cells']):
        source = ''.join(cell.get('source', '')) if isinstance(cell['source'], list) else str(cell.get('source', ''))
        
        # Check for pip install
        if '%pip install' in source or '!pip install' in source:
            print(f"✓ Cell {i} has pip install")
            pip_found = True
            
            # Extract and run pip install command
            match = re.search(r'%?pip\s+install\s+(\S+\s*,?\s*)+', source)
            if match:
                pkgs = match.group(1).strip()
                try:
                    result = subprocess.run(['pip', 'install'] + pkgs.split(','), capture_output=True, text=True, timeout=300)
                    print(f"  pip install returned {result.returncode}")
                    print(result.stdout[-500:] if result.stdout else "")
                    print(result.stderr[-500:] if result.stderr else "")
                except Exception as e:
                    print(f"! pip error: {e}")
            
            # Check torch import in this cell or subsequent cells up to next code cell
            for j in range(max(0, i-2), min(len(nb['cells']), i+3)):
                sc = nb[j].get('source', '')
                src_str = ''.join(sc) if isinstance(sc, list) else str(sc)
                if 'import torch' in src_str:
                    print(f"  → Cell {j} has torch import")
                    try:
                        result = subprocess.run(['python', '-c', 'import torch; print(torch.__version__)'], capture_output=True, text=True, timeout=120)
                        if result.returncode == 0:
                            print(f"  ✓ Torch version: {result.stdout.strip()}")
                            torch_avail = True
                        else:
                            print(f"  ✗ Torch import failed")
                    except Exception as e:
                        print(f"  ! Torch check error: {e}")
    
    if not pip_found:
        print("\n⚠ No pip install found in notebook!")
    else:
        print("\n✓ Pip installation verification complete")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())