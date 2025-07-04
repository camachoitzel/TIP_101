# Pokemon Class
# Add a line of code (outside of the class) to instantiate an instance of the class Pokemon and store it in a variable named my_pokemon. 
# The Pokemon instance created should have name "Pikachu" and its types should be ["Electric"].

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

# my_pokemon = Pokemon("Pikachu" , "Electric")


# Create Squirtle
# Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. 
# The Pokemon instance created should have name "Squirtle" and its types should be ["Water"].

# Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.


# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })

# squirtle = Pokemon("Squirtle", "Water")

# print(squirtle.print_pokemon())


# Is Caught
# Using your code from Problem 2, update your squirtle Pokemon so that is_caught is updated to True. 
# Use the print_pokemon() function to verify that squirtle's is_caught property was updated.

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })


# squirtle = Pokemon("Squirtle", "Water")
# squirtle.is_caught = True
# print(squirtle.print_pokemon())


# Catch Pokemon
# Update the Pokemon class with a new method catch() that takes in no parameters except self.

# The method should update the Pokemon's is_caught attribute to True and not return any value.

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })

#     def catch(self):
#         self.is_caught = True

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()


# Choose Pokemon
# Update the Pokemon class with a new method choose() that takes in no parameters except self.

# If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".

# Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!".


# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })

#     def catch(self):
#         self.is_caught = True

#     def choose(self):
#         if self.is_caught:
#             print(self.name + " I choose you!")
#         else:
#             print(self.name + " is wild! Catch them if you can!")

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()

# Add pokemon Type
# Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

# It should add new_type to the Pokemon's list of types.

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })

#     def catch(self):
#         self.is_caught = True

#     def choose(self):
#         if self.is_caught:
#             print(self.name + " I choose you!")
#         else:
#             print(self.name + " is wild! Catch them if you can!")

#     def add_type(self, new_type):
#         self.types.append(new_type)

# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()


# Get pokemon
# Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.

# The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })

#     def catch(self):
#         self.is_caught = True

#     def choose(self):
#         if self.is_caught:
#             print(self.name + " I choose you!")
#         else:
#             print(self.name + " is wild! Catch them if you can!")

#     def add_type(self, new_type):
#         self.types.append(new_type)
    


# def get_by_type(my_pokemon, pokemon_type):
#     result = []
#     for pokemon in my_pokemon:

#         if pokemon_type in pokemon.types:
#             result.append(pokemon.name)
    
#     return result


# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)

# Pokemon Evolution

# Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, each instance of Pokemon has an attribute evolution. 
# The attribute will either be the default value of None or another Pokemon instance.

# Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.

# The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.

class Pokemon:
    def  __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught:
            print(self.name + " I choose you!")
        else:
            print(self.name + " is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)

    def get_evolutionary_line(starter_pokemon):
	    evolution_list = []

        current = starter_pokemon
    
    
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)