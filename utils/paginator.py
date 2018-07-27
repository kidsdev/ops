from django.core.paginator import Paginator


def listing(request, contact_list):
    # Ref: https://docs.djangoproject.com/en/2.0/topics/pagination/#using-paginator-in-a-view
    paginator = Paginator(contact_list, 50)

    page = request.GET.get('page')
    return paginator.get_page(page)


def get_q(q_dict):
    q = ''
    for key, value in q_dict.items():
        if value:
            q += '&%s=%s' % (key, value)
    return q if len(q) > 0 else None
