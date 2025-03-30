# Changelog

## [Unreleased] - 2025-03-30

### Added
- Created a data model class (`MangoItem`) for pests and diseases
- Added a unified "Project List" page showing all pests and diseases together
- Implemented detail pages for each pest and disease with their own URLs
- Added regex URL pattern for detail pages
- Created team member information on the About page
- Added CSS for detail and projects pages
- Added filtering functionality to Project List page

### Changed
- Refactored pest and disease templates to use data from context instead of hardcoded HTML
- Updated navigation menu to include the new Project List page
- Modified the context processor to support active highlighting for the Project List
- Replaced JavaScript modal dialogs with proper detail pages
- Updated all "Show Details" links to point to their respective detail pages

## [Unreleased] - 2025-03-27

### Added
- Created a custom context processor (`context_processors.py`) to handle active menu highlighting
- Added URL namespacing with app_name in urls.py
- Created a CLAUDE.md file with project guidelines and commands

### Changed
- Replaced function-based views with class-based views for better code organization
- Updated all templates to use namespaced URLs (e.g., 'mango_app:home' instead of 'home')
- Refactored navigation menu to use context processor variables instead of request.path checks
- Split large CSS file into modular components:
  - base.css: Global styles, header, footer, and common elements
  - home.css: Home page specific styles
  - pests.css: Styles specific to the pests page
  - diseases.css: Styles specific to the diseases page
  - surveillance.css: Styles specific to the surveillance page
  - about.css: Styles specific to the about page

### Fixed
- Improved code organization by following Django best practices
- Enhanced maintainability with proper separation of concerns

## [Initial Release] - 2025

### Added
- Basic Django project structure
- Mango pest and disease information pages
- Surveillance methods information
- Static files with CSS and images
- Basic templates for all pages