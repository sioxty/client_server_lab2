import logging
import csv
from client import ApiClient

logging.basicConfig(level=logging.INFO)


def save_to_csv(filename: str, facts: list[str]) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["fact"])
        for item in facts:
            writer.writerow([item])


def main():
    client = ApiClient()

    facts = client.get_facts(count=5)
    logging.info("Отримано %d фактів про котів", len(facts))

    save_to_csv("meow_facts.csv", facts)
    logging.info("Факти збережено у meow_facts.csv")


if __name__ == "__main__":
    main()
