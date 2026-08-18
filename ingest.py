import os
import random
from datetime import datetime, timezone

import dns.resolver
from pymongo import MongoClient
from faker import Faker

# Configure DNS resolvers
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ["8.8.8.8", "1.1.1.1"]

# Initialize Faker
fake = Faker()

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")


def run_mock_ingestion():
    if not MONGO_URI:
        raise ValueError("Error: MONGO_URI environment variable is missing.")

    client = MongoClient(MONGO_URI)

    try:
        print("Connecting to MongoDB Atlas...")

        db = client["SecurityDB"]
        collection = db["logs"]

        print("Generating 5 mock security documents...")

        mock_records = []

        products = [
            "SentinelOne",
            "Cisco Duo",
            "Okta",
            "Splunk",
            "Microsoft 365 Defender"
        ]

        severities = ["low", "medium", "high", "critical"]

        statuses = [
            "open",
            "closed",
            "resolved",
            "investigating"
        ]

        # Generate exactly 5 records per run
        for _ in range(5):
            mock_records.append({
                "product": random.choice(products),
                "severity": random.choice(severities),
                "status": random.choice(statuses),
                "source_ip": fake.ipv4(),
                "user": fake.user_name(),
                "timestamp": datetime.now(timezone.utc)
            })

        print("Ingesting records into SecurityDB.logs...")

        result = collection.insert_many(mock_records)

        print("------------------------------------------------")
        print(f"SUCCESS! Ingested {len(result.inserted_ids)} records into MongoDB!")
        print("------------------------------------------------")

    except Exception as e:
        print(f"An error occurred during ingestion: {e}")

    finally:
        client.close()


if __name__ == "__main__":
    run_mock_ingestion()
