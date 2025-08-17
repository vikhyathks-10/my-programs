def feedback_collector():
    feedbacks = {}
    while True:
        name = input("Enter your name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        feedback = input("Enter your feedback: ")
        feedbacks[name] = feedback
    print("\nAll Feedbacks:")
    for name, fb in feedbacks.items():
        print(f"{name}: {fb}")

feedback_collector()
