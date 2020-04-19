# Brandon McRae int project
# this should pick a character for you in the game i play called smite
import random


def main():
    print("Hello! If you can't pick a character in smite, I am here to help!")
    getting_started = input("First off are you solo or in a group? ")
    if getting_started == 'solo':
        baseline()
    elif getting_started == 'group' and 'Group':
        group = input("Do you want a random 5 man team(1) or a game mode(2)? ")
        if group == '1':
            random_team()
        elif group == '2':
            gamemode()
        else:
            print("Invalid choice try again.")
            main()
    else:
        print("Invalid choice, try again")
        main()


# baseline is just the base line questions to calculate a character
def baseline():
    print(
        "So now I'm going to help you pick a character in smite(1), give you a random character(2),"
        " or I can even give you a game mode to play(3).")
    first_question = input("So option 1, 2, or 3: ")
    if first_question == '1':
        print("Right let's get started!")
        answer1 = input("Damage or tank? ")

        if answer1 == 'damage' and 'Damage':
            print("Damage, Nice Choice.")
            roles_damage()

        elif answer1 == 'tank' and 'Tank':
            print("Tank, Nice Choice.")
            role_tank()
        else:
            print("Invalid choice, try again")
            baseline()
    elif first_question == '2':
        print("Brave one you are... let's get started.")
        random_char()

    elif first_question == '3':
        print("Seems you don't know what to play... I'll help.")
        gamemode()
    else:
        print("Invalid choice, try again")
        baseline()


# this is for the damage characters to pick from
def roles_damage():
    import random
    answer2 = input("Now are you Melee or Ranged?: ")

    if answer2 == 'melee':
        print("So close to getting your character!")
        answer1234 = input("Assassin is the only melee damage is that ok? (y) or (n)")
        if answer1234 == 'n' and 'N':
            roles_damage()

        elif answer1234 == 'y' and 'Y':
            random1 = ('Thor', 'Pele', 'Fenrir', 'Arachne', 'Awilix', 'Bakasura', 'Bastet', 'Camazotz', 'Da Ji'
                       , 'Hun Batz', 'Kali', 'Loki', 'Mercury', 'Ne Zha', 'Nemesis', 'Ratatoskr', 'Ravana'
                       , 'Serqet', 'Set', 'Susano', 'Thanatos')
            print("Your character is:", random.choice(random1))
            print("Thank you for using me!")

        else:
            print("Invalid choice try again.")
            roles_damage()

    elif answer2 == 'ranged' and 'Ranged':
        print("So close to getting your character!")
        answer4 = input("Hunter or Mage: ")

        if answer4 == 'Hunter' and 'hunter':
            random4 = (
                'Ah Muzen Cab', 'Anhur', 'Apollo', 'Artemis', 'Cernunnos', 'Chernobog', 'Chiron', 'Cupid', 'Hachiman',
                'Heimdallr',
                'Hou Yi', 'Izanami', 'Jing Wei', 'Medusa', 'Neith'
                , 'Rama', 'Skadi', 'Ullr', 'Xbalanque')
            print("Your character is:", random.choice(random4))
            print("Thank you for using me!")

        elif answer4 == 'mage' and 'Mage':
            random5 = (
                'Agni', 'Ah Puch', 'Anubis', 'Aphrodite', 'Baron Samedi', 'Change', 'Chronos', 'Discordia', 'Freya',
                'Hades',
                'He Bo', 'Hel', 'Hera', 'Isis', 'Janus', 'Kukulkan', 'Merlin', 'Nox', 'Nu Wa', 'Olorun', 'Persephone',
                'Poseidon',
                'Ra', 'Raijin', 'Scylla', 'Sol', 'The Morrigan',
                'Thoth', 'Vulcan', 'Zeus', 'Zhong Kui')
            print("Your character is:", random.choice(random5))
            print("Thank you for using me!")
        else:
            print("Invalid choice try again.")
            roles_damage()
    else:
        print("Invalid choice try again.")
        roles_damage()


# this is just a completely random choice
def random_char():
    print("Getting your random character now!")
    random_pick = 'Thor', 'Pele', 'Fenrir', 'Arachne', 'Awilix', 'Bakasura', 'Bastet', 'Camazotz', 'Da Ji', 'Hun Batz' \
        , 'Kali', 'Loki', 'Mercury', 'Ne Zha' 'Nemesis', 'Ratatoskr', 'Ravana', 'Serqet', 'Set', 'Susano', 'Thanatos' \
        , 'Oden', 'Achilles', 'Amaterasu', 'Bellona', 'Ares', 'Artio', 'Athena', 'Bacchus', 'Ah Muzen Cab', 'Anhur' \
        , 'Apollo', 'Artemis', 'Cernunnos', 'Chernobog', 'Chiron', 'Cupid', 'Hachiman', 'Heimdallr', 'Hou Yi' \
        , 'Izanami', 'Jing Wei', 'Medusa', 'Neith''Rama', 'Skadi', 'Ullr', 'Xbalanque', 'Agni', 'Ah Puch', 'Anubis' \
        , 'Aphrodite', 'Baron Samedi', 'Change', 'Chronos''Discordia', 'Freya', 'Hades', 'He Bo', 'Hel', 'Hera' \
        , 'Isis', 'Janus', 'Kukulkan', 'Merlin', 'Nox', 'Nu Wa', 'Olorun', 'Persephone', 'Poseidon', 'Ra', 'Raijin' \
        , 'Scylla', 'Sol', 'The Morrigan', 'Thoth', 'Vulcan', 'Zeus', 'Zhong Kui''Cabrakan', 'Cerberus', 'Fafnir' \
        , 'Ganesha', 'Geb', 'Jormungandr', 'Khepri', 'Kumbhakarna', 'Kuzenbo', 'Sobek', 'Sylvanus', 'Terra' \
        , 'Xing Tian', 'Yemoja', 'Ymir'
    import random
    print("Your character is: ", random.choice(random_pick))
    print("Thank you for using me!")


