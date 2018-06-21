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
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Όταν μπήκες κάτω από το φορτηγό και έβαλες την πλάτη να σηκώσεις την καμπάνα είπα: Αυτός ο " \
                       "άνθρωπος κρατάει γυναίκα, τρία παιδιά, γέρο πατέρα, άρρωστη αδερφή, εμένα, τους φίλους του, " \
                       "τον ΠΑΟΚ και η ζωή πως τον πληρώνει; Με ψίχουλα, με τίποτα. Αυτό είπα. Θα έρθει μια μέρα που" \
                       "η ζωή θα αλλάξει. Εμείς δεν θα υπάρχουμε τότε, αλλά δεν πειράζει. Αρκεί που θα μας σκεφτούν." \
                       " Θα θυμηθούν πως ζήσαμε και εμείς κάποτε."
            comment.reply(ax_reply)
        elif re.search("τι λεει", comment.body, re.IGNORECASE)or re.search("τι λέει", comment.body, re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Γιατί δεν πέφτεις εσύ να πνιγείς;"
            comment.reply(ax_reply)
        elif re.search("καλησπερα σας", comment.body, re.IGNORECASE) or re.search("καλησπέρα σας", comment.body,
                                                                                  re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Δύο Jack Daniels, το ένα διπλό."
            comment.reply(ax_reply)
        elif re.search("καταλαβα", comment.body, re.IGNORECASE) or re.search("κατάλαβα", comment.body, re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Σκέψου πρώτα, κατάλαβε και μετά πες δεν καταλαβαίνω!"
            comment.reply(ax_reply)
        elif re.search("i5", comment.body, re.IGNORECASE) or re.search("ι5", comment.body, re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Τι είπες για μένα πουτανίτσα; Θα έπρεπε να ξέρεις ότι βγήκα πρώτος στο ΣΠΕΝ των Ειδικών " \
                       "Δυνάμεω στον  Έβρο, και έχω κάνει υπηρεσία σκοπός πύλης πάνω από 300 φορές. Είμαι " \
                       "εκπαιδευμένος στην διευθέτηση κλίνης και είμαι ο τοπ στρατιώτης των Ένοπλων Δυνάμεων της " \
                       "Ελλάδας. Δεν είσαι τίποτα για μένα παρά μόνο άλλος ένας στόχος. Θα σε διαλύσω με ακρίβεια " \
                       "που δεν έχει ξαναδεί ο πλανήτης γη, θυμήσου τα λόγια μου. Νομίζεις ότι θα την γλιτώσεις " \
                       "λεγοντάς μου μαλακίες από το ΚΕΠΙΚ; Ξανασκέψου το. Αυτήν την στιγμή επικοινωνώ με τους " \
                       "Διαβιβαστές του λόχου και έχουμε βρει το IP σου, γι’αυτό καλύτερα να ετοιμαστείς για τον " \
                       "τυφώνα. Τον τυφώνα που θα εξαλείψει το αξιολύπητο πράγμα που αποκαλείς ζωή. Είσαι νεκρός " \
                       "μικρέ. Μπορώ να είμαι παντού, πάντα, και μπορώ να σε σκοτώσω με 700 διαφορετικούς τρόπους, " \
                       "και αυτοί μόνο με το G3A3. Όχι μόνο έχω μάθει όλα τα παραγγέλματα, άλλα έχω και πρόσβαση σε " \
                       "όλα τα αρχεία του Ελληνικού Στρατού, και θα τα χρησιμοποιήσω για να σε εξαφανίσω από την " \
                       "χώρα. Αν ήξερες τι επιπτώσεις θα σου έφερνε αυτό το ‘’έξυπνο’’ σχόλιο, ίσως να το είχες " \
                       "βουλώσει. Αλλά δεν το έκανες και τώρα θα πληρώσεις το τίμημα. Θα χέσω θυμό πάνω σου και θα " \
                       "πνιγείς μέσα του. Είσαι νεκρός μικρέ."
            comment.reply(ax_reply)
        elif re.search("κλαμα", comment.body, re.IGNORECASE) or re.search("fake news", comment.body, re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Εγώ σας λέω ότι είναι fake news. Αναρωτηθείτε! Ρωτήστε τους εαυτούς σας! Τους είδαμε να " \
                       "κλαίνε? Υπάρχουν στοιχεία; Όχι. Παραμόνο ισχυρισμοί. Αν όντως είναι fake news, τι λόγο έχουν " \
                       "για να μας πουν ψέματα; Μήπως θέλουν να δημιουργήσουν εντυπώσεις; Μήπως η κυβέρνηση της " \
                       "διαφθοράς που παρέδωσε την χώρα στους ξένους αφήνουν να διαρρεύσουν τέτοιες ψευτιές για να " \
                       "\"καταλάβουν\" οι άλλοι μετά από αυτούς που θα τολμήσουν έστω να διανοηθούν να κάνουν κάτι " \
                       "τέτοιο, τι ακολουθεί.. Μήπως φοβούνται τις συνέπειες των πράξεων τους και πιστεύουν ότι έτσι " \
                       "θα γλιτώσουν/θα προλάβουν τα χειρότερα που ίσως ακολουθήσουν σε περιπτώσει που παραδώσουν " \
                       "ακόμα και ιστορία; δλδ το όνομα Μακεδονία"
            comment.reply(ax_reply)
        elif re.search("ραδιόφωνο", comment.body, re.IGNORECASE) or re.search("ράδιο", comment.body, re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Σι-Ντι!"
            comment.reply(ax_reply)
        elif re.search("ti eisai", comment.body, re.IGNORECASE) or re.search("τι είσαι", comment.body, re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Είμαι Αριστερός από το 1950 ενώ άλλοι κοιμόντουσαν με την αφίσα του βασιλέα εγώ είχα την " \
                       "αφίσα του Μαρξ. Θεωρώ ντροπή κάποιος να μπερδεύει την προοδευτική κομμουνιστικη αριστερά " \
                       "με ένα κακόγουστο αστείο.Όχι δεν είναι αστείο να μιμαρεις την μεγάλη έννοια και ιδέα της " \
                       "ΑΡΙΣΤΕΡΑΣ με την ποταπή ιδεολογία ΣΥΡΙΖΑ. Είναι γελοίο μέχρι αηδίας άνθρωποι σαν και εσένα, " \
                       "που σίγουρα στο σχολικό θίασο σήκωνες το χέρι σου για να υποδυθείς τον Ζέρβα να θες να " \
                       "λέγεσαι σοσιαλιστής. Μικρέ μάζεψε τα πράγματα σου και πήγαινε στα βουνά γιατί η ανατροπή " \
                       "θα έρθει και όταν έρθει θα είσαι ο πρώτος που θα νιώσει την οργή του ψυχολογικά ρακένδυτου " \
                       "αλλά αληθινού αριστερού Έλληνα και τότε κανένα ονλαιν μαιμς δεν θα σε σώσει.Να προσέχεις. ;)"
            comment.reply(ax_reply)
        elif re.search("μαλακια σαμπ", comment.body, re.IGNORECASE) or re.search("malakia sub", comment.body, re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Μάλιστα... Όμως, κυρίες και κύριοι· παραλάβαμε πραγματικά καμένη γη!"
            comment.reply(ax_reply)
        elif re.search("τουρκαλες", comment.body, re.IGNORECASE) or re.search("toyrkales", comment.body, re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Εδώ στη Γερμανία οι Τουρκάλες μας βλέπουν τους Έλληνες σαν ξερολούκουμα. Μας θεωρούν πιο " \
                       "σοφιστικέ και εκλεπτισμένους από τους Τούρκους, που τους θεωρούν χωριάτες και γύφτους. " \
                       "Τρελαίνονται να τις γαμάμε, θέλουν συνέχεια ελληνική πούτσα, κι όταν γαμιούνται με Έλληνα " \
                       "φωνάζουν στα τούρκικα κάτι ερεθιστικά πράγματα, που μάλλον είναι κραυγές υποταγής, " \
                       "μαζοχισμού, σκλαβιάς, και άλλα οθωμανικά φετίχ. Εμείς οι Ρωμηοί, λένε, δεν έχουμε μπέσα " \
                       "και φιλότιμο, και αυττό τους ερεθίζει, γιατί με το δαιμόνιό μας ξεφύγαμε από τη γυφτιά και " \
                       "πήγαμε στην Ευρώπη. Βάλε και χιλιετίες ιστορίας, βάλε και την τραγίλα των Μεμέτηδων, που " \
                       "μιλάνε και γελάν οι πέτρες, οι Τουρκάλες παρακαλάνε στα γόνατα μονάχα να μυρίσουν ελληνική " \
                       "βάλανο, όχι να την γλείψουν, εκεί ήδη κλαίνε. Οπότε μη φοβάστε, οι Τούρκοι θα πολεμούν, και " \
                       "οι γυναίκες τους θα τρίβονται με τη σκέψη πως ο Έλλην πεζοναύτης θα μπει μια μέρα να τις " \
                       "βατέψει με φορώντας λασπωμένες αρβύλες και κάλτσες βρώμικες. "
            comment.reply(ax_reply)
        elif re.search("skopia", comment.body, re.IGNORECASE) or re.search("σκοπια", comment.body, re.IGNORECASE) or \
                re.search("σκόπια", comment.body, re.IGNORECASE):
            print("{}:{}".format(comment.author, comment.body))
            ax_reply = "Ο μονος λογος που τα Σκοπια εχουν κρατησει την ιστορια αυτή 25 χρονια και απεσπασαν οριστικα " \
                       "το ονομα, την γλωσσα και την ταυτοτητα είναι επειδή η Εβραικη Κοινοτητα Θεσσαλονικης θελει " \
                       "να εκδικηθεί το συνολο των Ελλήνων για την απελευθερωση το 1912, στο ονομα της Μακεδονιας " \
                       "και του Αλεξανδρου, την πυρκαγια του 1917 και την τελικη τους εξοντωση το 1943. Για την " \
                       "απωλεια της Ιερουσαλημ των Βαλκανιων, όπως την αποκαλει ο κολλητος Μπουταρης. Δεν είναι " \
                       "τυχαιο ότι η ιστορια της διαπραγματευσης ξεκινησε τον Σεπτεμβρη του 2017, δηλαδη 100 χρονια " \
                       "και ένα μηνα από την πυρκαγια του 17 κατά την οποια καηκε ολη η Εβραικη συνοικια. Γιατι " \
                       "εχουν την εκδικηση και τους συμβολισμους αυτης βαθια μεσα στην κουλτουρα τους. Θα τους " \
                       "ικανοποιει διαστρεμμενα επισης ότι αυτό συμβαινει λιγο πριν συμπληρωθουν 100 χρονια από το " \
                       "1922. Γιατι ηδονιζονται στην σκεψη ότι προκαλεσαν άλλη μια «εθνικη καταστροφη/τραγωδια» για " \
                       "την οποια οι Ελληνες θα γκρινιαζουν για αλλα 100 χρονια. Εχουν πιασει την Ουάσιγκτον, τις " \
                       "Βρυξελλες και φυσικα το παντα προθυμο ελληνικο πολιτικο προσωπικο. Όλα τα ΜΜΕ συμμετεχουν " \
                       "στην πλεκτανη για να εχουν κρατικη διαφημιση, διευκολύνσεις και θαλασσοδάνεια. Για αυτό η " \
                       "αδιακοπη υποτιμητικη προπαγανδα συνολικα από όλα τα μεσα ακομα και τα παραδοσιακα πατριωτι" \
                       "κα/συντηρητικα. Η εντολη των Εβραιων της Θεσσαλονικης στον Τσιπρα είναι δωστε το ονομα και " \
                       "τριψτε το τους στη μουρη. Ταπεινώστε τους. Εμας το λαο. Για αυτό και η υπογραφη θα γινει σε " \
                       "ελληνικο εδαφος στις Πρεσπες, εκει που είναι ο μεγαλύτερος πληθυσμος Σλαβόφωνων."
            comment.reply(ax_reply)
            
        # Store the current id into our list and read file
        posts_replied_to.append(comment.id)
        with open("posts_replied_to.txt", "a") as f:
            f.write(comment.id + "\n")


