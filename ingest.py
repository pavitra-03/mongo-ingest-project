import dns.resolver
from pymongo import MongoClient
from faker import Faker
import random
from datetime import datetime

# Set public DNS resolvers to handle corporate VPN DNS issues
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '1.1.1.1']

# Initialize Faker generator
fake = Faker()

# Your MongoDB Atlas URI with simple credentials
uri = "mongodb+srv://appuser:Pass12345@cluster0.fsr660u.mongodb.net/?retryWrites=true&w=majority"

# Initialize MongoClient with SSL bypass for corporate network/VPN inspection
client = MongoClient(
    uri,
    tls=True,
    tlsAllowInvalidCertificates=True
)

def run_mock_ingestion():
    try:
        print("Connecting to MongoDB Atlas...")
        db = client["SecurityDB"]
        collection = db["logs"]

        print("Generating 5 mock security documents...")
        mock_records = []

        products = ["SentinelOne", "Cisco Duo", "Okta", "Splunk", "Microsoft 365 Defender"]
        severities = ["low", "medium", "high", "critical"]
        statuses = ["open", "closed", "resolved", "investigating"]

        # Exactly 5 records generated per run
        for _ in range(5):
            mock_records.append({
                "product": random.choice(products),
                "severity": random.choice(severities),
                "status": random.choice(statuses),
                "timestamp": datetime.utcnow()
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