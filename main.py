"""
In a single-player jump game, the player starts at one end of a series of squares, with the goal of reaching the last square.

At each turn, the player can take up to s
s
 steps towards the last square, where s
s
 is the value of the current square.

For example, if the value of the current square is 3
3
, the player can take either 3
3
 steps, or 2
2
 steps, or 1
1
 step in the direction of the last square. The player cannot move in the opposite direction, that is, away from the last square.

You have been tasked with writing a function to validate whether a player can win a given game or not.

You’ve been provided with the nums integer array, representing the series of squares. The player starts at the first index and, following the rules of the game, tries to reach the last index.

If the player can reach the last index, your function returns TRUE; otherwise, it returns FALSE.
"""

"""
[1,1,2,1,5,0]
"""

def jump_game(nums):
  N = len(nums)
  end = N-1
  for i in range(N-1, -1, -1):
    # check to see if you can reach target from ith index 
    dist_to_target = end - i
    num_steps = nums[i]
    if num_steps >= dist_to_target:
      # this means target is reachable from ith position
      # => re-assign target to ith position, only need a valid path to here
      if i == 0: # STARTING POSITION
        return True # if you can reach end/target from start
      end = i
  return False 


