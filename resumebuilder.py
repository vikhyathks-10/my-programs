name = input("Enter your name: ")
email = input("Enter your email: ")
education = input("Enter your education details: ")
skills = input("Enter your skills (comma-separated): ")
experience = input("Enter your work experience: ")

resume = f"""
--- Resume ---
Name: {name}
Email: {email}

Education:
{education}

Skills:
{skills}

Experience:
{experience}
"""

print("\nGenerated Resume:")
print(resume)
with open("resume.txt", "w") as file:
    file.write(resume)

print("✅ Resume saved as 'resume.txt'")
print("Thank you for using the Resume Builder!")