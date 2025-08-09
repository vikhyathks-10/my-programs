import random
from plyer import notification
quotes = [
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "Push yourself, because no one else is going to do it for you.",
    "Your limitation—it’s only your imagination."
]

quote = random.choice(quotes)
notification.notify(
    title="🌟 Daily Motivation",
    message=quote,
    timeout=10  
)
