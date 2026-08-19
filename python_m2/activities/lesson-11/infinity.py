print("Demonstrating an infinite loop safely...")

test_value = 0
safety_counter = 0
while test_value <= 0:
    print(f"Round {safety_counter + 1}: still running...")
    safety_counter += 1
    if safety_counter == 3:
        print("Stopped safely with break!")
        break