# this picks a random game mode based off the questions it asks
def gamemode():
    import random
    random_gm = ('Arena', 'Assault', 'Siege')
    random_tryhard = ('Conquest', 'Joust', 'Clash')
    gamemode_answer = input("Do you want a casual game or a try-hard game mode? ")
    if gamemode_answer == 'casual' and 'Casual':
        print("Your game mode is: ", random.choice(random_gm))

    elif gamemode_answer == 'try-hard' and 'Tryhard' and 'tryhard' and 'Try-hard':
        print("Your game mode is: ", random.choice(random_tryhard))
        print("Thank you for using me!")
    else:
        print("Invalid choice, try again")
        gamemode()


# this spits out a random 5 man team
def random_team():
    import random
    print("I'm calcuating your team now!")
    random_mage = 'Agni', 'Ah Puch', 'Anubis', 'Aphrodite', 'Baron Samedi', 'Change', 'Chronos', 'Discordia', 'Freya', \
                  'Hades', 'He Bo', 'Hel', 'Hera', 'Isis', 'Janus', 'Kukulkan', 'Merlin', 'Nox', 'Nu Wa', 'Olorun' \
        , 'Persephone', 'Poseidon', 'Ra', 'Raijin', 'Scylla', 'Sol', 'The Morrigan', 'Thoth', 'Vulcan', 'Zeus' \
        , 'Zhong Kui '
    random_hunter = 'Ah Muzen Cab', 'Anhur', 'Apollo', 'Artemis', 'Cernunnos', 'Chernobog', 'Chiron', 'Cupid' \
        , 'Hachiman', 'Heimdallr', 'Hou Yi', 'Izanami', 'Jing Wei', 'Medusa', 'Neith', 'Rama', 'Skadi', 'Ullr' \
        , 'Xbalanque'
    random_assassin = 'Thor', 'Pele', 'Fenrir', 'Arachne', 'Awilix', 'Bakasura', 'Bastet', 'Camazotz', 'Da Ji' \
        , 'Hun Batz', 'Kali', 'Loki', 'Mercury', 'Ne Zha' 'Nemesis', 'Ratatoskr', 'Ravana', 'Serqet', 'Set', 'Susano',
    'Thanatos'
    random_warrior = 'Oden', 'Achilles', 'Amaterasu', 'Bellona', 'Chaac', 'Cu Chulainn', 'Erlang Shen', 'Guan Yu' \
        , 'Hercules', 'Horus', 'King Arthur', 'Mulan', 'Nike', 'Odin', 'Osiris', 'Sun Wukong', 'Tyr' \
        , 'Vamana'
    random_guardian = 'Ares', 'Artio', 'Athena', 'Bacchus', 'Cabrakan', 'Cerberus', 'Fafnir', 'Ganesha', 'Geb', \
                      'Jormungandr', 'Khepri', 'Kumbhakarna', 'Kuzenbo', 'Sobek', 'Sylvanus', 'Terra', 'Xing Tian' \
        , 'Yemoja', 'Ymir'
    print("Your full team is... ", random.choice(random_mage), ',', random.choice(random_hunter), ',',
          random.choice(random_assassin), ',', random.choice(random_warrior), ',', random.choice(random_guardian))
    print("Thank you for using me!")


# this is to calculate a random tank
def role_tank():
    tanks = input("Tanks are only melee is this alright?(y)or(n)")
    if tanks == 'y' and 'Y':
        tank_choice = input("Do you want warrior(1) or guardian(2)")
        if tank_choice == '1':
            random2 = ('Oden', 'Achilles', 'Amaterasu', 'Bellona', 'Chaac', 'Cu Chulainn', 'Erlang Shen', 'Guan Yu'
                       , 'Hercules', 'Horus', 'King Arthur', 'Mulan', 'Nike', 'Odin', 'Osiris', 'Sun Wukong', 'Tyr',
                       'Vamana')
            print("Your character is:", random.choice(random2))
            print("Thank you for using me!")
        elif tank_choice == '2':
            random3 = ('Ares', 'Artio', 'Athena', 'Bacchus', 'Cabrakan', 'Cerberus', 'Fafnir', 'Ganesha', 'Geb',
                       'Jormungandr', 'Khepri', 'Kumbhakarna', 'Kuzenbo', 'Sobek', 'Sylvanus', 'Terra', 'Xing Tian'
                       , 'Yemoja', 'Ymir')
            print("Your character is:", random.choice(random3))
            print("Thank you for using me!")
        else:
            print("Invalid choice, try again")
            role_tank()
    elif tanks == 'n' and 'N':
        role_tank()

    else:
        print("Invalid choice, try again")
        role_tank()


# if the person wanted to to could change their character
def ending():
    end = input("If you like your character press (1) if not press (2)")
    if end == '1':
        main()
    elif end == '2':
        start_over = input("Do you want to start over?(y) or (n)")
        if start_over == 'y':
            baseline()
        elif start_over == 'n':
            print("Thank you for using me!")
        else:
            print("Invalid choice, try again")
            ending()
    else:
        print("Invalid choice, try again")
        ending()


main()
