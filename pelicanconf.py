from pheasant.plugins import pelican

AUTHOR = "daizutabi"
SITENAME = "大豆旅"
SITEURL = "https://blog.daizutabi.net"

PATH = "content"
RELATIVE_URLS = False

DEFAULT_PAGINATION = 10

TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "Ja"
DATE_FORMATS = {"ja": "%Y年%m月%d日 (%a)"}

PATH_METADATA = r"(?P<category>.+?)/.*"
FILENAME_METADATA = r"(?P<date>\d{8}).(?P<title>.+)"

THEME = 'themes/Flex'

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/index.html"
PAGE_URL = "page/{slug}/"
PAGE_SAVE_AS = "page/{slug}/index.html"
CATEGORY_URL = "category/{name}/"
CATEGORY_SAVE_AS = "category/{name}/index.html"

STATIC_PATHS = ["images", "extra"]

DELETE_OUTPUT_DIRECTORY = True

IGNORE_FILES = [".#*", "__pycache__"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FAVICON = "favicon.ico"
FAVICON_TYPE = "image/vnd.microsoft.icon"
EXTRA_PATH_METADATA = {"extra/" + FAVICON: {"path": FAVICON}}

PLUGINS = [pelican]
