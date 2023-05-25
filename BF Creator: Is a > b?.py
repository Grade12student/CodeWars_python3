tokens = ['za', '[-', 'ac', '+', 'cb', '[-', 'bc', '-', 'cb', '[-', 'bd', '+', 'db', ']]', 'bd', '[-',
          'db', '+', 'bd', ']', 'dc', '[-', 'cd', '+', 'da', '[-]', 'ac', ']', 'ca', ']', 'ad', '.']

def create(a, b, c, d, z=0):
    v = locals()
    move = lambda s, d: '<>'[v[d]>v[s]] * abs(v[d]-v[s])
    return ''.join((move(*token) if token.isalpha() else token) for token in tokens)
#The create function takes the input variables a, b, c, d, and an additional parameter z (which is set to 0 by default). 
# It uses the locals() function to access the values of the input variables. 
# The move lambda function determines the direction and number of steps needed to move the pointer 
# based on the values of the source and destination memory cells.
# The function then iterates over the tokens and performs the necessary replacements. 
# If the token is alphabetic, it calls the move function with the appropriate memory cells. 
# Otherwise, it leaves the token unchanged. 
# Finally, it joins the tokens together to form the resulting BrainF**k program