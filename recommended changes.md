These are the recommneded changes for the project based on the new requirements. Make these changes:

The current project follows some aspects but needs significant changes to comply with the assignment specifications:

What the Project Currently Follows:

✅ Django-based website: The project is built using Django.
✅ Multiple pages: Includes home, pests, diseases, surveillance, and about pages.
✅ Sufficient content: Has more than 7 pests/diseases in total (5 pests + 5 diseases).
✅ Navigation: Has consistent navigation and hyperlinks between pages.
✅ HTML5 with formatting: Uses proper HTML5 syntax with headers, formatting, etc.

What Needs to Be Changed:

❌ Data Model Structure:

Need to create a Python class in a separate file to define the data model for pests/diseases
Currently all pest/disease information is hardcoded in HTML templates


❌ Django Context Usage:

Need to instantiate the class for each pest/disease and store in a list
Pass this list to Django's Context rather than hardcoding in templates
Current approach doesn't use Context for rendering dynamic data


❌ Detail Pages Implementation:

Currently using JavaScript modals for details, which doesn't satisfy requirement
Need to create actual detail pages with their own URLs
Need to implement a single URL pattern with regex for all detail pages


❌ Project List Organization:

Currently has separate pages for pests and diseases
Should have a single "Project List" page showing all pests/diseases together


❌ About Page Content:

Current about page doesn't include team member information
Need to add team members' names and student IDs