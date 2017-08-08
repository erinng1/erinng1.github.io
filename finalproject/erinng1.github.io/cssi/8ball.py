import math
import random

n = raw_input("Ask a question.")

def question(n) :
    a = ["Not likely...", "Nope", "Never in a million years.","No way!", "Of course!", "Sure.", "Yes", "Maybe"]
    if "?" in n  :
        s = random.choice(a)
        print s;
    else:
        print("That's not a question!")
    
question(n);

