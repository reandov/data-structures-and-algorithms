# Hashmap init
players = {
    "john": ["minecraft", "terraria", "stardew valley"],
    "susan": ["league of legends", "valorant"],
    "rob": ["counter strike"]
}

# Looping through it's keys
for player in players.keys():
    print(player)

# Looping through it's values
for game in players.values():
    print(game)

# Looping through it's items (tuples)
for player, game in players.items():
    print(player, "likes", game)