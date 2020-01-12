#!/usr/env python3

config = {
    "base_url": "http://getbootstrap.com/docs/4.1/examples/",
    "pages": ["album", "checkout", "pricing", "cover"],
}


def get_base_url():
    return config["base_url"]


def get_page_url(name):
    page = ""

    if name in config["pages"]:
        page = name

    return f"{get_base_url()}{page}"


if __name__ == "__main__":
    print(get_page_url("album"))

    print(get_page_url("checkout"))

    print(get_page_url("checknot"))

    print(get_page_url("pricing"))

    print(get_page_url("cover"))
