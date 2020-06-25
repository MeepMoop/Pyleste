# exiting the level restarts the level
def enable_loop_mode(p8):
  g = p8.game
  g.next_room = lambda: g.load_room(g.level_index() % 8, g.level_index() // 8)

# load a room by level id
def load_room(p8, level_id):
  g = p8.game
  g.load_room(level_id % 8, level_id // 8)

# remove all instances of an object from the current loaded room
def suppress_object(p8, object_type):
  g = p8.game
  g.objects = [obj for obj in g.objects if type(obj) != object_type]

# replace a room with a 128-character room string (ignores white space and line breaks)
def replace_room(p8, level_id, room_data):
  room_data = room_data.replace('\n', '').replace(' ', '')
  tiles = {
    'w': 32, # terrain
    '^': 17, # up spike
    'v': 27, # down spike
    '<': 59, # leftspike
    '>': 43, # right spike
    'p': 1,  # player spawn
    '.': 0   # empty
  }
  rx, ry = level_id % 8, level_id // 8
  for tx in range(16):
    for ty in range(16):
      tile = room_data[tx + 16 * ty]
      p8.mset(rx * 16 + tx, ry * 16 + ty, tiles[tile] if tile in tiles else 0)

# forces an already spawned maddy to be in a specific state
def place_maddy(p8, x, y, remx=0.0, remy=0.0, spdx=0.0, spdy=0.0, grace=6, djump=1):
  g = p8.game
  p = g.get_player()
  if p != None:
    g.destroy_object(p)
  p = g.init_object(g.player, x, y)
  p.rem.x, p.rem.y = remx, remy
  p.spd.x, p.spd.y = spdx, spdy
  p.grace, p.djump = grace, djump

# render the game from the current game state onward given a list of inputs
def watch_inputs(p8, inputs):
  import time
  print(p8.input_display)
  print(p8.game)
  for a in inputs:
    time.sleep(1 / 30)
    p8.set_btn_state(a)
    p8.step()
    print(p8.input_display)
    print(p8.game)