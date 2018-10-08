import json

from django.shortcuts import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Config, Version


@csrf_exempt
def last_view(request):
    if request.method == 'POST':
        try:
            d = json.loads(request.body)
        except:
            return HttpResponse(status=404)
        if 'key' in d and 'secret' in d and 'revision' in d:
            config = Config.objects.filter(key=d['key'], secret=d['secret']).first()
            if config is None:
                return HttpResponse(status=404)
        else:
            return HttpResponse(status=404)
        version = config.version_set.first()
        if version is None:
            date = timezone.now().date()
            version = Version.objects.create(
                config=config,
                revision=d['revision'][:255],
                value='%s.1' % (date.strftime("%Y.%m"))
            )
        if config.key.find('develop') == -1:
            _version = version.value
        else:
            _version = 'Develop~%s' % version.value
        format = request.GET.get('format', None)
        if format == 'plain':
            return HttpResponse("%s\n" % _version)
        else:
            return HttpResponse("let version = '%s'\nmodule.exports = version\n" % _version)
    else:
        return HttpResponse(status=404)
