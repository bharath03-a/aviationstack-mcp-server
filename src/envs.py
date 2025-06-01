from dotenv import load_dotenv
import os

load_dotenv()

FLIGHTSTACK_API_KEY = os.getenv("FLIGHTSTACK_API_KEY")

if FLIGHTSTACK_API_KEY is None:
    raise EnvironmentError("Missing FLIGHTSTACK_API_KEY in .env file")