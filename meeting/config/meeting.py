from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("Document"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Meeting App",
                    "label": _("Meeting"),
                },
                {
                    "type": "doctype",
                    "name": "Meeting",
                    "label": _("Meeting"),
                }
            ]
        }
    ]
