# app.py (Final Corrected)
import os
from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve
import teslapy
import webbrowser

# --- Configuration ---
TESLA_EMAIL = os.environ.get('TESLA_EMAIL')
CACHE_FILE = 'cache.json'

if not TESLA_EMAIL:
    raise ValueError("TESLA_EMAIL environment variable not set. Please set it before running.")

app = Flask(__name__)
CORS(app)

tesla = teslapy.Tesla(TESLA_EMAIL, cache_file=CACHE_FILE)

# --- One-Time Authentication Function ---
def setup_authentication():
    if not tesla.authorized:
        print('--- TeslaPy Authentication Setup ---')
        auth_url = tesla.authorization_url()
        print(f"\nPlease open this URL in your browser:\n{auth_url}\n")
        url = input("After logging in, paste the full URL of the blank page here: ")
        tesla.fetch_token(authorization_response=url)
        print('--- Authentication Successful! ---')

# --- API Endpoints ---
@app.route('/api/live_status', methods=['GET'])
def get_live_status():
    try:
        # Step 1: Get the list of battery objects
        powerwalls = tesla.battery_list()
        
        if not powerwalls:
            return jsonify({'error': 'No energy sites (Powerwalls) found on this account.'}), 404
        
        # Step 2: Use the first powerwall object from the list
        powerwall = powerwalls[0]
        
        # Step 3: Get the live status from that specific powerwall object
        live_status = powerwall.get_live_status()

        return jsonify(live_status)

    except Exception as e:
        import traceback
        print(f"An error occurred in get_live_status: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("--- Starting TeslaPy API Server (Final) ---")
    setup_authentication()
    print("--- Server is now running on port 5000 ---")
    serve(app, host='0.0.0.0', port=5000)