RELATIVE_URLS = True


AUTHOR = 'daizutabi'
SITENAME = '大豆旅'
SITESUBTITLE = 'Sub-title that goes underneath site name in jumbotron.'
SITEURL = 'https://daizutabi.github.io'
OUTPUT_PATH = '../daizutabi.github.io/'

SLUGIFY_SOURCE = 'title'

TIMEZONE = 'Asia/Tokyo'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ja': '%Y年%m月%d日 (%a)',
}
DEFAULT_LANG = 'ja'

DEFAULT_PAGINATION = 5


ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'page/{slug}/'
PAGE_SAVE_AS = 'page/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = '../voidy-bootstrap/'

# Voidy Bootstrap
STYLESHEETS = (
    'custom/custom.css',
    # 'voidybootstrap.css',
    'addition/pygment.css',
    # 'addition/style.css',
    # 'addition/image.css',
    # 'addition/admonition.css',
)

CUSTOM_SITE_HEADERS = ['custom/jumbotron.jinja2']
CUSTOM_ARTICLE_HEADERS = ['custom/article_header.jinja2']
CUSTOM_INDEX_ARTICLE_HEADERS = ['custom/index_article_header.jinja2']

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
