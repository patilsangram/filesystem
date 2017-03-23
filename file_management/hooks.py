# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "file_management"
app_title = "File Management"
app_publisher = "Indictrans"
app_description = "App for managing  File"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sangram.p@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/file_management/css/file_management.css"
# app_include_js = "/assets/file_management/js/file_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/file_management/css/file_management.css"
# web_include_js = "/assets/file_management/js/file_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "file_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "file_management.install.before_install"
# after_install = "file_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "file_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"file_management.tasks.all"
# 	],
# 	"daily": [
# 		"file_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"file_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"file_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"file_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "file_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "file_management.event.get_events"
# }

