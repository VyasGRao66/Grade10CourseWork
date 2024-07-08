import random
import tkinter
import tkinter.messagebox


colors = ["red", "yellow", "green", "black"] # in a rook deck there are colours instead of suits
deck = [] # the deck that holds all the cards
pond = [] # the cards in the middle
player_cards = [] # the cards that the player holds
player_capture = [] # when the player captures a card it is stashed here
temp_player_capture = [] 
bot_cards = [] # the card the bot holds
bot_capture = [] # when the bot captures a card it is stashed here
player_build = False # ensureing that the if the player is building it captures that card first
build = [] # making sure the code knows what card the player will capture
player_points = 0 # the  amount of points the player has
bot_points = 0 # the amount of points the bot has
game_start = False # ensures that the certain variables will start when needed to 
card_number = 0 # the index of player_cards
index_num = 0 # index of pond
player_cards_choice = [] # what card player chose
player_card = [] # spesific card player chose
player_choice = '' # the players option
card_sum_value = 0 # sum for some cards
frame_destroyed = False # desides the destrction of frame
build_selected_card = [] # the selected player card to build
CAPTURE = 'capture'
BUILD = 'build'

class Tuxedo:
    def __init__(self): # main
        self.startup_gui = tkinter.Tk() # gui
        self.startup_gui.minsize(489, 334) # size
        self.startup_gui.title('Tuxedo') # title

        self.startup_frame = tkinter.Frame(self.startup_gui)   # frame

        self.header = tkinter.Label(self.startup_frame, text = 'Tuxedo', font= 'Ariel 30',).pack()
        
        self.start_button = tkinter.Button(self.startup_frame, text='start', command=self.start) # start fresh
        self.start_button.pack(side= 'top')
        self.startup_frame.pack()

        self.start_button = tkinter.Button(self.startup_frame, text='rules', command=self.rules) # rules
        self.start_button.pack(side= 'top')
        self.startup_frame.pack()

         # vars to label values
        self.deck_var = tkinter.StringVar() # deck value
        self.player_points_var = tkinter.StringVar() # player points
        self.bot_points_var = tkinter.StringVar() # bot points
        self.induvidual_value_var = tkinter.StringVar() # the spesific value
        
        
        tkinter.mainloop()

        
    def start(self): # the game
        global game_start, frame_destroyed, index_num, player_points, bot_points, pond
        index_num = 0
        player_capture = []
        bot_capture = []
        
        # checking if it needs to create card or already created
        self.randomization() # creating and randomizing the deck
        self.giving_cards()    
        self.pickup_cards()
            
        self.deck_var.set(pond) # setting thr var      
        self.induvidual_value_var.set(pond[0])
    
        
        if game_start == True: # making sure this happens one round after it starts
            tkinter.messagebox.showinfo('new round', 'New round')  # displaying new round
            self.points()
            
        game_start = True # making game start to true
        
        if frame_destroyed == False: # destorying the frame
            self.startup_frame.destroy()
            frame_destroyed = True
        
        
        if player_points >= 100 or bot_points >= 100: # checking if game ends till someone has 100 points
            if player_points > bot_points:
                tkinter.messagebox.showinfo('winner', 'YOU WON')
            elif player_points < bot_points:
                tkinter.messagebox.showinfo('lose', 'you lost :(')
            elif player_points == bot_points:
                tkinter.messagebox.showinfo('tie', 'congrats tie it was a good game')


        # creatinfg buttons
        self.start_button = tkinter.Button(self.startup_gui, text='Pick', command = self.player_pick).place(x = 161, y = 194, width = 166, height = 18)
        self.right = tkinter.Button(self.startup_gui, text='<', command = self.greater_than).place(x = 113, y = 150, width = 18, height = 18)
        self.left = tkinter.Button(self.startup_gui, text='>', command = self.less_than).place(x = 357, y = 150, width = 18, height = 18)
        
        self.capture_button = tkinter.Button(self.startup_gui, text='Capture',command=self.choice_capture).place(x = 408, y = 125, width = 71, height = 25)

        self.build_button = tkinter.Button(self.startup_gui, text='Build', command= self.choice_build).place(x = 408, y = 162, width = 71, height = 25)
        self.give_up_button = tkinter.Button(self.startup_gui, text='Give Up', command = self.player_giving_up_a_card).place(x = 408, y = 199, width = 71, height = 25)
        self.endturn_button = tkinter.Button(self.startup_gui, text='End Turn',command = self.ending_playerturn).place(x = 408, y = 236, width = 71, height = 25)
        self.induvidual_value = tkinter.Label(self.startup_gui, textvariable = self.induvidual_value_var, font= 'Ariel 10', bg = 'white').place(x = 149, y = 131, width = 190, height = 49)
        self.deck_value = tkinter.Label(self.startup_gui, textvariable = self.deck_var, bg = 'white', font = 'Ariel 7').place(x = 107, y = 88, width = 275, height = 24)


        colour1 = player_cards[0]
        colour2 = player_cards[1]
        colour3 = player_cards[2]
        colour4 = player_cards[3]

        self.card_one = tkinter.Button(self.startup_gui, text=player_cards[0], command=self.player_card_one, font = 'Ariel 7', fg = colour1[0], bg = '#48AAAD')
        self.card_one.place(x = 107, y = 233, width = 44, height = 85)
        self.card_two = tkinter.Button(self.startup_gui, text=player_cards[1], command=self.player_card_two, font = 'Ariel 7', fg = colour2[0], bg = '#48AAAD')
        self.card_two.place(x = 180, y = 233, width = 44, height = 85)
        self.card_three = tkinter.Button(self.startup_gui, text=player_cards[2], command=self.player_card_three, font = 'Ariel 7', fg = colour3[0], bg = '#48AAAD')
        self.card_three.place(x = 253, y = 233, width = 44, height = 85)
        self.card_four = tkinter.Button(self.startup_gui, text=player_cards[3], command=self.player_card_four, font = 'Ariel 7', fg = colour4[0], bg = '#48AAAD') 
        self.card_four.place(x = 328, y = 233, width = 44, height = 85)

        self.rules_button = tkinter.Button(self.startup_gui, text='?', command=self.rules, font = 'Ariel 7') 
        self.rules_button.place(x = 24, y = 281, width = 29, height = 28)

        self.tuxedo_header = tkinter.Label(self.startup_gui, text = 'Tuxedo', font= 'Ariel 30',).place(x = 113, y = 7, width = 262, height = 64)
        
        # creaing labels
        self.player_points_var.set('Player Points ' + str(player_points))
        self.player_point_label = tkinter.Label(self.startup_gui, textvariable = self.player_points_var, font= 'Ariel 7', bg = 'white').place(x = 8, y = 7, width = 77, height = 19)
        self.bot_points_var.set('Bot Points ' + str(bot_points))
        self.player_point_label = tkinter.Label(self.startup_gui, textvariable = self.bot_points_var, font= 'Ariel 7', bg = 'white').place(x = 8, y = 34, width = 77, height = 19)

    def rules(self): # rules
        self.rules_gui = tkinter.Tk()
        self.rules_gui.minsize(500, 500)
        self.rules_gui.title('Rules')
        self.rule_frame = tkinter.Frame(self.rules_gui)
        self.objective_label = tkinter.Label(self.rule_frame, text = 'Objective: Be the first player to earn 100 points or more.', font= 'Ariel 10', bg = 'white')
        self.objective_label.pack()
        self.match = tkinter.Label(self.rule_frame, text = 'Match the Number: A player can capture a card by matching the number with a card from their hand.', font= 'Ariel 10', bg = 'white')
        self.match.pack()
        self.sum_label = tkinter.Label(self.rule_frame, text = 'A player can capture more than one card from the center by using a card that equals the sum of two or more cards in the center.', font= 'Ariel 10', bg = 'white')
        self.sum_label.pack()
        self.combo_label = tkinter.Label(self.rule_frame, text = 'Pull off a Combo: Players should capture as many cards as possible on their turn.', font= 'Ariel 10', bg = 'white')
        self.combo_label.pack()
        self.build_rule_label = tkinter.Label(self.rule_frame, text = 'building is taking one of your cards and adding it in the middle but you are required to take it next round', font= 'Ariel 10', bg = 'white')
        self.build_rule_label.pack()
        self.give_up_rule_label = tkinter.Label(self.rule_frame, text = 'give up a card is when you are taking one of your card and keeping it the center', font= 'Ariel 10', bg = 'white')
        self.give_up_rule_label.pack()
        self.capturing = tkinter.Label(self.rule_frame, text = 'to capture a card just click capture, then click a card in your hand, then use the slide button to select which card in the midde you want to capture', font= 'Ariel 10', bg = 'white')
        self.capturing.pack()
        self.build_label = tkinter.Label(self.rule_frame, text = 'to build select the build button select which card you want to pair with the pond then select the card in the pond using the slider, then select the card in your hand that you want to capture with it next round', font= 'Ariel 10', bg = 'white')
        self.build_label.pack()
        self.give_up_label = tkinter.Label(self.rule_frame, text = 'to give up a card select the give up button then click the button in your hand', font= 'Ariel 10', bg = 'white')
        self.give_up_label.pack()
        self.end_label = tkinter.Label(self.rule_frame, text = 'after you have selected which option click end turn button.', font= 'Ariel 10', bg = 'white')
        self.end_label.pack()
        self.rule_frame.pack()

    def greater_than(self): # moving to the right of ponds values
        global index_num
        index_num -=1
        if index_num >= 0: # ensuing not out of index
            self.induvidual_value_var.set(pond[index_num])
        else:
            index_num +=1
            
    def less_than(self): # moving to the left of ponds values
        global index_num
        index_num +=1
        if len(pond)-1 >= index_num: # ensuing not out of index
            self.induvidual_value_var.set(pond[index_num])
        else:
            index_num -=1
            
    def randomization(self): 
        global deck
        
        temp_deck = [] 
        for color in colors: # creating cards
            for i in range(1, 15):
                card = [color, i]
                deck.append(card)
        
        for i in range(56): # randomizing cards
            length = len(deck)
            index = random.randint(0,length-1)
            card = deck[index]
            deck.remove(card)
            temp_deck.append(card)
        deck = temp_deck


    def pickup_cards(self): # center cards
        for i in range(4):
            card = deck[0]
            deck.remove(card)
            pond.append(card)
            
    def pond_empty(self): # checking if pond is empty
        if pond == []:
            self.pickup_cards()

    def giving_cards(self): # distributing cards
        global player_cards, game_start, card_number
        temp_value = player_cards
        player_cards = []
        for i in range(4):
            if deck != []:
                card = deck[0]
                deck.remove(card)
                player_cards.append(card)
                card = deck[0]
                deck.remove(card)
                bot_cards.append(card)
                
        if deck != [] and game_start == True and temp_value == [0,0,0,0]: # recrating buttons
            card_number = 0
            colour1 = player_cards[0]
            colour2 = player_cards[1]
            colour3 = player_cards[2]
            colour4 = player_cards[3]
            self.card_one = tkinter.Button(self.startup_gui, text=player_cards[0], command=self.player_card_one, font = 'Ariel 7', fg = colour1[0], bg = '#48AAAD')
            self.card_one.place(x = 107, y = 233, width = 44, height = 85)
            self.card_two = tkinter.Button(self.startup_gui, text=player_cards[1], command=self.player_card_two, font = 'Ariel 7', fg = colour2[0], bg = '#48AAAD')
            self.card_two.place(x = 180, y = 233, width = 44, height = 85)
            self.card_three = tkinter.Button(self.startup_gui, text=player_cards[2], command=self.player_card_three, font = 'Ariel 7', fg = colour3[0], bg = '#48AAAD')
            self.card_three.place(x = 253, y = 233, width = 44, height = 85)
            self.card_four = tkinter.Button(self.startup_gui, text=player_cards[3], command=self.player_card_four, font = 'Ariel 7', fg = colour4[0], bg = '#48AAAD') 
            self.card_four.place(x = 328, y = 233, width = 44, height = 85)

                
    def ending_playerturn(self): # each turn
        global temp_player_capture, card_number, index_num, CAPTURE, BUILD
        self.pond_empty()
        bot_choice = False
        
        if player_choice == CAPTURE: # making sure if the user enterd capture
            self.player_sweap(temp_player_capture)
            
            for i in range(len(temp_player_capture)): # removing the players card from there cards
                player_capture.append(temp_player_capture[i])
            player_capture.append(player_card)
            for i in range(len(player_cards)):
                if player_cards[i-1] == player_card:
                    player_cards[card_number-1] = 0
        temp_player_capture = []
        
        if player_choice == BUILD: # making sure if buiild
            self.player_building()
            tkinter.messagebox.showinfo('build', 'Just know you are required to capture that card next round')
        
        elif player_choice == 'give up': # making sure if the user entered give up
            card = player_card
            pond.append(card)
            player_cards[card_number-1] = 0

        
        if card_number == 1: # removing button
            self.card_one.destroy()
        elif card_number == 2:
            self.card_two.destroy()
        elif card_number == 3:
            self.card_three.destroy()
        elif card_number == 4:
            self.card_four.destroy()
       
        self.pond_empty() # checking if empty
        
        if bot_choice == False: # bots turn to figure out what he will do
            bot_choice = self.bot_capturing()
                    
        if bot_choice == False:
            bot_choice = self.bot_build()
            
        if bot_choice == False:
            self.bot_give_up()
            
        self.pond_empty() # checking if empty
        
        self.deck_var.set(pond) # updating the center
         
        if bot_cards == [] or player_cards == [0,0,0,0]: # checking if cards are empty
            self.giving_cards()
            
        if deck == []:
            self.start()
            
        index_num = 0 # reseting index
        
        self.induvidual_value_var.set(pond[index_num]) # resteing var

        
        
    #-----------------------------------------------------PLAYER----------------------------------------------------------#    
    
    def choice_capture(self): # seting that player wants to capture
        global player_choice, CAPTURE
        player_choice = CAPTURE

    def choice_build(self): # seting that player wants to build
        global player_choice, BUILD
        player_choice = BUILD
        
    def player_giving_up_a_card(self):  # seting that player wants to give up
        global player_choice
        player_choice = 'give up'

    def player_capturing(self): # player capturing values
        global index_num, player_choice, temp_player_capture, card_sum_value, build, build_selected_card
        
        temp_player_capture = [] # resting the temp deck

        if player_build == True: # checking if they built
            #player_cards_choice
            card = build[0]
            card1 = build[1]
            if card[1] + card1[1] == build_selected_card[1]: # capturing what they built
                temp_player_capture.append(card)
                temp_player_capture.append(card1)

        else:
            card = pond[index_num] # making card the same value as the iduvidual var
        
            if type(card[0]) != list: # checking if it isnt a list
                card_sum_value = card_sum_value + card[1] # adding values
            elif type(card[0]) == list: # checking if it is a list
                
                card_sum_value = card[0] + card[1] # adding values
                
            if card[1] == player_card[1] or card_sum_value == player_card[1]: # making sure if it captures a build it cap capture it properly
                if type(card[0]) == list:
                    pond.remove(card)
                    temp_player_capture.append(card[0])
                    temp_player_capture.append(card[1])
                    card_sum_value = 0

                else: # captureing normal values
                    self.player_orange(temp_player_capture)
                    pond.remove(card)
                    self.deck_var.set(pond)
                    card_sum_value = 0

            if type(card[0]) != list: # making sure they can cpture more than one thing
                temp_player_capture.append(card)

        for i in range(len(pond)): # remvoing the build or value from pond
            if pond[i-1] == build:
                pond.remove(build)
            elif pond[i-1] == card:
                pond.remove(card)    
        
    def player_building(self): # building cards
        global pond,player_build

        build.append(player_card)

        for i in range(len(player_cards)): # adding 2 cards into one list
            if player_cards[i] == player_card:
                player_cards[i] = 0
        pond[index_num] = build
        
    def player_card_one(self): # making sure it knows what is the first card
        global player_card, card_number, player_build, build_selected_card 
        
        if player_build == True:  # making it knows what to add to build 
            build_selected_card = player_cards[0]
        elif card_number != 1:
            player_card = player_cards[0]
            card_number = 1
        
    def player_card_two(self): # making sure it knows what is the second card
        global player_card, card_number, player_build, build_selected_card
        
        if player_build == True:
            build_selected_card = player_cards[1]
        elif card_number != 2:
            player_card = player_cards[1]
            card_number = 2
        
    def player_card_three(self):  # making sure it knows what is the third card
        global player_card, card_number, player_build, build_selected_card
        if player_build == True:
            build_selected_card = player_cards[2]
            
        elif card_number != 3:
            player_card = player_cards[2]
            card_number = 3
        
    def player_card_four(self): # making sure it knows what is the fourth card
        global player_card, card_number, player_build, build_selected_card

        if player_build == True:
            build_selected_card = player_cards[3]
            
        elif card_number != 4:
            player_card = player_cards[3]
            card_number = 4 
        
    def player_pick(self):
        global player_choice, build, pond, player_build, index_num, CAPTURE, BUILD
        if player_choice == CAPTURE:  # making its capture
            self.player_capturing()
        if player_choice == BUILD and player_build == False:  # making sure its build and adding values
            build = []
            card = pond[index_num]
            build.append(card)
            player_build = True
            
            
        
    #-------------------------------------------------------BOT-----------------------------------------------------------#
                
    def finding_binary(self, combo, value):  # making sure the combonations that equal the card are found
        binary = []
        difference = value
        qotent = combo/2
        while qotent >=1:
            if difference >= qotent:
                binary.append(1)
                difference = difference-qotent
            else:
                binary.append(0)
            qotent = qotent//2
                
                
                
        return binary

    def bot_capturing(self):
        global player_build
        combinations = 2**len(pond) # finding the amount of combinations
        stash = []
        temp_bot_capture = []
        for count in range(1, combinations): # ensuring you check every combination till you find one that works
            total = 0 
            num_binary = []
            num_binary = self.finding_binary(combinations, count)
            
            for y in range(len(pond)):  # checking if it is a list and knowing to capture it if needed
                value3 = pond[y]
                if type(value3[0]) == list:
                    sum = 0
                    for i in range(len(value3)):
                        value = value3[i]    
                        value2 = value[1]
                        sum = sum + value2
                    total = total + (int(num_binary[y]) * sum)
                else:
                    total = total + (int(num_binary[y]) * value3[1])  # making the combonation works 
            for i in range(len(bot_cards)):
                card  = bot_cards[i]
                
                if total == card[1]:
                    for u in range(len(pond)):
                        if num_binary[u] == 1:
                            stash.append(pond[u])  # adding the values
                            
                    for u in stash:  # making sure it knows what to remove for its cards
                        temp_bot_capture.append(u)
                        pond.remove(u)
                        self.bot_orange(temp_bot_capture)
                        
                    bot_cards.remove(card)
                    temp_bot_capture.append(card)
                    self.bot_sweap(temp_bot_capture)
                    
                    if player_build == True:
                        for y in range(len(temp_bot_capture)):
                            if temp_bot_capture[y] == build:
                                player_build = False
                                
                    for u in range(len(temp_bot_capture)):
                        bot_capture.append(temp_bot_capture[u])        
                    return True
        return False

    def bot_build(self):  # building values
        for i in range(len(bot_cards)): # Making sure it cycles through every card in bots hand
            card = bot_cards[i] 
            for count in range(len(bot_cards)):  # making sure it knows what is good to capture
                card1 = bot_cards[count]
                for u in range(len(pond)):
                    card2 = pond[u]
                    card3 = card2[0]
                    if type(card3) == list: # making sure it cant build on builds
                        print('')
                    elif card1[1] + card2[1] == card[1]:
                        build = []
                        bot_cards.remove(card1)
                        build.append(card1)
                        build.append(card2)
                        pond[u] = build
                        return True
        return False

    def bot_give_up(self):  # giveing up a card to pond
        global bot_cards, pond
        card = bot_cards[0]
        bot_cards.remove(card)
        pond.append(card)
        return True


    #-------------------------------------------------------POINTS--------------------------------------------------------#


    def points(self): 
        global bot_capture, player_capture, bot_points, player_points  # calculating the points
        
        if len(player_capture) > len(bot_capture):  # finding who has the most
            player_points += 15
        elif len(bot_capture) > len(player_capture):
            bot_points += 15
        elif len(player_capture) == len(bot_capture):
            player_points += 5
            bot_points += 5

        for i in range(len(player_capture)):  # making sure it knows who has captured a 5
            card = player_capture[i]
            if card[1] == 5:
                player_points += 5

        for i in range(len(bot_capture)):
            card = bot_capture[i]
            if card[1] == 5:
                bot_points += 5
                
    def player_sweap(self, stash):  # making sure it knows when the pond has been cleared and whether its a big or little sweep
        global player_points
        if len(stash)-1 <= 3 and pond == []:
            player_points += 5
        elif len(stash)-1 >= 4 and pond == []:
            player_points += 10

    def bot_sweap(self, stash): # making sure it knows when the pond has been cleared and whether its a big or little sweep
        global bot_points
        if len(stash)-1 <= 3 and pond == []:
            bot_points += 5
        elif len(stash)-1 >= 4 and pond == []:
            bot_points += 10
        

    def player_orange(self, stash): # making sure it knows if they captured a red or a orange 
        global player_capture
        count = 0
        if len(stash) > 1:
            for i in range(len(stash)):
                for u in range(len(stash)):
                    card = stash[i]
                    card1 = stash[u]
                    if card[0] == 'red' and card1[0] == 'yellow' and card != card1 and count == 0:
                        player_points += 10
                        count += 1

    def bot_orange(self, stash): # making sure it knows if they captured a red or a orange
        global bot_points
        count = 0
        if len(stash) > 1:
            for i in range(len(stash)):
                for u in range(len(stash)):
                    card = stash[i]
                    card1 = stash[u]
                    if type(card[0]) != list and type(card1[0]) != list:
                        if card[0] == 'red' and card1[0] == 'yellow' and card != card1 and count == 0:
                            bot_points += 10
                            count += 1
                
tuxedo = Tuxedo()
