import re

import jinja2
from staticjinja import Site

def quoted(s):
    l = re.findall('\'([^\']*)\'', str(s))
    if l:
        return l[0]
    return None




if __name__ == "__main__":
    site = Site.make_site(
        mergecontexts=True,
        filters={
            "quoted": quoted,
        }
    )

    site.render(use_reloader=True)
