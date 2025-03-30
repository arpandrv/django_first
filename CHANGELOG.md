# Changelog

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