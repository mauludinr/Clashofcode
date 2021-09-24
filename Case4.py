# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input
# Expected output
# Hello there!!
# there!! Hello
# 02 Test 2
# Input
# Expected output
# We had a three-course meal.
# meal. three-course a had We
# 03 Test 3
# Input
# Expected output
# Oh, how I'd love to go!
# go! to love I'd how Oh,
# 04 Test 4
# Input
# Expected output
# Reaching the large house near the Horse Guards' barracks, in which Anatole lived, Pierre entered the lighted porch, ascended the stairs, and went in at the open door.
# door. open the at in went and stairs,

s = input()
z = s.split(sep=" ")
for i in range(len(z)-1,-1, -1):
    if i==0:
        print(z[i],end="")
    else:
        print(z[i],end=" ")
