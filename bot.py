import csv
from pathlib import Path

from twitter_client import post_tweet

TWEETS_FILE = Path("tweets.csv")


def get_next_tweet() -> tuple[int | None, str | None]:
    with TWEETS_FILE.open("r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    for index, row in enumerate(rows):
        if not row.get("Posted", "").strip():
            tweet = row.get("Tweet", "").strip()

            if tweet:
                return index, tweet

    return None, None


def mark_as_posted(target_index: int) -> None:
    with TWEETS_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        fieldnames = reader.fieldnames

    if not fieldnames:
        raise RuntimeError("tweets.csv has no column headers.")

    rows[target_index]["Posted"] = "tweet posted"

    with TWEETS_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    row_index, tweet = get_next_tweet()

    if row_index is None or tweet is None:
        print("No unposted tweets remain.")
        return

    post_tweet(tweet)
    mark_as_posted(row_index)

    print(f"Successfully posted: {tweet}")


if __name__ == "__main__":
    main()
