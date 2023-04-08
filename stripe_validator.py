import stripe
from termcolor import colored

with open("key.txt", "r") as f:
    api_keys = [line.strip() for line in f.readlines()]

with open("validkey.txt", "w") as f_valid:
    for api_key in api_keys:
        stripe.api_key = api_key
        try:
            stripe.Balance.retrieve()
            f_valid.write(f"{api_key}\n")
            print(colored(f"API Valid: {api_key}", "green"))
        except stripe.error.AuthenticationError as e:
            print(colored(f"API Invalid: {api_key}", "red"))
            continue

answer = input("Do you want to continue to check the balance? (y/n): ")
if answer.lower() == "y":
    with open("validkey.txt", "r") as f:
        api_keys = [line.strip() for line in f.readlines()]

    with open("results.txt", "w") as f:
        for api_key in api_keys:
            stripe.api_key = api_key
            balance = stripe.Balance.retrieve()
            available_amount = balance["available"][0]["amount"]
            currency = balance["available"][0]["currency"]
            # Menyimpan hasil ke file found.txt
            f.write(f"Key : {api_key}\nBalance : available {available_amount} {currency}\n\n")
    print("Done checking Results.txt")
else:
    print("Exiting without checking balance.")
