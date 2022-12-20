# metagamebalance
Measures metagame balance using game theory and the assumption that different players have unique skillsets that affect how they'll perform with individual strategies. 

Using a matrix, such as a matchup chart, that describes how different options in a game fare against each other, and an estimate of how much these matchups will vary from player to player, this estimates how much usage each option should have in competitive play.

For instance, I've included a matchup chart from Super Smash Bros. 64 you can use to estimate how much usage each character in that game should have in competitive play.

For a conceptual explanation, see: 

https://quantimschmitz.com/2022/12/07/a-better-way-to-measure-game-balance-using-game-theory/


See also:

Alex Jaffe's approach, which offers a similar way to measure metagame balance, but without noise and with the option to manually constrain the usage of particular options.

https://github.com/Blinkity/metagame

His talk explaining this approach: https://www.youtube.com/watch?v=miu3ldl-nY4

Siddarth Nahar's Nash Equilibrium finding code, which I repurposed: 

https://github.com/sid230798/Game_Theory/blob/master/Problem3/analyse_equilibrium.py
