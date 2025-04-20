from argparse import ArgumentParser
import csv
from pathlib import Path
from datetime import date

parser = ArgumentParser()

parser.add_argument("--balance", action="store_true", help="Show current balances and exit")
parser.add_argument("-S", "--statement", type=str, help="Saves the Statement")
parser.add_argument("--type", type=str, help="Is it Expense(Exp), Revenue(R), or Transfer(Trans)",
                    choices=["Exp", "R", "Trans"])
parser.add_argument("-C", "--cash", type=int, help="Cash Amount")
parser.add_argument("-B", "--bank", type=int, help="Bank Amount")

args = parser.parse_args()

# Path and file
file_path = Path.cwd() / "budget.csv"

CashBalance = 0
BankBalance = 0

# If balance is provided!
if args.balance:
    if file_path.exists():
        with open(file_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if bool(row["Cash"]) and not bool(row["Bank"]):
                    CashBalance += int(row["Cash"])
                elif not bool(row["Cash"]) and bool(row["Bank"]):
                    BankBalance += int(row["Bank"])
                else:
                    CashBalance += int(row["Cash"])
                    BankBalance += int(row["Bank"])

    print(f"\n💰 Your Cash Balance is: {CashBalance}")
    print(f"🏦 Your Bank Balance is: {BankBalance}\n")
    exit() # Skip everything else!!!

# ⛔ If --balance is NOT provided, these are required:
if not args.statement or not args.type:
    parser.error("The following arguments are required unless using --balance: --statement, --type")

# Check if file exists, to decide on writing header
is_header_needed = not file_path.exists()

# ✅ Write to CSV if it's not just balance
with open(file_path, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Date", "Statement", "Cash", "Bank"])
    if is_header_needed:
        writer.writeheader()

    data = {
        "Date": date.today(),
        "Statement": args.statement,
        "Cash": 0,
        "Bank": 0
    }

    if args.type == "R":
        data["Cash"] = args.cash or 0
        data["Bank"] = args.bank or 0
    elif args.type == "Exp":
        data["Cash"] = -(args.cash or 0)
        data["Bank"] = -(args.bank or 0)
    elif args.type == "Trans":
        if args.cash:
            data["Cash"] = -args.cash
            data["Bank"] = args.bank or 0
        elif args.bank:
            data["Cash"] = args.cash or 0
            data["Bank"] = -args.bank

    writer.writerow(data)
    print("\n✅ Transaction saved!\n")

with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if bool(row["Cash"]) and not bool(row["Bank"]):
                CashBalance += int(row["Cash"])
            elif not bool(row["Cash"]) and bool(row["Bank"]):
                BankBalance += int(row["Bank"])
            else:
                CashBalance += int(row["Cash"])
                BankBalance += int(row["Bank"])

print(f"\n💰 Your Cash Balance is: {CashBalance}")
print(f"🏦 Your Bank Balance is: {BankBalance}\n")