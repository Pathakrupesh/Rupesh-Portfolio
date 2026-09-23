from datetime import datetime
from .models import SiteSettings


def portfolio_globals(request):
    """
    Context processor providing site settings and the current year to all templates.
    """
    try:
        settings = SiteSettings.get_settings()
    except Exception:
        settings = None

    return {
        'site_settings': settings,
        'current_year': datetime.now().year,
    }
