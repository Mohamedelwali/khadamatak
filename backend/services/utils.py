def filter_services(queryset, params):
    """
    Apply optional filters to the services queryset based on query parameters.
    Supported filters:
    - category: filter by category slug
    - city: filter by city name (case-insensitive)
    """
    category = params.get("category")
    city = params.get("city")

    if category:
        queryset = queryset.filter(category__slug=category)
    if city:
        queryset = queryset.filter(city__icontains=city)

    return queryset
