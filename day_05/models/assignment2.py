# import random
# class Player:
#     def __init__(self, player_name):
#         self.player_name = player_name
#         self.curr_pos = 0
#         self.no_rolls = 0

#     def move(self, steps):
#         self.curr_pos += steps

#     def reset_position(self):
#         self.curr_pos = 0
    
#     def display_position(self):
#         print(f"{self.player_name} - {self.curr_pos}")

# class Dice:
#     def __init__(self, sides):
#         self.sides = sides

#     def roll(self):
#         return random.randint(1, self.sides)

# class Board:
#     def __init__(self, size):
#         self.size = size

#     def is_valid_position(self, position):
#         self.position<= self.size

# class Game:
#     def __init__(self, player, dice, board):
#         self.player = player
#         self.dice = dice
#         self.board = board

#         board= Board(30)
#         dice =  Dice(6)
#         alice= Player("Alice")
#         bob= Player("bob")
#         charlie= Player("charlie")




import random


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.curr_pos = 0
        self.no_rolls = 0

    def move(self, steps):
        self.curr_pos += steps

    def reset_position(self):
        self.curr_pos = 0

    def display_position(self):
        print(f"{self.player_name} position: {self.curr_pos}")


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Board:
    def __init__(self, size):
        self.size = size

    def is_valid_position(self, position):
        return position <= self.size


class Game:
    def __init__(self, board, dice, players):
        self.board = board
        self.dice = dice
        self.players = players
        self.winner = None

    def check_collision(self, current_player):
        for player in self.players:
            if (
                player != current_player
                and player.curr_pos == current_player.curr_pos
                and player.curr_pos != 0
            ):
                print("\nCollision!")
                print(
                    f"{player.player_name} was already at position {player.curr_pos}"
                )
                player.reset_position()
                print(f"{player.player_name} goes back to Start")

    def check_winner(self, player):
        if player.curr_pos == self.board.size:
            self.winner = player
            return True
        return False

    def play_turn(self, player):
        roll_value = self.dice.roll()
        player.no_rolls += 1

        print(f"\n{player.player_name} rolled {roll_value}")

        new_position = player.curr_pos + roll_value

        if self.board.is_valid_position(new_position):
            player.move(roll_value)
            print(f"{player.player_name} moved to {player.curr_pos}")

            self.check_collision(player)

            if self.check_winner(player):
                print(f"\n{player.player_name} wins the game!")
                return True

        else:
            print(
                f"Move ignored! {player.player_name} cannot move beyond {self.board.size}"
            )

        return False

    def display_rankings(self):
        print("\nCurrent Positions:")
        rankings = sorted(
            self.players,
            key=lambda player: player.curr_pos,
            reverse=True
        )

        for player in rankings:
            print(f"{player.player_name}: {player.curr_pos}")

    def start_game(self):
        print("===== Board Race Game =====")

        while not self.winner:
            for player in self.players:
                if self.play_turn(player):
                    return

            self.display_rankings()

board = Board(30)
dice = Dice(6)

player1 = Player("Alice")
player2 = Player("Bob")
player3 = Player("Charlie")

players = [player1, player2, player3]

game = Game(board, dice, players)

game.start_game()


for player in players:
    print(f"{player.player_name}: {player.no_rolls} dice rolls")