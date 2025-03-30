# Django Mango App Development Guide

## Commands
- Run server: `python manage.py runserver`
- Run tests: `python manage.py test`
- Run single test: `python manage.py test mango_app.tests.TestClassName.test_method_name`
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Lint: `pylint mango_app`

## Code Style Guidelines
- **Imports**: Group imports (stdlib, Django, 3rd party, local)
- **Formatting**: Four spaces for indentation, max line length 88 characters
- **Naming**: Snake case for variables/functions, CamelCase for classes
- **Templates**: Keep logic out of templates, use template inheritance
- **Error handling**: Use specific exceptions, log errors appropriately
- **Django conventions**: Follow official Django style guide for views, models, etc.
- **Static files**: Place in app-specific static directory with proper namespacing