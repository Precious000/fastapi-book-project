import requests
import time

URL = "http://127.0.0.1:8000/stage2"

# Step 1: Ensure the route is missing (expecting 404)
response = requests.get(URL)
assert response.status_code == 404, f"❌ Expected 404, but got {response.status_code}"
print("✅ Initial failure confirmed.")

# Step 2: Add the route dynamically to main.py
with open("main.py", "a") as f:
    f.write(
        """
@app.get("/stage2")
async def stage2():
    return {"message": "Welcome to stage 2"}
"""
    )

print("🔧 Route /stage2 added to main.py")

# Step 3: Restart the FastAPI server (assuming it's running on uvicorn)
import os
os.system("pkill -f 'uvicorn'")  # Kill the old process
time.sleep(2)
os.system("uvicorn main:app --host 127.0.0.1 --port 8000 &")
time.sleep(5)  # Give it time to start

# Step 4: Re-test after adding the route (expecting 200)
response = requests.get(URL)
assert response.status_code == 200, f"❌ Expected 200 OK, but got {response.status_code}"
print("✅ Route successfully added and verified!")

