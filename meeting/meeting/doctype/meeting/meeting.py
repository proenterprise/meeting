# -*- coding: utf-8 -*-
# Copyright (c) 2019, Adam Dawoodjee and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Meeting(Document):

	def validate(self):
		found = []
		for attendee in self.attendees:
			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee.attendee)

			if attendee.attendee in found:
				frappe.throw(_("{0} has already been added as an attendee").format(attendee.full_name))

			found.append(attendee.attendee)

@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User", attendee)
	return " ".join(filter(None, [user.first_name, user.last_name]))