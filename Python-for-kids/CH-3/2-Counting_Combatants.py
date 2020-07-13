print('''If there are 3 buildings with 25 ninjas hiding on each roof and 2 tunnels 
with 40 samurai hiding inside each tunnel, how many ninjas and samurai 
are about to do battle?''')

roof = 3
ninjas = 25
tunnel = 2
samurai = 40

result = (roof * ninjas) + (tunnel * samurai)

print("\nThe answer is (%s x %s) + (%s x %s) = %s" %
      (roof, ninjas, tunnel, samurai, result))
