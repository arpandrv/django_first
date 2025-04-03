Mango Pest and Disease Surveillance Website
Revised Comprehensive Design Brief
This document outlines the modified design and functionality of the Mango Pest and Disease Surveillance Website, focusing specifically on the informational components for Objective 1 of the project.
1. System Overview
The website provides an informational platform about mango pests and diseases, designed to educate growers about common threats to their crops. This represents the first phase (Objective 1) of the larger project, focusing on delivering static educational content rather than interactive surveillance tools.
The system is built with Django, utilizing HTML5 for markup, CSS for styling, and Python for the backend data model. All pest/disease information is stored in Python objects and rendered dynamically through Django templates.
2. Core Pages and Features
2.1 Home Page

Introduction section:

Welcome message explaining the purpose of the website
Overview of the importance of pest surveillance for mango cultivation
Brief explanation of the website's organization and content
Call-to-action directing users to the pest/disease list


Visual elements:

Hero image of healthy mango trees/fruits
Clean, readable typography suited for the target audience



2.2 Project List Page (Pest/Disease Catalog)

List of all seven mango pests/diseases:

Each item displayed in a consistent card/grid format
For each pest/disease:

Name of the pest/disease
Brief description (1-2 sentences)
Representative image
Link to detailed information page




Organization options:

Grouping by type (insect pests, fungal diseases, etc.)
Consistent styling to differentiate between categories



2.3 Project Details Page (Individual Pest/Disease)

Comprehensive information about the selected pest/disease:

Full name (scientific and common)
Detailed description
Visual identification characteristics
Symptoms on different plant parts
Seasonal patterns and lifecycle information
Affected plant parts
Severity and economic impact
High-quality images showing the pest/disease and symptoms
References or further reading


Navigation elements:

Previous/next pest/disease links
Return to catalog link



2.4 About Page

Team information:

List of all team members with full names and student IDs
Project background and acknowledgments


Project context:

Brief explanation of the assignment objectives
Future development plans (mention of upcoming interactive features)



3. Technical Implementation
3.1 URL Structure

Home: /
Pest/Disease List: /pests/
Pest/Disease Detail: /pests/<pest_id>/ (using a single URL pattern with regex)
About: /about/

3.2 Data Model

Custom Python class defined in a separate file (e.g., models.py or pest_model.py)
Class attributes for all pest/disease properties:

ID/slug (for URL routing)
Name
Scientific name
Category/type
Description (brief)
Detailed information
Affected plant parts
Symptoms
Lifecycle
Severity
Image paths/references
Additional properties as needed


List of seven class instances representing different pests/diseases

3.3 View Implementation

Home view: Simple template rendering
List view: Passes the complete list of pest objects to the template
Detail view:

Extracts the pest ID from the URL
Finds the matching pest object
Passes it to the template for rendering


About view: Simple template rendering

3.4 Templates

Base template for consistent layout across all pages
Home template extending from base
List template for displaying all pests
Detail template for individual pest information
About template for team information

4. Navigation

Consistent navbar present on all pages with links to:

Home
Pest/Disease List
About


Breadcrumb navigation showing current location in site hierarchy
Previous/next links on detail pages for browsing through pests/diseases
Return to list link on detail pages

5. HTML5 Structure and Formatting
5.1 Semantic Markup

Proper use of semantic HTML5 elements:

<header>, <footer>, <nav>, <main>, <article>, <section>
Appropriate heading hierarchy (<h1> through <h6>)
Lists (<ul>, <ol>) for appropriate content



5.2 Content Formatting

Tables for structured data presentation (e.g., lifecycle stages)
Text formatting for readability (paragraphs, emphasis, strong)
Image inclusion with proper alt text
Semantic use of HTML for content organization

6. Content Requirements
6.1 Pest/Disease Selection
Seven different mango pests/diseases, such as:

Anthracnose
Powdery Mildew
Mango Seed Weevil
Mango Scale
Bacterial Black Spot
Mango Malformation
Mango Fruit Fly

6.2 Information Requirements
For each pest/disease, the following information should be included:

Common name(s)
Scientific name
Type of organism (fungus, insect, bacteria, etc.)
Description of appearance
Symptoms on the plant
Plant parts affected
Lifecycle information
Seasonal patterns
Detection methods
Economic impact/severity

6.3 Visual Elements

High-quality images for each pest/disease
Diagrams showing lifecycle where appropriate
Images of symptoms on different plant parts

7. Implementation Plan
7.1 Setup Phase

Create Django project
Define URL patterns with regex for detail pages
Create custom Python class for the data model
Implement base templates and styling

7.2 Content Development

Research and compile information on seven mango pests/diseases
Create class instances for each pest/disease
Gather appropriate images for each

7.3 View and Template Creation

Implement view functions for all pages
Create HTML templates with appropriate formatting
Integrate navigation between pages

7.4 Testing and Refinement

Verify all links work correctly
Ensure consistent styling across pages
Test URL patterns for all pest/disease detail pages

8. Summary
This design brief outlines the implementation of a Django-based informational website about mango pests and diseases. The site consists of four main pages (Home, Pest/Disease List, Pest/Disease Details, and About), with content dynamically generated from a custom Python class. The implementation focuses on delivering educational content about seven mango pests/diseases through a consistent, well-structured website that follows HTML5 standards and best practices.
This website represents the completion of Objective 1 from the Project Brief, focusing specifically on the static informational component rather than the interactive surveillance tools that would be developed in Objective 2.