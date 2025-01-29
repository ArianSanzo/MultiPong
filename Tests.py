import json
with open('data//config.json', 'r') as f:
    config = json.load(f)

keys_groups = []
for keys in config['player_movement_configs']:
    keys_groups.append((keys[0]['key_code'], keys[1]['key_code']))

players_and_keys = [[player, movement_key] for player, movement_key in zip([1, 2], keys_groups)]

print(players_and_keys)
