from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import datetime
import os
import logging

logger = logging.getLogger(__name__)


@api_view(["GET"])
def get_profile(request):
    try:
        # Fetch random cat fact
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_data = response.json()
        cat_fact = cat_data.get("fact", "Cats are mysterious creatures.")
    except Exception as e:
        logger.error(f"Error fetching cat fact: {e}")
        cat_fact = "Unable to fetch cat fact at the moment."

    data = {
        "status": "success",
        "user": {
            "email": os.getenv("USER_EMAIL", "unknown@example.com"),
            "name": os.getenv("USER_NAME", "Anonymous User"),
            "stack": os.getenv("USER_STACK", "Python/Django"),
        },
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "fact": cat_fact,
    }
    return Response(data)
