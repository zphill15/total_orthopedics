# Debt Leads Campaign Management

## Overview

This is a complete single-page web application for debt leads campaign management. The application fetches debt leads from an external webhook API and displays them in a professional campaign management interface with filtering, search, and responsive design. Built with vanilla HTML, CSS, and JavaScript with security best practices implemented.

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes (September 16, 2025)

- **Updated dashboard metrics integration** - Added new Flask proxy endpoint `/api/dashboard-data` to fetch metrics from webhook https://n8n.srv884802.hstgr.cloud/webhook/nd_load_dashboard_data
- **Replaced old metrics** - Removed "New Leads", "Contacted", and "Qualified" metrics; added new metrics: Total Patients In Collection, Total Outstanding Debt In Collection, Collected Debt, Number of Debts Cleared
- **Added robust error handling** - Implemented fallback data for dashboard metrics when webhook is unavailable
- **Enhanced currency formatting** - Added proper formatting for monetary values using toLocaleString
- **Fixed CORS issues** - Created Flask proxy to avoid browser CORS restrictions when calling external webhooks

## Previous Changes (September 15, 2025)

- Created complete single-page HTML application with embedded CSS and JavaScript
- Implemented secure API integration with webhook endpoint https://n8n.srv884802.hstgr.cloud/webhook/nd_load_debt_leads
- Added comprehensive campaign management interface with lead display, filtering, and search
- Fixed CORS preflight issues by optimizing HTTP headers
- Eliminated XSS vulnerabilities by implementing secure DOM manipulation
- **Converted to Flask application for better deployment and publishing capabilities**
- **Configured production-ready deployment with Gunicorn WSGI server**
- **Added Flask health check endpoint for deployment monitoring**

## Project Architecture

### Application Architecture
- **Framework**: Flask web application serving HTML templates
- **Frontend**: HTML template with embedded CSS and JavaScript
- **Design Pattern**: Single-page application with responsive design
- **Security**: XSS-protected DOM manipulation using createElement/textContent
- **API Integration**: Secure GET requests to webhook with proper CORS handling

### Features Implemented
- **Lead Display**: Dynamic table with all lead data from webhook
- **Search & Filter**: Full-text search across all lead fields
- **Statistics Dashboard**: Real-time stats showing Total Patients In Collection, Total Outstanding Debt In Collection, Collected Debt, and Number of Debts Cleared
- **Responsive Design**: Mobile and desktop optimized interface
- **Status Management**: Color-coded lead status badges
- **Data Formatting**: Automatic formatting for currency, dates, phone numbers, and emails
- **Error Handling**: Comprehensive error states and loading indicators

### Security Features
- **DOM Security**: All user data rendered via createElement/textContent to prevent XSS
- **Email Validation**: Regex validation for email fields before creating mailto links
- **CORS Optimized**: GET requests without preflight-triggering headers
- **Input Sanitization**: Safe handling of all external webhook data

### Technical Specifications
- **File Structure**: Flask app (app.py) serving HTML template (templates/index.html)
- **Dependencies**: Flask, Gunicorn for production deployment
- **Development**: Flask development server on port 5000
- **Production**: Gunicorn WSGI server with dynamic PORT binding
- **Deployment**: Autoscale configuration with health checks
- **Webhook Integration**: GET requests to n8n webhook endpoint
- **Browser Support**: Modern browsers with ES6+ support

## Dependencies

- **Python Framework**: Flask for web application structure
- **Production Server**: Gunicorn WSGI server for deployment
- **API Endpoints**: 
  - Lead Data: n8n webhook at https://n8n.srv884802.hstgr.cloud/webhook/nd_load_debt_leads
  - Dashboard Metrics: Flask proxy `/api/dashboard-data` connecting to https://n8n.srv884802.hstgr.cloud/webhook/nd_load_dashboard_data
- **Frontend**: Vanilla HTML/CSS/JavaScript (no external frontend libraries)