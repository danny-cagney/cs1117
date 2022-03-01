text = """Now, this is a story all about how 
My life got flipped-turned upside down
And I'd like to take a minute
To sit right there
I'll tell you how I became the prince of a town called Bel Air
In west Philadelphia born and raised
On the playground was where I spent most of my days
Chillin' out maxin' relaxin' all cool
And all shootin some b-ball outside of the school
When a couple of guys who were up to no good
Started making trouble in my neighborhood
I got in one little fight and my mom got scared
She said 'You're movin' with your auntie and uncle in Bel Air'
I begged and pleaded with her day after day
But she packed my suit case and sent me on my way
She gave me a kiss and then she gave me my ticket.
I put my Walkman on and said, 'I might as well kick it'.
First class, yo this is bad
Drinking orange juice out of a champagne glass.
Is this what the people of Bel-Air living like?
Hmmmmm this might be alright.
But wait I hear they're prissy, bourgeois, all that
Is this the type of place that they just send this cool cat?
I don't think so
I'll see when I get there
I hope they're prepared for the prince of Bel-Air
Well, the plane landed and when I came out
There was a dude who looked like a cop standing there with my name out
I ain't trying to get arrested yet
I just got here
I sprang with the quickness like lightning, disappeared
I whistled for a cab and when it came near
The license plate said fresh and it had dice in the mirror
If anything I could say that this cab was rare
But I thought 'Nah, forget it' - 'Yo, holmes to Bel Air'
I pulled up to the house about 7 or 8
And I yelled to the cabbie 'Yo holmes smell ya later'
I looked at my kingdom
I was finally there
To sit on my throne as the Prince of Bel Air"""

# freq = {"A": 0, "B":0, "C": 0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "X":0, "Y":0, "Z":0} 

freq = {}

def analyse(englishtext):
    """Analyse some English text and print out the percentage of letters that are A's, B;s etc. And 'A' and an 
    'a' count as the same letter. Keep the letter count in a dictionary called freq. Use this dictionary to 
    print out the letter (in upper case) and the frequency of the letter.  """
    
    #Example on set()method
    
  
    for letter in text:
        
        if letter.isalpha():
            letter = letter.upper()
            if letter in freq:
                freq[letter] = freq[letter] + 1
            else:
                freq[letter] = 1
    
    print(freq)
    #Your code goes here

analyse(text)