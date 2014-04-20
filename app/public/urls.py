import sys
import os
import web

route = {
    "default": ("app/public/publicMain", "Home.response"),
    "/login": ("app/public/publicMain", "Login.response"),
    "/profile/?$": ("app/public/profileMain", "Profile.response"),
    "/profile/domainstat": ("app/public/profileMain", "Profile.responseStat"),
    "/profile/domainstatdomain": ("app/public/profileMain", "Profile.responseStatDomain"),
    "/profile/domainauthadd": ("app/public/profileMain", "Profile.domainAuthAdd"),
    "/profile/domainauthdel": ("app/public/profileMain", "Profile.domainAuthDel"),
    "/util": ("app/public/publicMain", "Util.response"),
    "^/plot": ("app/public/plot", "Plot.response"),
    "^/online": ("app/public/publicMain", "Online.online"),
}

def urls(environ):
    return web.execute(environ, route)