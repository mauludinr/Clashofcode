# Goal
# You are given a string w, and a single character c.
# c is equal to either S or D.

# You need to print the word w as many times as the length of w. You print w once and then print w reversed, you print w once and then print w reversed and so on...

# if c equal to S you need to have spaces between each word.

# if c equal to D you need to have line breaks between each word.

# Input
# A word w.
# A character c equal to S or D.

# Output
# The word w, alternatively reversed.
# w must be outputted on different lines if c is D, or on the same line (with line breaks) if c is S.

# Constraints
# c = D or S

# Example
# Input
# Hello
# S
# Output
# Hello olleH Hello olleH Hello

w=input()
c=input()
for i in range(len(w)):
    if c=="D":
        if i%2!=0:print(w[::-1])
        else:print(w)
    else:
        if i%2!=0:print(w[::-1],end=" ")
        elif(i%2==0):
            if (i==len(w)-1):print(w,end="")
            else:print(w,end=" ")

# Test Cases      
# 1) Input: 
# Hello
# S
# Output :
# Hello olleH Hello olleH Hello

# 2) Input: 
# CodinGame
# D
# Output :
# CodinGame
# emaGnidoC
# CodinGame
# emaGnidoC
# CodinGame
# emaGnidoC
# CodinGame

# 3) Input: 
# ClashOfCode
# S
# Output :
# ClashOfCode odeCfOhsalC ClashOfCode odeCfOhsalC ClashOfCode odeCfOhsalC ClashOfCode odeCfOhsalC ClashOfCode odeCfOhsalC ClashOfCode

# 4) Input: 
# ChampionCoder
# D
# Output :
# ChampionCoder
# redoCnoipmah
# ChampionCoder
# redoCnoipmahC
# ChampionCoder
# redoCnoipmah
# ChampionCoder
# redoCnoipmahC
# ChampionCoder
# redoCnoipmah
# ChampionCoder
# redoCnoipmahC
# ChampionCoder
# redoCnoipmah
# ChampionCoder
