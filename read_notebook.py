#!/usr/bin/env python3
import json, sys

# Read the notebook file
with open(sys.argv[1], 'r', encoding='utf-8-sig') as f:
    try:
        data = json.load(f)
        cells = data.get('cells', [])
        
        print("="*60)
        print("NOTEBOOK FILE READ SUCCESS")
        print("="*60)
        
        for i, cell in enumerate(cells):
            cell_type = cell.get('cell_type', 'unknown')
            source_lines = cell.get('source', '') if isinstance(cell['source'], list) else cell['source'].split('\n')
            
            source_preview = '\n'.join(source_lines[:10])  # First 10 lines
            
            print(f"\nCell {i} ({cell_type}):")
            print("-"*40)
            
            # Check for pip install cells
            if 'pip' in source_preview.lower() or 'install' in source_preview.lower():
                print(source_preview)
        print("\n" + "="*60)
        print("TOTAL CELLS:", len(cells))
        print("="*60)
        
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
except Exception as e:
    print(f"Error: {e}")