# --- Day 2: Cube Conundrum ---
# You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

# The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

# As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

# For example, the record of a few games might look like this:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

class Game:
    def __init__(self, game_text):
        self.game_text = game_text
        self.id = self.get_game_id()
        self.rounds = self.get_rounds()
        self.max_colors = self.get_max_colors()
        self.power = self.get_power()

    def get_game_id(self):
        return self.game_text.split(":")[0].split(" ")[1]
    
    def get_rounds(self):
        return self.game_text.split(":")[1].split(";")

    def get_max_colors(self):
        maxs = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for r in self.rounds:
            colors = r.split(",")
            for c in colors:
                if "red" in c:
                    num = c.split("red")[0].strip()
                    if int(num) > maxs["red"]:
                        maxs["red"] = int(num)
                elif "green" in c:
                    num = c.split("green")[0].strip()
                    if int(num) > maxs["green"]:
                        maxs["green"] = int(num)
                elif "blue" in c:
                    num = c.split("blue")[0].strip()
                    if int(num) > maxs["blue"]:
                        maxs["blue"] = int(num)
                else:
                    raise ValueError  
        return maxs

    def get_power(self):
        power = 1
        for key in self.max_colors.keys():
            power *= self.max_colors[key]
        return power

           
class Tourney:
    def __init__(self, rules={}, file=""):
        self.rules = rules
        self.games_text = self.load(file)
        self.sum_fewest = 0
        self.games = self.handle_games()
        self.total = self.get_sum()
        # self.mins = self.get_mins()

    def load(self, file):
        with open(file, "r") as f:
            return f.readlines()
        
    def handle_games(self):
        games = {}  # game_id: is_valid
        fewest = {} # game_id: power
        for line in self.games_text:
            game = Game(line)
            games[game.id] = self.check_game(game)
            self.sum_fewest += game.power
        return games
    
    def check_game(self, game):
        for key in game.max_colors.keys():
            if game.max_colors[key] > self.rules[key]:
                return False   
        return True
    
    def get_sum(self):
        total = 0
        for key in self.games.keys():
            if self.games[key]:
                total += int(key)
        return total       
    

# --- Part Two ---
# The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

# As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

# Again consider the example games from earlier:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?


if __name__ == "__main__":
    # Part One (2A)
    rules = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    tourney = Tourney(rules=rules, file="2a.txt")
    print(tourney.total)

    # Part Two (2B)
    rules = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    tourney = Tourney(rules=rules, file="2a.txt")
    print(tourney.sum_fewest)





    