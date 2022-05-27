def hitcount_middleware(get_response):
    def middleware(request):
        response = get_response(request)

        # Get the URL from the `request` parameter and save it
        # in a Hitcount model.

        return response

    return middleware
