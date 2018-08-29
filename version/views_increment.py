from django.shortcuts import HttpResponse

from .models import Config, Version
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


@csrf_exempt
def increment_view(request):
    if request.method == 'POST':
        try:
            d = json.loads(request.body)
        except:
            return HttpResponse(status=404)
            # {"key": "web", "version": "'$v'"}
        if 'key' in d and 'secret' in d and 'revision' in d:
            config = Config.objects.filter(key=d['key'], secret=d['secret']).first()
            if config is None:
                return HttpResponse(status=404)
        else:
            return HttpResponse(status=404)
        version = config.version_set.first()
        date = timezone.now().date()
        if version:
            p = version.value.split('.')
            if len(p) != 3:
                return HttpResponse(status=404)
            if date.strftime("%Y.%m") == '%s.%s' % (p[0], p[1]):
                _ = int(p[2]) + 1
                version = Version.objects.create(
                    config=config,
                    revision=d['revision'][:255],
                    value='%s.%s' % (date.strftime("%Y.%m"), _)
                )
            else:
                version = Version.objects.create(
                    config=config,
                    revision=d['revision'][:255],
                    value='%s.1' % (date.strftime("%Y.%m"))
                )
        else:
            version = Version.objects.create(
                config=config,
                revision=d['revision'][:255],
                value='%s.1' % (date.strftime("%Y.%m"))
            )
        if config.key.find('develop') == -1:
            _version = version.value
        else:
            _version = 'Develop~%s' % version.value
        return HttpResponse("let version = '%s'\nmodule.exports = version\n" % _version)
    else:
        return HttpResponse(status=404)
