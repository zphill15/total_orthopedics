# Overview

This is a Flask web application that serves a comprehensive debt campaign setup form. The application features a single-page interface with CSV file upload, field mapping capabilities, and webhook integration for submitting campaign data to external systems. The form includes all necessary campaign parameters including scheduling, contact management, and data processing workflows.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Single Page Application**: Uses server-side rendering with Flask's `render_template_string` function
- **Embedded Templates**: Complete HTML template with CSS and JavaScript embedded in the Python code
- **CSS Styling**: Modern CSS with gradient backgrounds, glassmorphism effects (backdrop-filter), responsive design, and interactive form elements
- **Form-based Interface**: Comprehensive form with campaign scheduling, contact management, and CSV processing capabilities
- **File Upload**: Interactive CSV file upload with preview functionality
- **Field Mapping Interface**: Dynamic UI for mapping CSV columns to required data fields
- **Real-time Validation**: Form validation with submit button state management

## Backend Architecture
- **Framework**: Flask web framework for Python
- **Template Engine**: Uses Flask's built-in Jinja2 templating via `render_template_string`
- **Single Route Application**: Single root endpoint serving the complete form interface
- **No Database Layer**: Stateless application with data processed client-side and forwarded to webhook
- **Webhook Integration**: Client-side JavaScript handles form submission to external webhook endpoint
- **Development Server**: Flask development server configured for Replit environment (host=0.0.0.0, port=5000)

## Design Patterns
- **Monolithic Structure**: All code contained in a single `app.py` file
- **Template Embedding**: HTML template stored as Python string constant rather than separate template files
- **Static Styling**: CSS embedded directly in HTML template

## Development Approach
- **Minimal Setup**: Simple Flask application with no external dependencies beyond Flask
- **Prototype Architecture**: Structure suggests early development or proof-of-concept phase
- **Self-contained**: All frontend code embedded within the Python application

# External Dependencies

## Core Framework
- **Flask**: Python web framework for serving the application and handling HTTP requests

## Frontend Technologies
- **HTML5**: Standard markup for the form interface
- **CSS3**: Modern styling including gradients, backdrop filters, and flexbox
- **Vanilla JavaScript**: No external JavaScript frameworks detected

## Missing Dependencies
- **No Database**: Stateless application with no data persistence requirements
- **Client-side Form Processing**: JavaScript handles CSV parsing, preview generation, and field mapping
- **Webhook Integration**: Form data submitted to external webhook at https://n8n.srv884802.hstgr.cloud/webhook/debt_form_upload
- **No Authentication**: Public form interface with no user authentication requirements

The application has minimal external dependencies while providing comprehensive form functionality including file processing, data validation, and external system integration through webhooks.