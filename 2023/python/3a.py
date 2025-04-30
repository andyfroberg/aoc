# --- Day 3: Gear Ratios ---
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

class Schematic:
    def __init__(self, file="") -> None:
        self.txt = self.load_file(file)
        self.txt_padded = self.pad_txt()
        self.nums = []
        self.symbols = ["!", "@", "#", "$", "%", "^", "&", "(", ")", "-", "=", "/"]

    def load_file(self, file):
        with open(file, "r") as f:
            return f.readlines()
        
    def pad_txt(self):
        top = "." * len(self.txt[0])
        top += "\n"
        bottom = str(top)
        for i, line in enumerate(self.txt):
            self.txt[i] = "." + line[:-2] + ".\n"  # correct for newline chars
        self.txt.insert(0, top)
        self.txt.append(bottom)

    
    def check_neighbors(self):
        current_num = False
        for i, line in list(enumerate(self.txt_padded))[1:]:
            for j, char in list(enumerate(line))[1:]:
                if self.northwest(i, j) or self.north(i, j) or self.northeast(i, j) \
                        or self.west(i, j) or self.east(i, j) \
                        or self.southwest(i, j) or self.south(i, j) or self.southeast(i, j):
                    self.get_current_num(i, j)
                    self.get_next_candidate(i, j)

    def get_current_num(self, i, j):
        pass

    
    def get_next_candidate(self, i, j):
        pass
    
    def northwest(self, i, j):
        for s in self.symbols:
            if self.txt_padded[i-1][j-1] == "s":
                return True
        return False
            
    def north(self, i, j):
        for s in self.symbols:
            if self.txt_padded[i-1][j] == "s":
                return True
        return False
            
    def northeast(self, i, j):
        for s in self.symbols:
            if self.txt_padded[i-1][j+1] == "s":
                return True
        return False
            
    def west(self, i, j):
        for s in self.symbols:
            if self.txt_padded[i][j-1] == "s":
                return True
        return False
    
    def east(self, i, j):
        for s in self.symbols:
            if self.txt_padded[i][j+1] == "s":
                return True
        return False
    
    def southwest(self, i, j):
        for s in self.symbols:
            if self.txt_padded[i+1][j-1] == "s":
                return True
        return False
            
    def south(self, i, j):
        for s in self.symbols:
            if self.txt_padded[i+1][j] == "s":
                return True
        return False
            
    def southeast(self, i, j):
        for s in self.symbols:
            if self.txt_padded[i+1][j+1] == "s":
                return True
        return False
        




if __name__ == "__main__":
    s = Schematic("3a_test.txt")
    print(s.txt)