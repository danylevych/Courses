from logic import *

def not_two_per_once(first, second):
    return And(Or(first, second), Not(And(first, second)))

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
ASaid = And(AKnight, AKnave)
knowledge0 = And(
    not_two_per_once(AKnight, AKnave),
    Implication(AKnight, ASaid),
    Implication(AKnave, Not(ASaid))
)

# Puzzle 1
# A says "We are both knaves."
ASaid = And(AKnave, BKnave)
# B says nothing.
knowledge1 = And(
    not_two_per_once(AKnight, AKnave),
    not_two_per_once(BKnight, BKnave),
    Implication(AKnight, ASaid),
    Implication(AKnave, Not(ASaid))
)

# Puzzle 2
# A says "We are the same kind."
ASaid = Or(And(AKnave, BKnave), And(AKnight, BKnight))
# B says "We are of different kinds."
BSaid = Not(ASaid)
knowledge2 = And(
    not_two_per_once(AKnight, AKnave),
    not_two_per_once(BKnight, BKnave),
    Implication(AKnight, ASaid),
    Implication(AKnave, Not(ASaid)),
    Implication(BKnight, BSaid),
    Implication(BKnave, Not(BSaid))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
ASaid = Or(AKnave, AKnight)
# B says "A said 'I am a knave'."
# B says "C is a knave."
BSaid = And(
            AKnave,
            CKnave
)

# C says "A is a knight."
CSaid = AKnight

knowledge3 = And(
    not_two_per_once(AKnight, AKnave),
    not_two_per_once(BKnight, BKnave),
    not_two_per_once(CKnight, CKnave),
    Implication(AKnight, ASaid),
    Implication(AKnave, Not(ASaid)),
    Implication(BKnight, BSaid),
    Implication(BKnave, Not(BSaid)),
    Implication(CKnight, CSaid),
    Implication(CKnave, Not(CSaid))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
