def active_menu(request):
    """
    A context processor to add active menu information to templates.
    This allows us to highlight the current active menu item.
    """
    path = request.path
    
    active_section = {
        'is_home': path == '/' or path == '/home/',
        'is_projects': '/projects/' in path,
        'is_pests': '/pests/' in path,
        'is_diseases': '/diseases/' in path,
        'is_surveillance': '/surveillance/' in path,
        'is_about': '/about/' in path,
    }
    
    return {
        'active_section': active_section
    }