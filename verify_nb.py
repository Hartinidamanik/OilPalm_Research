with open('d:/S2/Research/OilPalm_Research/OilPalm_UCFF_Experiments.ipynb', 'r') as f:
    lines = f.read().split('\n')
    for i in range(75, 85):
        if i < len(lines):
            print(f'Line {i}: {repr(lines[i])}')