# Python program: Arbitrary Arguments (*args and **kwargs)
# Date: 2026-08-30

def sum_all(*args):
    return sum(args)

def print_user_profile(username, **kwargs):
    print(f"User: {username}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    print("Sum of numbers:", sum_all(10, 20, 30, 40))
    print_user_profile("Frozen-47", role="Student", repo="PythonLearning", status="Active")
