from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template directly embedded (your provided template)
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Debt Campaign Form</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 2.5em;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .form-group {
            margin-bottom: 25px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
            font-size: 1.1em;
        }

        input, select, textarea {
            width: 100%;
            padding: 15px;
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            font-size: 16px;
            transition: all 0.3s ease;
            background: white;
        }

        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            transform: translateY(-2px);
        }

        .file-upload {
            position: relative;
            display: inline-block;
            width: 100%;
        }

        .file-input {
            position: absolute;
            opacity: 0;
            width: 100%;
            height: 100%;
            cursor: pointer;
        }

        .file-label {
            display: block;
            padding: 20px;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            text-align: center;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
        }

        .file-label:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(240, 147, 251, 0.3);
        }

        .csv-preview {
            display: none;
            margin-top: 20px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border: 2px solid #e9ecef;
        }

        .csv-preview h3 {
            color: #495057;
            margin-bottom: 15px;
        }

        .mapping-section {
            display: none;
            margin-top: 30px;
            padding: 25px;
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 15px;
        }

        .mapping-section h3 {
            color: #333;
            margin-bottom: 20px;
            text-align: center;
        }

        .name-choice-section {
            display: none;
            margin-top: 25px;
            padding: 20px;
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            border-radius: 15px;
            border: 2px solid #f8b500;
        }

        .name-choice-section h3 {
            color: #8b4513;
            margin-bottom: 15px;
            text-align: center;
        }

        .name-choice-item {
            background: white;
            margin-bottom: 15px;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #ddd;
        }

        .name-choice-row {
            margin-bottom: 10px;
            font-weight: 500;
            color: #333;
        }

        .name-options {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 8px;
        }

        .name-option {
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .name-option input[type="radio"] {
            width: auto;
            margin: 0;
        }

        .name-option label {
            margin: 0;
            padding: 5px 10px;
            background: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-weight: normal;
        }

        .name-option input[type="radio"]:checked + label {
            background: #667eea;
            color: white;
            border-color: #667eea;
        }

        .mapping-row {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            gap: 15px;
        }

        .mapping-row label {
            min-width: 150px;
            margin-bottom: 0;
            font-weight: 600;
            color: #2c3e50;
        }

        .mapping-row select {
            flex: 1;
        }

        .preview-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .preview-table th,
        .preview-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e9ecef;
        }

        .preview-table th {
            background: #6c757d;
            color: white;
            font-weight: 600;
        }

        .preview-table tr:hover {
            background-color: #f8f9fa;
        }

        .submit-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 18px 40px;
            border: none;
            border-radius: 50px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: block;
            margin: 30px auto 0;
            min-width: 200px;
        }

        .submit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
        }

        .submit-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .error-message {
            color: #dc3545;
            background: #f8d7da;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
            display: none;
        }

        .success-message {
            color: #155724;
            background: #d4edda;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            display: none;
            text-align: center;
            font-weight: 600;
        }

        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }

            .mapping-row {
                flex-direction: column;
                align-items: stretch;
                gap: 8px;
            }

            .mapping-row label {
                min-width: auto;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Debt Campaign Setup</h1>
        
        <form id="campaignForm">
            <div class="form-group">
                <label for="startDate">Campaign Start Date:</label>
                <input type="date" id="startDate" name="startDate" required>
            </div>

            <div class="form-group">
                <label for="timezone">Timezone:</label>
                <select id="timezone" name="timezone">
                    <option value="America/New_York" selected>America/New York (EST/EDT)</option>
                    <option value="America/Los_Angeles">America/Los Angeles (PST/PDT)</option>
                    <option value="America/Chicago">America/Chicago (CST/CDT)</option>
                    <option value="America/Denver">America/Denver (MST/MDT)</option>
                    <option value="America/Phoenix">America/Phoenix (MST)</option>
                    <option value="Europe/London">Europe/London (GMT/BST)</option>
                    <option value="Europe/Paris">Europe/Paris (CET/CEST)</option>
                    <option value="Asia/Tokyo">Asia/Tokyo (JST)</option>
                    <option value="Australia/Sydney">Australia/Sydney (AEST/AEDT)</option>
                </select>
            </div>

            <div class="form-group">
                <label for="numContacts">Number of Contacts:</label>
                <input type="number" id="numContacts" name="numContacts" min="1" required>
            </div>

            <div class="form-group">
                <label for="contactDays">Select Contact Days:</label>
                <select id="contactDays" name="contactDays">
                    <option value="weekdays">Weekdays (Mon-Fri)</option>
                    <option value="full_week">Full Week (Mon-Sun)</option>
                </select>
            </div>

            <div class="form-group">
                <label for="csvFile">Upload CSV File:</label>
                <div class="file-upload">
                    <input type="file" id="csvFile" name="csvFile" class="file-input" accept=".csv" required>
                    <label for="csvFile" class="file-label">
                        📁 Choose CSV File
                    </label>
                </div>
                <div class="error-message" id="fileError"></div>
            </div>

            <div class="csv-preview" id="csvPreview">
                <h3>CSV Preview (First 5 rows):</h3>
                <div id="previewContent"></div>
            </div>

            <div class="mapping-section" id="mappingSection">
                <h3>Map Your CSV Columns</h3>
                <p style="text-align: center; margin-bottom: 20px; color: #666;">
                    Select which columns from your CSV correspond to the required fields:
                </p>
                
                <div class="mapping-row">
                    <label for="firstNameMapping">First Name:</label>
                    <select id="firstNameMapping" name="firstNameMapping">
                        <option value="">-- Select Column --</option>
                    </select>
                </div>

                <div class="mapping-row">
                    <label for="phoneMapping">Phone Number:</label>
                    <select id="phoneMapping" name="phoneMapping">
                        <option value="">-- Select Column --</option>
                    </select>
                </div>

                <div class="mapping-row">
                    <label for="amountMapping">Amount Owed:</label>
                    <select id="amountMapping" name="amountMapping">
                        <option value="">-- Select Column --</option>
                    </select>
                </div>

                <div class="mapping-row">
                    <label for="dateOfServiceMapping">Date of Service:</label>
                    <select id="dateOfServiceMapping" name="dateOfServiceMapping">
                        <option value="">-- Select Column --</option>
                    </select>
                </div>
            </div>

            <div class="name-choice-section" id="nameChoiceSection">
                <h3>Set Name Pattern</h3>
                <p style="text-align: center; margin-bottom: 20px; color: #8b4513;">
                    Some entries have multiple names. Choose which part to use, and this pattern will be applied to all multi-name entries:
                </p>
                <div id="nameChoiceContainer"></div>
            </div>

            <button type="submit" class="submit-btn" id="submitBtn" disabled>
                Submit Campaign
            </button>
        </form>

        <div class="success-message" id="successMessage">
            ✅ Campaign submitted successfully!
        </div>
    </div>

    <script>
        let csvData = [];
        let csvHeaders = [];
        let namePattern = null; // Stores which part to use (index: 0=first, 1=second, etc.)
        let allMultiNameRows = []; // Stores all rows with multi-part names

        document.getElementById('csvFile').addEventListener('change', handleFileUpload);
        document.getElementById('campaignForm').addEventListener('submit', handleSubmit);

        // Set minimum date to today
        document.getElementById('startDate').min = new Date().toISOString().split('T')[0];

        function handleFileUpload(event) {
            const file = event.target.files[0];
            const errorDiv = document.getElementById('fileError');
            
            if (!file) {
                hidePreview();
                return;
            }

            if (!file.name.toLowerCase().endsWith('.csv')) {
                showError(errorDiv, 'Please select a CSV file.');
                hidePreview();
                return;
            }

            const reader = new FileReader();
            reader.onload = function(e) {
                try {
                    parseCSV(e.target.result);
                    errorDiv.style.display = 'none';
                } catch (error) {
                    showError(errorDiv, 'Error reading CSV file: ' + error.message);
                    hidePreview();
                }
            };
            reader.readAsText(file);
        }

        function parseCSV(csvText) {
            const lines = csvText.split('\\n').filter(line => line.trim());
            
            if (lines.length < 2) {
                throw new Error('CSV must have at least a header row and one data row.');
            }

            // Parse headers with proper CSV handling
            csvHeaders = parseCSVLine(lines[0]);
            
            // Parse data
            csvData = [];
            for (let i = 1; i < lines.length; i++) {
                const values = parseCSVLine(lines[i]);
                if (values.length === csvHeaders.length) {
                    const row = {};
                    csvHeaders.forEach((header, index) => {
                        row[header] = values[index];
                    });
                    csvData.push(row);
                }
            }

            showPreview();
            setupMapping();
        }

        function parseCSVLine(line) {
            const result = [];
            let current = '';
            let inQuotes = false;
            let i = 0;
            
            while (i < line.length) {
                const char = line[i];
                
                if (char === '"') {
                    if (inQuotes && line[i + 1] === '"') {
                        // Escaped quote
                        current += '"';
                        i += 2;
                    } else {
                        // Toggle quote state
                        inQuotes = !inQuotes;
                        i++;
                    }
                } else if (char === ',' && !inQuotes) {
                    // End of field
                    result.push(current.trim());
                    current = '';
                    i++;
                } else {
                    current += char;
                    i++;
                }
            }
            
            // Add the last field
            result.push(current.trim());
            
            return result;
        }

        function showPreview() {
            const previewDiv = document.getElementById('csvPreview');
            const contentDiv = document.getElementById('previewContent');
            
            // Show first 5 rows
            const previewData = csvData.slice(0, 5);
            
            let html = '<table class="preview-table"><thead><tr>';
            csvHeaders.forEach(header => {
                html += `<th>${header}</th>`;
            });
            html += '</tr></thead><tbody>';
            
            previewData.forEach(row => {
                html += '<tr>';
                csvHeaders.forEach(header => {
                    html += `<td>${row[header] || ''}</td>`;
                });
                html += '</tr>';
            });
            html += '</tbody></table>';
            
            contentDiv.innerHTML = html;
            previewDiv.style.display = 'block';
        }

        function setupMapping() {
            const mappingSection = document.getElementById('mappingSection');
            const selects = ['firstNameMapping', 'phoneMapping', 'amountMapping', 'dateOfServiceMapping'];
            
            selects.forEach(selectId => {
                const select = document.getElementById(selectId);
                select.innerHTML = '<option value="">-- Select Column --</option>';
                
                csvHeaders.forEach(header => {
                    const option = document.createElement('option');
                    option.value = header;
                    option.textContent = header;
                    select.appendChild(option);
                });
            });

            mappingSection.style.display = 'block';
            
            // Enable submit button validation
            selects.forEach(selectId => {
                document.getElementById(selectId).addEventListener('change', function() {
                    if (selectId === 'firstNameMapping') {
                        checkForMultiPartNames();
                    }
                    validateForm();
                });
            });
            
            validateForm();
        }

        function checkForMultiPartNames() {
            const firstNameColumn = document.getElementById('firstNameMapping').value;
            const nameChoiceSection = document.getElementById('nameChoiceSection');
            const nameChoiceContainer = document.getElementById('nameChoiceContainer');
            
            // Always clear previous pattern when mapping changes
            namePattern = null;
            allMultiNameRows = [];
            
            if (!firstNameColumn) {
                nameChoiceSection.style.display = 'none';
                return;
            }
            
            // Find rows with multiple names (containing commas)
            csvData.forEach((row, index) => {
                const nameValue = row[firstNameColumn];
                if (nameValue && nameValue.includes(',')) {
                    const nameParts = nameValue.split(',').map(part => part.trim()).filter(part => part);
                    if (nameParts.length > 1) {
                        allMultiNameRows.push({
                            index: index,
                            originalName: nameValue,
                            nameParts: nameParts,
                            row: row
                        });
                    }
                }
            });
            
            if (allMultiNameRows.length > 0) {
                showPatternChoice();
                nameChoiceSection.style.display = 'block';
            } else {
                nameChoiceSection.style.display = 'none';
            }
        }

        function showPatternChoice() {
            const container = document.getElementById('nameChoiceContainer');
            
            if (allMultiNameRows.length === 0) return;
            
            // Show only the first multi-name entry for pattern selection
            const firstEntry = allMultiNameRows[0];
            let html = `
                <div class="name-choice-item">
                    <div class="name-choice-row">
                        Set pattern using: "${firstEntry.originalName}"
                    </div>
                    <div class="name-options">
            `;
            
            firstEntry.nameParts.forEach((namePart, partIndex) => {
                const radioId = `pattern_${partIndex}`;
                const isChecked = partIndex === 0 ? 'checked' : ''; // Default to first name
                html += `
                    <div class="name-option">
                        <input type="radio" id="${radioId}" name="name_pattern" 
                               value="${partIndex}" ${isChecked} 
                               onchange="updateNamePattern(${partIndex})">
                        <label for="${radioId}">${namePart}</label>
                    </div>
                `;
            });
            
            html += `
                    </div>
                </div>
            `;
            
            container.innerHTML = html;
            
            // Set default pattern (first part)
            namePattern = 0;
        }

        function updateNamePattern(patternIndex) {
            namePattern = patternIndex;
            validateForm();
        }

        function validateForm() {
            const firstNameMapping = document.getElementById('firstNameMapping').value;
            const phoneMapping = document.getElementById('phoneMapping').value;
            const amountMapping = document.getElementById('amountMapping').value;
            const dateOfServiceMapping = document.getElementById('dateOfServiceMapping').value;
            const submitBtn = document.getElementById('submitBtn');
            
            const isValid = firstNameMapping && phoneMapping && amountMapping && dateOfServiceMapping && csvData.length > 0;
            submitBtn.disabled = !isValid;
        }

        function hidePreview() {
            document.getElementById('csvPreview').style.display = 'none';
            document.getElementById('mappingSection').style.display = 'none';
            document.getElementById('nameChoiceSection').style.display = 'none';
            document.getElementById('submitBtn').disabled = true;
            csvData = [];
            csvHeaders = [];
            namePattern = null;
            allMultiNameRows = [];
        }

        async function handleSubmit(event) {
            event.preventDefault();
            
            const submitBtn = document.getElementById('submitBtn');
            const successDiv = document.getElementById('successMessage');
            
            submitBtn.disabled = true;
            submitBtn.textContent = 'Submitting...';

            try {
                const formData = {
                    campaignStartDate: document.getElementById('startDate').value,
                    timezone: document.getElementById('timezone').value,
                    numberOfContacts: parseInt(document.getElementById('numContacts').value),
                    contactDays: document.getElementById('contactDays').value,
                    mappedData: csvData.map((row, index) => {
                        const firstNameColumn = document.getElementById('firstNameMapping').value;
                        let firstName = row[firstNameColumn];
                        
                        // Apply pattern to multi-name entries
                        if (namePattern !== null) {
                            const multiNameRow = allMultiNameRows.find(item => item.index === index);
                            if (multiNameRow) {
                                firstName = multiNameRow.nameParts[namePattern] || multiNameRow.nameParts[0];
                            }
                        }
                        
                        return {
                            first_name: firstName,
                            phone_number: row[document.getElementById('phoneMapping').value],
                            amount_owed: row[document.getElementById('amountMapping').value],
                            date_of_service: row[document.getElementById('dateOfServiceMapping').value]
                        };
                    })
                };

                const response = await fetch('https://n8n.srv884802.hstgr.cloud/webhook-test/586c72fa-6f2d-46ab-a4cf-ac9a2375a012', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                if (response.ok) {
                    successDiv.style.display = 'block';
                    document.getElementById('campaignForm').reset();
                    hidePreview();
                    setTimeout(() => {
                        successDiv.style.display = 'none';
                    }, 5000);
                } else {
                    throw new Error(`Server responded with status: ${response.status}`);
                }

            } catch (error) {
                alert('Error submitting form: ' + error.message);
                console.error('Submission error:', error);
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Submit Campaign';
            }
        }

        function showError(element, message) {
            element.textContent = message;
            element.style.display = 'block';
        }
    </script>
</body>
</html>'''

@app.route('/')
def index():
    """Main route that serves the debt campaign form and health check endpoint"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health_check():
    """Health check endpoint for deployment monitoring"""
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    import os
    # Configure Flask for development environment 
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)