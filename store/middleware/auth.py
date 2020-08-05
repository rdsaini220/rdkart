from django.shortcuts import render,redirect

# One-time configuration and initialization.
def auth_middleware(get_response):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
    def middleware(request):
        return_url = request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'/login?return_url={return_url}')
        response = get_response(request)        
        return response

    return middleware
