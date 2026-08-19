# mongo-ingest-project
Automation for ingesting the data in mongoDB
# Security Logs Mock Data Ingestion Pipeline

A lightweight, automated Python ingestion pipeline that generates mock security log events (SentinelOne, Okta, Cisco Duo, Splunk, Microsoft 365 Defender) using `Faker` and ingests them into a **MongoDB Atlas** database cluster.

## Features

* **Automated Execution:** Runs on a scheduled schedule using GitHub Actions.
* **Realistic Security Logs:** Generates randomized security event logs including IP addresses, usernames, severity levels, and timestamps.
* **Secure Setup:** Uses GitHub Repository Secrets to protect sensitive connection strings without hardcoding credentials in source code.

---

## Tech Stack

* **Language:** Python 3.x
* **Database:** MongoDB Atlas (`pymongo`)
* **Automation:** GitHub Actions
* **Libraries:** `faker`, `dnspython`, `pymongo`

---

## Security & Configuration

This project requires a connection to a MongoDB cluster. **Never hardcode your credentials in source files.**

### Setting up Environment Variables

1. Go to your GitHub Repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Click **New repository secret**.
3. Create a secret named `MONGO_URI` with your connection string:
   ```text
   mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority

Local Installation & Usage
To run the ingestion script locally:

*Clone the repository:
git clone [https://github.com/pavitra-03/mongo-ingest-project.git]
(https://github.com/pavitra-03/mongo-ingest-project.git)
cd mongo-ingest-project

*Install dependencies:
pip install -r requirements.txt

*Set the environment variable:
Linux/MacOS - Set the environment variable:
Windows (PowerShell): $env:MONGO_URI="your_mongodb_connection_string"

*Run the script
python mongodb_ingest.py
