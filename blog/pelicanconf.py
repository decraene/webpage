AUTHOR = 'Mathieu De Craene'
SITENAME = "Mathieu's blog"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

SUMMARY_MAX_LENGTH = 50 # no summary unless specified in the header

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ["images", "extra/robots.txt", "extra/favicon.ico"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"}
}

# Social links
SOCIAL = (
    ("Instagram", "https://www.instagram.com/mathieudecraene/"),
    ("Mastodon", "https://musicians.today/@decraene"),
    ("LinkedIn", "https://fr.linkedin.com/in/decraene"),
    ("Bluesky", "https://bsky.app/profile/decraene.bsky.social"),
    ("Soundcloud", "https://soundcloud.com/mathieu-de-craene")
)

ARTICLE_ORDER_BY = 'basename'
DEFAULT_PAGINATION = 100

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
