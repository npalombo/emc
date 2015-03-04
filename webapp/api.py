__author__ = 'nick'

import json

from django.shortcuts import HttpResponse, Http404
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_GET

from fibonacci import fib


@require_GET
def fib_api(request, n):
    try:
        n = int(n)
    except:
        return HttpResponseBadRequest('Argument must be numeric')

    try:
        if n > 0:
            seq = fib(n)
            result = json.dumps(seq)
            return HttpResponse(result, content_type='application/json')
        else:
            return HttpResponseBadRequest('Argument must be at least 1')
    except Exception, e:
        raise Http404(e)
