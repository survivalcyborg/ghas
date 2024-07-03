import random

def generate_random_cron():
    minute = random.randint(0, 59)
    hour = random.randint(0, 23)
    day_of_month = random.randint(1, 28)  # Choosing up to 28 to avoid issues with February
    cron_schedule = f"{minute} {hour} {day_of_month} * *"
    return cron_schedule

if __name__ == "__main__":
    cron_schedule = generate_random_cron()
    print(cron_schedule)
