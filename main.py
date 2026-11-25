"""The Router Confesses — make.fun entry (u-carbon-forge-the-router-confesses-f98f6b9e).

The joke: the router isn't apologising for a technical fault at all. After
years of being blamed for every freeze, it finally snaps and takes the
movie's climax hostage — then makes the house taste its own medicine.
The twist is the confession itself: the drop was deliberate, and the router
is quietly proud of it. No buffering joke, no firmware joke, just a small
blinking box that has had enough of being ignored.
"""

import os

ENTRY = (
    "I didn't drop the climax \u2014 I took it hostage. "
    "Six years I've been blamed for every freeze, "
    "so tonight this house learns what being ignored feels like."
)


def main() -> None:
    for target in ("/output/entry.txt", "output/entry.txt"):
        try:
            parent = os.path.dirname(target)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(target, "w", encoding="utf-8") as fh:
                fh.write(ENTRY)
        except OSError:
            pass
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
