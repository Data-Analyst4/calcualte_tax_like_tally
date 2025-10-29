# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "calculate_tax_like_tally"
app_title = "Calculate Tax Like Tally"
app_publisher = "K95 FOODS PVT LTD"
app_description = "ERPNext Sales Invoice tax calculation matching Tally Prime GST logic"
app_icon = "octicon octicon-calculator"
app_color = "green"
app_email = "contact@k95foods.com"
app_license = "MIT"

# Override Sales Invoice controller to apply Tally tax calculation
override_doctype_class = {
	"Sales Invoice": "calculate_tax_like_tally.overrides.sales_invoice.TallyTaxSalesInvoice"
}
