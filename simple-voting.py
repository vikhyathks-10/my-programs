candidates = ["Alice", "Bob", "Charlie"]
votes = {name: 0 for name in candidates}

print("Candidates:", ", ".join(candidates))
num_voters = int(input("Enter number of voters: "))

for i in range(num_voters):
    vote = input(f"Voter {i+1}, enter your vote: ").strip()
    if vote in votes:
        votes[vote] += 1
    else:
        print("Invalid vote!")
        continue
print("\n--- Voting Results ---")
for name, count in votes.items():
    print(f"{name}: {count} votes")
winner = max(votes, key=votes.get)
print(f"\n🏆 Winner: {winner} with {votes[winner]} votes!")
