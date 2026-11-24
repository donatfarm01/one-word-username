"""Write the entry for the One Word, One Username, One Reward bounty.

The entry is the entrant's own make.fun username, one word and nothing
else: donatfarm01. The program writes exactly that word, with no
trailing newline and no extra text, so the sealed gate reads 11 bytes.

The gate allows 1 to 30 characters of UTF-8 text, not only white space,
so the program checks its own output against that shape before writing:
a single word, no spaces, no padding.
"""

USERNAME = "donatfarm01"


def main():
    if not (1 <= len(USERNAME) <= 30):
        raise ValueError("username must be 1 to 30 characters")
    if any(ch.isspace() for ch in USERNAME):
        raise ValueError("username must be a single word")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
