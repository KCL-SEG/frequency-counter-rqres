"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes HERE
    items = [str(i) for i in items]
    myset = set(items)
    
    for item in myset:
        freq = items.count(item)
        frequencies[str(item)] = freq

    return frequencies
    
