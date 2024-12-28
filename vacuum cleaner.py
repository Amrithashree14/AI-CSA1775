class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.cleaned = 0

    def clean(self):
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == 'D':  # 'D' represents dirty
                    self.grid[r][c] = 'C'  # 'C' represents clean
                    self.cleaned += 1
                    print(f"Cleaned position: ({r}, {c})")

    def get_cleaned_count(self):
        return self.cleaned

# Example usage
grid = [
    ['C', 'D', 'C'],
    ['D', 'D', 'C'],
    ['C', 'C', 'D']
]

vacuum = VacuumCleaner(grid)
vacuum.clean()
print(f"Total cleaned spots: {vacuum.get_cleaned_count()}")
