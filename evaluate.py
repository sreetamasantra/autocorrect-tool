from autocorrect import correct_word

# Standard test set: (misspelled, expected_correct)
test_cases = [
    ("speling",    "spelling"),
    ("korrect",    "correct"),
    ("waht",       "what"),
    ("wrold",      "world"),
    ("hav",        "have"),
    ("dreem",      "dream"),
    ("becuase",    "because"),
    ("freind",     "friend"),
    ("recieve",    "receive"),
    ("occured",    "occurred"),
    ("untill",     "until"),
    ("seperate",   "separate"),
    ("definately", "definitely"),
    ("goverment",  "government"),
    ("begining",   "beginning"),
    ("beleive",    "believe"),
    ("calender",   "calendar"),
    ("enviroment", "environment"),
    ("knowlege",   "knowledge"),
    ("neccessary", "necessary"),
]

correct = 0
print(f"{'Misspelled':<15} {'Expected':<15} {'Got':<15} {'✓/✗'}")
print("-" * 55)

for misspelled, expected in test_cases:
    got = correct_word(misspelled)
    match = got == expected
    if match:
        correct += 1
    print(f"{misspelled:<15} {expected:<15} {got:<15} {'✅' if match else '❌'}")

accuracy = (correct / len(test_cases)) * 100
print(f"\nAccuracy: {correct}/{len(test_cases)} = {accuracy:.1f}%")