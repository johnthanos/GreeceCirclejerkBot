import praw
import pdb
import re
import os
"""
Script for bot that reads comments from greececirclejerk subreddit and responds accordingly, the allready parsed 
comments are saved in the post_replied_to.txt so we dont reply twice to the same post after a diffrent run.


"""

# Initialising praw submission object
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit('greececirclejerk')

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Parse each comment in the subreddit stream
for comment in subreddit.stream.comments():

    if comment.id not in posts_replied_to:
        # Respond for Ax, ti leei, kalhspera sas comment
        if re.search("Αχ ", comment.body, re.IGNORECASE):
            print(comment.body)

            ax_reply = "Όταν μπήκες κάτω από το φορτηγό και έβαλες την πλάτη να σηκώσεις την καμπάνα είπα: Αυτός ο " \
                       "άνθρωπος κρατάει γυναίκα, τρία παιδιά, γέρο πατέρα, άρρωστη αδερφή, εμένα, τους φίλους του, " \
                       "τον ΠΑΟΚ και η ζωή πως τον πληρώνει; Με ψίχουλα, με τίποτα. Αυτό είπα. Θα έρθει μια μέρα που" \
                       "η ζωή θα αλλάξει. Εμείς δεν θα υπάρχουμε τότε, αλλά δεν πειράζει. Αρκεί που θα μας σκεφτούν." \
                       " Θα θυμηθούν πως ζήσαμε και εμείς κάποτε."
            comment.reply(ax_reply)
        elif re.search("τι λεει", comment.body, re.IGNORECASE):
            print(comment.body)
            ax_reply = "Γιατί δεν πέφτεις εσύ να πνιγείς;"
            comment.reply(ax_reply)
        elif re.search("καλησπερα σας", comment.body, re.IGNORECASE):
            print(comment.body)
            ax_reply = "Δύο Jack Daniels, το ένα διπλό."
            comment.reply(ax_reply)

        # Store the current id into our list and read file
        posts_replied_to.append(comment.id)
        with open("posts_replied_to.txt", "a") as f:
            f.write(comment.id + "\n")


