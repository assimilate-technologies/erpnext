import frappe
from frappe.tests.utils import FrappeTestCase

from erpnext.accounts.party import get_default_price_list


class PartyTestCase(FrappeTestCase):
	def test_get_default_price_list_should_return_none_for_invalid_group(self):
		customer = frappe.get_doc(
			{"doctype": "Customer", "customer_name": "test customer", "customer_group": "Individual"}
		).insert(ignore_permissions=True, ignore_mandatory=True)
		customer.save()
		price_list = get_default_price_list(customer)
		assert price_list is None
