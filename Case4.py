# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 1) Test 1
# Input
# Hello there!!
# Expected output
# there!! Hello

# 2) Test 2
# Input
# We had a three-course meal.
# Expected output
# meal. three-course a had We

# 3) Test 3
# Input
# Oh, how I'd love to go!
# Expected output
# go! to love I'd how Oh,

# 4) Test 4
# Input
# Reaching the large house near the Horse Guards' barracks, in which Anatole lived, Pierre entered the lighted porch, ascended the stairs, and went in at the open door.
# Expected output
# door. open the at in went and stairs, the ascended porch, lighted the entered Pierre lived, Anatole which in barracks, Guards' Horse the near house large the Reaching

s = input()
z = s.split(sep=" ")
for i in range(len(z)-1,-1, -1):
    if i==0:
        print(z[i],end="")
    else:
        print(z[i],end=" ")
