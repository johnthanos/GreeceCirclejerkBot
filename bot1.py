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

    if (comment.id not in posts_replied_to) and not(comment.author == 'GreeceCirclejerkBot'):
        # Respond for Ax, ti leei, kalhspera sas comment
        if re.search("Αχ ", comment.body, re.IGNORECASE):
            print(comment.body)

            ax_reply = "Όταν μπήκες κάτω από το φορτηγό και έβαλες την πλάτη να σηκώσεις την καμπάνα είπα: Αυτός ο " \
                       "άνθρωπος κρατάει γυναίκα, τρία παιδιά, γέρο πατέρα, άρρωστη αδερφή, εμένα, τους φίλους του, " \
                       "τον ΠΑΟΚ και η ζωή πως τον πληρώνει; Με ψίχουλα, με τίποτα. Αυτό είπα. Θα έρθει μια μέρα που" \
                       "η ζωή θα αλλάξει. Εμείς δεν θα υπάρχουμε τότε, αλλά δεν πειράζει. Αρκεί που θα μας σκεφτούν." \
                       " Θα θυμηθούν πως ζήσαμε και εμείς κάποτε."
            comment.reply(ax_reply)
        elif re.search("τι λεει", comment.body, re.IGNORECASE)or re.search("τι λέει", comment.body, re.IGNORECASE):
            print(comment.body)
            ax_reply = "Γιατί δεν πέφτεις εσύ να πνιγείς;"
            comment.reply(ax_reply)
        elif re.search("καλησπερα σας", comment.body, re.IGNORECASE) or re.search("καλησπέρα σας", comment.body, re.IGNORECASE):
            print(comment.body)
            ax_reply = "Δύο Jack Daniels, το ένα διπλό."
            comment.reply(ax_reply)
        elif re.search("καταλαβα", comment.body, re.IGNORECASE) or re.search("κατάλαβα", comment.body, re.IGNORECASE):
            print(comment.author)
            ax_reply = "Σκέψου πρώτα, κατάλαβε και μετά πες δεν καταλαβαίνω!"
            comment.reply(ax_reply)
        elif re.search("i5", comment.body, re.IGNORECASE) or re.search("ι5", comment.body, re.IGNORECASE):
            print(comment.body)
            ax_reply = "Τι είπες για μένα πουτανίτσα; Θα έπρεπε να ξέρεις ότι βγήκα πρώτος στο ΣΠΕΝ των Ειδικών Δυνάμεων" \
                       " στον  Έβρο, και έχω κάνει υπηρεσία σκοπός πύλης πάνω από 300 φορές. Είμαι εκπαιδευμένος στην " \
                       "διευθέτηση κλίνης και είμαι ο τοπ στρατιώτης των Ένοπλων Δυνάμεων της Ελλάδας. Δεν είσαι τίποτα" \
                       " για μένα παρά μόνο άλλος ένας στόχος. Θα σε διαλύσω με ακρίβεια που δεν έχει ξαναδεί ο πλανήτης " \
                       "γη, θυμήσου τα λόγια μου. Νομίζεις ότι θα την γλιτώσεις λεγοντάς μου μαλακίες από το ΚΕΠΙΚ; " \
                       "Ξανασκέψου το. Αυτήν την στιγμή επικοινωνώ με τους Διαβιβαστές του λόχου και έχουμε βρει το IP " \
                       "σου, γι’αυτό καλύτερα να ετοιμαστείς για τον τυφώνα. Τον τυφώνα που θα εξαλείψει το αξιολύπητο " \
                       "πράγμα που αποκαλείς ζωή. Είσαι νεκρός μικρέ. Μπορώ να είμαι παντού, πάντα, και μπορώ να σε " \
                       "σκοτώσω με 700 διαφορετικούς τρόπους, και αυτοί μόνο με το G3A3. Όχι μόνο έχω μάθει όλα τα " \
                       "παραγγέλματα, άλλα έχω και πρόσβαση σε όλα τα αρχεία του Ελληνικού Στρατού, και θα τα " \
                       "χρησιμοποιήσω για να σε εξαφανίσω από την χώρα. Αν ήξερες τι επιπτώσεις θα σου έφερνε αυτό το" \
                       " ‘’έξυπνο’’ σχόλιο, ίσως να το είχες βουλώσει. Αλλά δεν το έκανες και τώρα θα πληρώσεις το " \
                       "τίμημα. Θα χέσω θυμό πάνω σου και θα πνιγείς μέσα του. Είσαι νεκρός μικρέ."
            comment.reply(ax_reply)
        elif re.search("κλαμα", comment.body, re.IGNORECASE) or re.search("fake news", comment.body, re.IGNORECASE):
            ax_reply = "Εγώ σας λέω ότι είναι fake news. Αναρωτηθείτε! Ρωτήστε τους εαυτούς σας! Τους είδαμε να κλαίνε?" \
            "Υπάρχουν στοιχεία; Όχι. Παραμόνο ισχυρισμοί. Αν όντως είναι fake news, τι λόγο έχουν για να μας πουν ψέματα; " \
            "Μήπως θέλουν να δημιουργήσουν εντυπώσεις; Μήπως η κυβέρνηση της διαφθοράς που παρέδωσε την χώρα στους ξένους" \
            " αφήνουν να διαρρεύσουν τέτοιες ψευτιές για να \"καταλάβουν\" οι άλλοι μετά από αυτούς που θα τολμήσουν έστω "\
            "να διανοηθούν να κάνουν κάτι τέτοιο, τι ακολουθεί.. Μήπως φοβούνται τις συνέπειες των πράξεων τους και " \
            "πιστεύουν ότι έτσι θα γλιτώσουν/θα προλάβουν τα χειρότερα που ίσως ακολουθήσουν σε περιπτώσει που παραδώσουν " \
            "ακόμα και ιστορία; δλδ το όνομα Μακεδονία"
            comment.reply(ax_reply)
            
        # Store the current id into our list and read file
        posts_replied_to.append(comment.id)
        with open("posts_replied_to.txt", "a") as f:
            f.write(comment.id + "\n")


