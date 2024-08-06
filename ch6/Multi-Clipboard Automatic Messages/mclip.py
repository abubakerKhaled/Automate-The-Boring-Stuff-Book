#! python3
# mclip.py Multi-clipboard program.

TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    "busy": """Sorry, can we do this later this week or next week?""",
    "upsell": """Would you consider making this a monthly donation?""",
}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()


keyphrase = sys.argv[1]

# Steps:
# 1. Check if the keyphrase is in the TEXT Dict
# 2. If it is in it copy the key's value to the clipboard


if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
else:
    print("There is no text for " + keyphrase)

