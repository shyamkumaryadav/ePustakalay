'''
doc: `https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/`
'''
from django import template
from django.urls import NoReverseMatch, reverse
from django.utils.html import escape, format_html, smart_urlquote
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def optional_info(request, user):
    """
    Include a logout snippet if REST framework's logout view is in the URLconf.
    """
    try:
        logout_url = reverse('rest_framework:logout')
        update = reverse('user-update-user', kwargs={'pk': user.id})
        setpassword = reverse('user-set-password', kwargs={'pk': user.id})
    except NoReverseMatch:
        snippet = format_html('<li class="navbar-text">{user}</li>', user=escape(user))
        return mark_safe(snippet)

    snippet = """<li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
            {user}
            <b class="caret"></b>
        </a>
        <ul class="dropdown-menu">
            <li><a href='{update}'>Update</a></li>
            <li><a href='{setpassword}'>Change Password</a></li>
            <li><a href='{href}'>Log out</a></li>
        </ul>
    </li>"""
    snippet = format_html(snippet, update=update, setpassword=setpassword, user=escape(user), href=logout_url)

    return mark_safe(snippet)


def a_tag(request, path, title):
    'return li el'
    return f'<li class="disabled"><a>{title}</a></li>' if request.path == path else f"<li><a href={path}>{title}</a></li>"

@register.simple_tag
def all_router(request):
    '''
    Displays all of the url routes for the project.
    '''
    try:
        user = reverse('user-list')
        userTitle = user[1:-1].replace('-', ' ').title()
        issue_list = reverse('issue-list')
        issue_listTitle = issue_list[1:-1].replace('-', ' ').title()
        bookpublish_list = reverse('bookpublish-list')
        bookpublish_listTitle = bookpublish_list[1:-1].replace('-', ' ').title()
        genre_list = reverse('genre-list')
        genre_listTitle = genre_list[1:-1].replace('-', ' ').title()
        bookauthor_list = reverse('bookauthor-list')
        bookauthor_listTitle = bookauthor_list[1:-1].replace('-', ' ').title()
        book_list = reverse('book-list')
        book_listTitle = book_list[1:-1].replace('-', ' ').title()

        snippet = """<li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                Routes
                <b class="caret"></b>
            </a>
            <ul class="dropdown-menu">
                {user}
                {book_list}
                {bookpublish_list}
                {genre_list}
                {issue_list}
                {bookauthor_list}
            </ul>
        </li>
        """.format(user=a_tag(request, user, userTitle), 
            book_list=a_tag(request, book_list, book_listTitle), 
            bookpublish_list=a_tag(request, bookpublish_list, bookpublish_listTitle), 
            genre_list=a_tag(request, genre_list, genre_listTitle), 
            issue_list=a_tag(request, issue_list, issue_listTitle), 
            bookauthor_list=a_tag(request, bookauthor_list, bookauthor_listTitle))
    except:
        snippet = ""

    snippet = format_html(snippet)
    return mark_safe(snippet)

@register.simple_tag
def create_user():
    try:
        snippet = '<label>Already have an account <a href={user_create}  data-toggle="tooltip" data-placement="top" title="Sign In">Sign in</a></label>'.format(user_create=reverse('user-create'))
    except:
        snippet = ''
    
    return mark_safe(format_html(snippet))
