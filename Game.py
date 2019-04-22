from Tree2 import Tree2


class Game:
    def __init__(self):
        self.number_of_sticks = None
        self.is_play_first = None
        self.tree = None
        self.current_player = None
        self.play()

    def play(self):
        self.menu()
        current_node = self.tree.tree[0]
        while not current_node.is_leaf:
            print('\n=======================================')
            if self.available_moving_point(current_node) == False:
                print('There is no available moving point')
                break
            else:
                if self.current_player:
                    current_node = self.get_human_moving_choice(current_node)
                else:
                    current_node = self.get_comp_moving_choice(current_node)
            self.current_player = not self.current_player
            print('=======================================')
        print('=======================================')
        self.current_player = not self.current_player
        print("\n" + ("\tY o u  " if self.current_player else "C o m p u t e r  ") + " w i n !")
        self.current_player = not self.current_player
        print(("   Y o u  " if self.current_player else "   C o m p u t e r  ") + " l o s e !\n")

    def available_moving_point(self, current_node):
        print(("(^_^)/ Your" if self.current_player else "['-']/ Computer") + " Turn\nAvailable moving point:")
        count_child = 0
        count_number = 0
        for i in current_node.children:
            count_one_two = 0
            node_string = ("-".join(map(str, i.node_value)))
            node_split = node_string.split("-")
            node_length = len(node_split)
            for j in range(node_length):
                if node_split[j] == "1" or node_split[j] == "2":
                    count_one_two += 1
                j += 1
            if count_one_two != len(node_split):
                print(str(count_number + 1) + ". [" + node_string +"]")
                count_number += 1
            count_child += 1
        if count_number == 0:
            return False
        else:
            return True

    def get_comp_moving_choice(self, current_node):
        choice_child = self.check_comp_moving_choice(current_node)
        current_child = 0
        for i in current_node.children:
            if current_child == choice_child:
                print("Computer move\t\t: [" + ("-".join(map(str, i.node_value)))+"]")
                return i
            current_child += 1
        for i in current_node.children:
            print("Computer move\t\t: [" + ("-".join(map(str, i.node_value)))+"]")
            return i

    def check_comp_moving_choice(self, current_node):
        child_choice = 0
        for i in current_node.children:
            if i.evaluator_value == 1:
                return child_choice
            child_choice += 1
        return child_choice / child_choice - 1

    def get_human_moving_choice(self, current_node):
        count_child = 0
        while True:
            moving_choice = int(input("Choose your move\t: "))
            for i in current_node.children:
                if moving_choice - 1 == count_child:
                    print("Your move\t\t: [" + ("-".join(map(str, i.node_value)))+"]")
                    return i
                count_child += 1
            print("Invalid move\n\n")

    def menu(self):
        print('\n=======================================')
        self.number_of_sticks = int(input("Insert number of sticks\t: "))
        print('=======================================')
        self.is_play_first = int(input("Select Turn\n1. You play first\n2. Computer play first\n"
                                       "Choose your turn\t: "))
        print('=======================================')
        print('\n=======================================')
        self.is_play_first = True if self.is_play_first == 1 else False
        print("\nCreating tree....")
        self.tree = Tree2(self.number_of_sticks, self.is_play_first)
        print("Tree created.\n")
        is_show_tree = input("View rendered tree [y/n]? ")
        if is_show_tree == "y" or is_show_tree == "Y":
            print(self.tree.get_tree())
            print("\n")
        self.current_player = self.tree.first_player
        print('\n=======================================')
        
print('\t ____________________')
print('\t|                    |')
print('\t|      NIM GAME      |')
print('\t| develop by python3 |')
print('\t|                    |')
print('\t ____________________')
Game()
