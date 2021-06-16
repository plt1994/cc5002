import os
dev_username = "patlopez"
username = os.getenv("USER")
ENV = "dev" if username == dev_username else "prod"