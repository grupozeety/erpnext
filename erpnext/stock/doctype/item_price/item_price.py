# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _

class ItemPriceDuplicateItem(frappe.ValidationError): pass

from frappe.model.document import Document

class ItemPrice(Document):
	def validate(self):
		self.validate_item()
		self.validate_price_list()
		self.check_duplicate_item()
		self.update_price_list_details()
		self.update_item_details()

	def validate_item(self):
		if not frappe.db.exists("Item", self.item_code):
			throw(_("Item {0} not found").format(self.item_code))

	def validate_price_list(self):
		enabled = frappe.db.get_value("Price List", self.price_list, "enabled")
		if not enabled:
			throw(_("Price List {0} is disabled").format(self.price_list))

	def check_duplicate_item(self):
		if frappe.db.sql("""select name from `tabItem Price`
			where item_code=%s and price_list=%s and name!=%s""", (self.item_code, self.price_list, self.name)):

			frappe.throw(_("Item {0} appears multiple times in Price List {1}").format(self.item_code, self.price_list),
				ItemPriceDuplicateItem)

	def update_price_list_details(self):
		self.buying, self.selling, self.currency = \
			frappe.db.get_value("Price List", {"name": self.price_list, "enabled": 1},
				["buying", "selling", "currency"])

	def update_item_details(self):
		self.item_name, self.item_description = frappe.db.get_value("Item",
			self.item_code, ["item_name", "description"])
		
	def on_update(self):
		self.sincronizarPrecio()
	
	def sincronizarPrecio(self):		
	
		nombrePyme=frappe.db.get_value("Global Defaults", None, "default_company")
		nombreProducto=	self.item_name
		descripcion=self.description
		
		"""Verificar que efectivamente se tenga una cadena valida en la imagen"""
		if frappe.db.get_value(self.doctype, self.name, "website_image")!= None:
			imagen=frappe.utils.get_url()+frappe.db.get_value(self.doctype, self.name, "website_image")
		else:
			imagen=''
			
		precio=0
		stock=0
		categoria=self.product_category
		segmento=self.product_segment
		subcategoria=self.product_subcategory
		url = 'http://54.164.102.108/joomlaH/Servicios/producto/sincronizarProducto'
		registro = {
				'nombrePyme': nombrePyme, 
				'nombreProducto': nombreProducto,
				'descripcion':descripcion,
				'imagen':imagen,
				'precio':precio, 
				'stock':stock, 
				'categoria':categoria,
				'segmento':segmento,
				'subcategoria':subcategoria
				}		
		r = requests.post(url, params=registro)
		"""frappe.msgprint (r.json())"""	
		frappe.msgprint(r.url)