# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class DiabetesForm(http.Controller):
	@http.route('/website/form/', type='http', auth='public')
	def diabetes_form(self, **post):
		contact_name = request.httprequest.form.get('contact_name')
		middle_name = request.httprequest.form.get('x_studio_nombre_2')
		last_name = request.httprequest.form.get('x_studio_apellido_1')
		contact_name = contact_name + " " + last_name
		second_surname = request.httprequest.form.get('x_studio_apellido_2')
		identification_number = request.httprequest.form.get('x_studio_identificacin_miembro')
		sex = request.httprequest.form.get('sex')
		email_from = request.httprequest.form.get('email_from')
		country_of_residence = request.httprequest.form.get('country_id')
		country_id = request.env['res.country'].search([('name','=','country_of_residence')])
		country_id = country_id.id
		phone = request.httprequest.form.get('phone')
		phone_or_cell_phone = request.httprequest.form.get('phone')
		type_diabetes = request.httprequest.form.get('x_studio_many2one_field_RVWpx')
		current_rule = request.httprequest.form.get('2_detail_hidden')
		type_2_diabetes = request.httprequest.form.get('1_detail_hidden')
		specifies = request.httprequest.form.get('x_studio_rol')
		like_volunteer_or_leader = 'yes' if request.httprequest.form.get('yes-no') == 'on' else 'no'

		first_name_2 = request.httprequest.form.get('x_studio_pac_nombre_1')
		middle_name_2 = request.httprequest.form.get('x_studio_pac_nombre_2')
		first_surname_2 = request.httprequest.form.get('x_studio_pac_apellido_1')
		second_surname_2 = request.httprequest.form.get('x_studio_pac_apellido_2')
		country_of_residence_2 = request.httprequest.form.get('x_studio_pas_residencia_paciente')
		address_2 = request.httprequest.form.get('x_studio_direccin')
		city_2 = request.httprequest.form.get('x_studio_ciudad')
		province = request.httprequest.form.get('Provincia')
		identification_number_2 = request.httprequest.form.get('x_studio_identificacin_paciente')
		diabetes_treat_condition = False if request.httprequest.form.get('x_studio_many2one_field_s8eOq') == '-' else request.httprequest.form.get('x_studio_many2one_field_s8eOq')
		speci_diabetes_treat_condition = request.httprequest.form.get('x_studio_detalle')
		dob_2 = request.httprequest.form.get('x_studio_fecha_de_nacimiento') if request.httprequest.form.get('x_studio_fecha_de_nacimiento') else False
		date_of_diagnosis = request.httprequest.form.get('x_studio_fecha_de_diagnostico') if request.httprequest.form.get('x_studio_fecha_de_diagnostico') else False
		name_of_doc_treat_diabetes = request.httprequest.form.get('x_studio_nombre_del_medico_tratante_de_la_diabetes')
		other_medico = request.httprequest.form.get('other_medico')

		insulin_use = request.httprequest.form.get('x_studio_rgimen_de_insulinas_accin_intermedia')
		other_insulin_use = request.httprequest.form.get('x_studio_detalle_insulina_accin_intermedia')
		rapid_insulin = request.httprequest.form.get('x_studio_rgimen_de_insulinas_regular_r_cristalina')
		other_rapid_insulin = request.httprequest.form.get('x_studio_detalle_r_cristalina')
		method_of_insulin_1 = request.httprequest.form.get('x_studio_many2many_field_YyKw8')
		# method_of_insulin_2 = request.httprequest.form.get('x_studio_many2many_field_YyKw8q')
		blood_glucose_monitoring = request.httprequest.form.get('x_studio_many2many_field_CglRU')
		spe_blood_glucose_monitoring = request.httprequest.form.get('x_studio_describa')

		agreement_check = True if request.httprequest.form.get('x_studio_acepta_poltica_de_privacidad_de_diabeteslatam') == 'Yes' else False 
		crm_lead_id = request.env['crm.lead']
		crm_lead_id = crm_lead_id.sudo().create({
			'name': 'Inscripción Fundación DiabetesLATAM',
			'contact_name': contact_name,
			'middle_name': middle_name,
			'second_surname': second_surname,
			'identification_number': identification_number,
			'sex': sex,
			'email_from': email_from,
			'country_of_residence': country_of_residence,
			'country_id': country_id,
			'phone': phone,
			'phone_or_cell_phone': phone_or_cell_phone,
			'type_diabetes': type_diabetes,
			'current_rule': current_rule,
			'type_2_diabetes': type_2_diabetes,
			'specifies': specifies,
			'like_volunteer_or_leader': like_volunteer_or_leader,

			'first_name_2': first_name_2,
			'middle_name_2': middle_name_2,
			'first_surname_2': first_surname_2,
			'second_surname_2': second_surname_2,
			'country_of_residence_2': country_of_residence_2,
			'address_2': address_2,
			'city_2': city_2,
			'province': province,
			'identification_number_2': identification_number_2,
			'diabetes_treat_condition': diabetes_treat_condition,
			'speci_diabetes_treat_condition': speci_diabetes_treat_condition,
			'dob_2': dob_2,
			'date_of_diagnosis': date_of_diagnosis,
			'name_of_doc_treat_diabetes': name_of_doc_treat_diabetes,

			'insulin_use': insulin_use,
			'other_insulin_use': other_insulin_use,
			'rapid_insulin': rapid_insulin,
			'other_rapid_insulin': other_rapid_insulin,
			'method_of_insulin_1': method_of_insulin_1,
			# 'method_of_insulin_2': method_of_insulin_2,
			'blood_glucose_monitoring': blood_glucose_monitoring,
			'spe_blood_glucose_monitoring': spe_blood_glucose_monitoring,

			'agreement_check': agreement_check,
		})

		return request.redirect('/thank-you')

	@http.route('/thank-you', type='http', auth='public', website=True)
	def thank_you(self, **post):
		return request.render('studio_customization.thank_you')