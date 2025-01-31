from django.shortcuts import redirect
from django.http import JsonResponse
import requests
import os

CLIENT_ID = os.getenv("CLIENT_ID", "your_client_id")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "your_client_secret")
REDIRECT_URI = os.getenv("REDIRECT_URI", "https://yourapp.railway.app/callback")  # To be updated later

def login(request):
    auth_url = f"https://smartapi.angelbroking.com/publisher-login?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code"
    return redirect(auth_url)

def callback(request):
    code = request.GET.get("code")
    if code:
        token_url = "https://smartapi.angelbroking.com/auth/token"
        payload = {
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
            "redirect_uri": REDIRECT_URI
        }
        response = requests.post(token_url, json=payload)
        if response.status_code == 200:
            access_token = response.json().get("access_token")
            return JsonResponse({"message": "Login successful!", "access_token": access_token})
        return JsonResponse({"error": "Failed to get access token"}, status=400)
    return JsonResponse({"error": "Authorization code missing"}, status=400)

