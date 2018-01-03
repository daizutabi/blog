AUTHOR = 'daizutabi'
SITENAME = '大豆旅'
SITESUBTITLE = 'daizutabiのブログです．'
SITEURL = 'https://blog.daizutabi.net'

RELATIVE_URLS = False

DEFAULT_PAGINATION = 5

TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'
DATE_FORMATS = {
    'ja': '%Y年%m月%d日 (%a)',
}

PATH_METADATA = r'(?P<category>.+?)/.*'
FILENAME_METADATA = r'(?P<date>\d{8}).(?P<title>.+)'
# USE_FOLDER_AS_CATEGORY = False
# FILENAME_METADATA = r'(?P<date>.+?)_(?P<title>.+)'
# SLUGIFY_SOURCE = 'title'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'
PAGE_URL = 'page/{slug}/'
PAGE_SAVE_AS = 'page/{slug}/index.html'
CATEGORY_URL = 'category/{name}/'
CATEGORY_SAVE_AS = 'category/{name}/index.html'

STATIC_PATHS = ['images']

THEME = 'voidy-bootstrap/'
STYLESHEETS = (
    'custom/custom.css',
    # 'voidybootstrap.css',
    'pygment.css',
    # 'addition/style.css',
    # 'addition/image.css',
    # 'addition/admonition.css',
)

STYLESHEET_URLS = (
    'https://fonts.googleapis.com/earlyaccess/sawarabigothic.css',
)

CUSTOM_SITE_HEADERS = ['custom/jumbotron.jinja2']
CUSTOM_ARTICLE_HEADERS = ['custom/article_header.jinja2']
CUSTOM_INDEX_ARTICLE_HEADERS = ['custom/index_article_header.jinja2']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# PLUGIN_PATHS = ['../pelican-plugins']
# PLUGINS = []
