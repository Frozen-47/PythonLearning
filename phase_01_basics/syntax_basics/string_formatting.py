# Python program: Modern String Formatting Techniques
# Date: 2026-08-29

def demo_formatting():
    name = "Sabareesh"
    score = 98.456
    rank = 1

    # F-string formatting
    print(f"Student: {name}, Rank: {rank:02d}, Score: {score:.2f}%")

    # Format method
    print("Welcome {0}! Your target score is {1:.1f}".format(name, score))

if __name__ == "__main__":
    demo_formatting()
