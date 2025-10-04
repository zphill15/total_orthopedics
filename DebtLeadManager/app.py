import os
import requests
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health_check():
    return {'status': 'healthy'}, 200

@app.route('/api/dashboard-data')
def get_dashboard_data():
    """Proxy endpoint to fetch dashboard data from n8n webhook"""
    try:
        # Fetch data from the n8n webhook
        response = requests.get(
            'https://n8n.srv884802.hstgr.cloud/webhook/nd_load_dashboard_data',
            timeout=30
        )
        
        # If webhook returns successful response, use it
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        
    except Exception as e:
        print(f"Webhook error: {e}")
    
    # Fallback to sample data when webhook fails
    # This uses the updated response structure from the user
    fallback_data = [
        {
            "row_number": 2,
            "Total Patients In Collection": 619,
            "Total Outstanding Debt In Collection": 137551.11,
            "Collected Debt": 5822.13,
            "Number of Debts Cleared": 56
        }
    ]
    
    return jsonify(fallback_data)

@app.route('/api/update-lead', methods=['POST'])
def update_lead():
    """Proxy endpoint to update lead status via n8n webhook"""
    try:
        # Get the request data
        data = request.get_json()
        
        if not data or 'phone_number' not in data:
            return jsonify({'error': 'Missing phone_number in request'}), 400
        
        # Prepare payload for n8n webhook
        update_string = data.get('update_string', 'donotcall')
        payload = {
            'update_string': update_string,
            'phone_number': data['phone_number']
        }
        
        # Send POST request to n8n webhook
        response = requests.post(
            'https://n8n.srv884802.hstgr.cloud/webhook/nd_update_lead',
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            return jsonify({'success': True, 'message': 'Lead updated successfully'})
        else:
            return jsonify({'error': f'Webhook returned status {response.status_code}'}), 500
            
    except requests.exceptions.RequestException as e:
        print(f"Update webhook error: {e}")
        return jsonify({'error': 'Failed to update lead', 'message': str(e)}), 500
    except Exception as e:
        print(f"Update error: {e}")
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

@app.route('/api/send-pay-link', methods=['POST'])
def send_pay_link():
    """Send payment link via n8n webhook"""
    try:
        # Get the request data
        data = request.get_json()
        
        if not data or 'payment_link' not in data:
            return jsonify({'error': 'Missing payment_link in request'}), 400
        
        # Prepare payload for n8n webhook
        payload = {
            'first_name': data.get('first_name', ''),
            'phone_number': data.get('phone_number', ''),
            'payment_link': data['payment_link']
        }
        
        # Send POST request to n8n webhook
        response = requests.post(
            'https://n8n.srv884802.hstgr.cloud/webhook/text_pay_link',
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            return jsonify({'success': True, 'message': 'Payment link sent successfully'})
        else:
            return jsonify({'error': f'Webhook returned status {response.status_code}'}), 500
            
    except requests.exceptions.RequestException as e:
        print(f"Send pay link webhook error: {e}")
        return jsonify({'error': 'Failed to send payment link', 'message': str(e)}), 500
    except Exception as e:
        print(f"Send pay link error: {e}")
        return jsonify({'error': 'Internal server error', 'message': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)