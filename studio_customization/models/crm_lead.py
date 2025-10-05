# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    SELECTION_COUNTRY = [
        ('afganistan', 'Afganistán'),
        ('albania', 'Albania'),
        ('alemania', 'Alemania'),
        ('andorra', 'Andorra'),
        ('angola', 'Angola'),
        ('anguilla', 'Anguilla'),
        ('antigua_y_barbuda', 'Antigua y Barbuda'),
        ('antartida', 'Antártida'),
        ('arabia_saudita', 'Arabia Saudita'),
        ('argelia', 'Argelia'),
        ('argentina', 'Argentina'),
        ('armenia', 'Armenia'),
        ('aruba', 'Aruba'),
        ('australia', 'Australia'),
        ('austria', 'Austria'),
        ('azerbaiyan', 'Azerbaiyán'),
        ('bahamas', 'Bahamas'),
        ('bahrein', 'Bahréin'),
        ('bangladesh', 'Bangladesh'),
        ('barbados', 'Barbados'),
        ('belice', 'Belice'),
        ('benin', 'Benín'),
        ('bermudas', 'Bermudas'),
        ('bhutan', 'Bhután'),
        ('bielorrusia', 'Bielorrusia'),
        ('birmania', 'Birmania'),
        ('bolivia', 'Bolivia'),
        ('bonaire_san_eustaquio_y_saba', 'Bonaire, San Eustaquio y Saba'),
        ('bosnia_herzegovina', 'Bosnia-Herzegovina'),
        ('botsuana', 'Botsuana'),
        ('brasil', 'Brasil'),
        ('brunei_darussalam', 'Brunei Darussalam'),
        ('bulgaria', 'Bulgaria'),
        ('burkina_faso', 'Burkina Faso'),
        ('burundi', 'Burundi'),
        ('belgica', 'Bélgica'),
        ('cabo_verde', 'Cabo Verde'),
        ('camboya', 'Camboya'),
        ('camerun', 'Camerún'),
        ('canada', 'Canadá'),
        ('chad', 'Chad'),
        ('chile', 'Chile'),
        ('china', 'China'),
        ('chipre', 'Chipre'),
        ('colombia', 'Colombia'),
        ('comores', 'Comores'),
        ('congo', 'Congo'),
        ('corea_del_norte', 'Corea del Norte'),
        ('corea_del_sur', 'Corea del Sur'),
        ('costa_rica', 'Costa Rica'),
        ('costa_de_marfil', 'Costa de Marfil'),
        ('croacia', 'Croacia'),
        ('cuba', 'Cuba'),
        ('curacao', 'Curaçao'),
        ('dinamarca', 'Dinamarca'),
        ('dominica', 'Dominica'),
        ('eeuu_islas_exteriores_menores', 'EE.UU. Islas Exteriores Menores'),
        ('ecuador', 'Ecuador'),
        ('egipto', 'Egipto'),
        ('el_salvador', 'El Salvador'),
        ('emiratos_arabes_unidos', 'Emiratos Árabes Unidos'),
        ('eritrea', 'Eritrea'),
        ('eslovaquia', 'Eslovaquia'),
        ('eslovenia', 'Eslovenia'),
        ('espana', 'España'),
        ('estado_de_palestina', 'Estado de Palestina'),
        ('estados_unidos', 'Estados Unidos'),
        ('estonia', 'Estonia'),
        ('etiopia', 'Etiopía'),
        ('federacion_rusa', 'Federación Rusa'),
        ('fiji', 'Fiji'),
        ('filipinas', 'Filipinas'),
        ('finlandia', 'Finlandia'),
        ('francia', 'Francia'),
        ('gabon', 'Gabón'),
        ('gambia', 'Gambia'),
        ('georgia', 'Georgia'),
        ('ghana', 'Ghana'),
        ('gibraltar', 'Gibraltar'),
        ('granada', 'Granada'),
        ('grecia', 'Grecia'),
        ('groenlandia', 'Groenlandia'),
        ('guadalupe', 'Guadalupe'),
        ('guam', 'Guam'),
        ('guatemala', 'Guatemala'),
        ('guayana', 'Guayana'),
        ('guayana_francesa', 'Guayana Francesa'),
        ('guernsey', 'Guernsey'),
        ('guinea', 'Guinea'),
        ('guinea_ecuatorial', 'Guinea Ecuatorial'),
        ('guinea_bisau', 'Guinea-Bisáu'),
        ('haiti', 'Haití'),
        ('holanda', 'Holanda'),
        ('honduras', 'Honduras'),
        ('hong_kong', 'Hong Kong'),
        ('hungria', 'Hungría'),
        ('india', 'India'),
        ('indonesia', 'Indonesia'),
        ('irak', 'Irak'),
        ('irlanda', 'Irlanda'),
        ('iran', 'Irán'),
        ('isla_bouvet', 'Isla Bouvet'),
        ('isla_norfolk', 'Isla Norfolk'),
        ('isla_de_man', 'Isla de Man'),
        ('isla_de_navidad', 'Isla de Navidad'),
        ('islandia', 'Islandia'),
        ('islas_caiman', 'Islas Caimán'),
        ('islas_cocos_keeling', 'Islas Cocos (Keeling)'),
        ('islas_cook', 'Islas Cook'),
        ('islas_feroe', 'Islas Feroe'),
        ('islas_georgia_del_sur_y_sandwich_del_sur', 'Islas Georgia del sur y Sandwich del sur'),
        ('islas_heard_y_mcdonald', 'Islas Heard y McDonald'),
        ('islas_malvinas', 'Islas Malvinas'),
        ('islas_marianas_del_norte', 'Islas Marianas del Norte'),
        ('islas_marshall', 'Islas Marshall'),
        ('islas_pitcairn', 'Islas Pitcairn'),
        ('islas_salomon', 'Islas Salomón'),
        ('islas_turcas_y_caicos', 'Islas Turcas y Caicos'),
        ('islas_virgenes_britanicas', 'Islas Vírgenes (Británicas)'),
        ('islas_virgenes_eeuu', 'Islas Vírgenes (EE.UU.)'),
        ('islas_aland', 'Islas Åland'),
        ('israel', 'Israel'),
        ('italia', 'Italia'),
        ('jamaica', 'Jamaica'),
        ('japon', 'Japón'),
        ('jersey', 'Jersey'),
        ('jordania', 'Jordania'),
        ('kazajstan', 'Kazajstán'),
        ('kenia', 'Kenia'),
        ('kirguistan', 'Kirguistán'),
        ('kiribati', 'Kiribati'),
        ('kosovo', 'Kosovo'),
        ('kuwait', 'Kuwait'),
        ('laos', 'Laos'),
        ('lesotho', 'Lesotho'),
        ('letonia', 'Letonia'),
        ('liberia', 'Liberia'),
        ('libia', 'Libia'),
        ('liechtenstein', 'Liechtenstein'),
        ('lituania', 'Lituania'),
        ('luxemburgo', 'Luxemburgo'),
        ('libano', 'Líbano'),
        ('macao', 'Macao'),
        ('macedonia_del_norte', 'Macedonia del Norte'),
        ('madagascar', 'Madagascar'),
        ('malasia', 'Malasia'),
        ('malawi', 'Malawi'),
        ('maldivas', 'Maldivas'),
        ('mali', 'Mali'),
        ('malta', 'Malta'),
        ('marruecos', 'Marruecos'),
        ('martinica', 'Martinica'),
        ('mauricio', 'Mauricio'),
        ('mauritania', 'Mauritania'),
        ('mexico', 'México'),
        ('micronesia', 'Micronesia'),
        ('moldavia', 'Moldavia'),
        ('monaco', 'Mónaco'),
        ('mongolia', 'Mongolia'),
        ('mozambique', 'Mozambique'),
        ('namibia', 'Namibia'),
        ('nauru', 'Nauru'),
        ('nepal', 'Nepal'),
        ('nicaragua', 'Nicaragua'),
        ('niger', 'Níger'),
        ('nigeria', 'Nigeria'),
        ('noruega', 'Noruega'),
        ('nueva_caledonia', 'Nueva Caledonia'),
        ('nueva_zelanda', 'Nueva Zelanda'),
        ('oman', 'Omán'),
        ('pakistan', 'Pakistán'),
        ('palaos', 'Palaos'),
        ('panama', 'Panamá'),
        ('papua_nueva_guinea', 'Papúa Nueva Guinea'),
        ('paraguay', 'Paraguay'),
        ('peru', 'Perú'),
        ('polonia', 'Polonia'),
        ('portugal', 'Portugal'),
        ('puerto_rico', 'Puerto Rico'),
        ('reino_unido', 'Reino Unido'),
        ('republica_centroafricana', 'República Centroafricana'),
        ('republica_checa', 'República Checa'),
        ('republica_de_corea', 'República de Corea'),
        ('republica_democratica_del_congo', 'República Democrática del Congo'),
        ('republica_dominicana', 'República Dominicana'),
        ('rumania', 'Rumania'),
        ('rusia', 'Rusia'),
        ('sahara_occidental', 'Sahara Occidental'),
        ('samoa', 'Samoa'),
        ('samoa_americana', 'Samoa Americana'),
        ('san_bartolome', 'San Bartolomé'),
        ('san_cristobal_y_nieves', 'San Cristóbal y Nieves'),
        ('san_marino', 'San Marino'),
        ('san_vicente_y_las_granadinas', 'San Vicente y las Granadinas'),
        ('santa_helena', 'Santa Helena')
    ]

    #part - 1

    middle_name = fields.Char()
    second_surname = fields.Char()
    identification_number = fields.Char()
    sex = fields.Selection([('Femenino','Femenino'),('Masculino','Masculino')])
    # country_of_residence = fields.Selection(SELECTION_COUNTRY)
    country_of_residence = fields.Char()
    phone_or_cell_phone = fields.Char()
    type_diabetes = fields.Selection([
            ('1','Tengo diabetes tipo 1'),
            ('2','Soy Cuidador de una Persona con Diabetes Tipo'),
            ('3','Interesados')
        ])
    current_rule = fields.Selection([
        ('7','Teacher or school administrator'),
        ('8','Teacher or school administrator'),
        ('9','Teacher or school administrator'),
    ])
    type_2_diabetes = fields.Selection([
            ('1','Madre'),
            ('2','Padre'),
            ('3','Hermana(o)'),
            ('4','Cónyuge'),
            ('5','Abuela(o)'),
            ('9','Otro'),
        ])
    specifies = fields.Char()
    like_volunteer_or_leader = fields.Selection([('yes','Yes'),('no','No')])

    #part - 2 

    first_name_2 = fields.Char()
    middle_name_2 = fields.Char()
    first_surname_2 = fields.Char()
    second_surname_2 = fields.Char()
    # country_of_residence_2 = fields.Selection(SELECTION_COUNTRY)
    country_of_residence_2 = fields.Char()
    address_2 = fields.Char()
    city_2 = fields.Char()
    province = fields.Selection([
        ('Bocas del Toro', 'Bocas del Toro'),
        ('Coclé', 'Coclé'),
        ('Colón', 'Colón'),
        ('Chiriquí', 'Chiriquí'),
        ('Darién', 'Darién'),
        ('Herrera', 'Herrera'),
        ('Los Santos', 'Los Santos'),
        ('Panamá', 'Panamá'),
        ('Panamá Oeste', 'Panamá Oeste'),
        ('Veraguas', 'Veraguas'),
        ('Emberá-Wounaan', 'Emberá-Wounaan'),
        ('Guna Yala', 'Guna Yala'),
        ('Ngöbe-Buglé', 'Ngöbe-Buglé')
    ])
    identification_number_2 = fields.Char()
    diabetes_treat_condition = fields.Selection([
        ('1', 'Sistema público - Caja del seguro social'),
        ('2', 'Sistema público - Ministerio de salud'),
        ('3', 'Sistema privado - Consulta particular o privada'),
        ('4', 'Otro (especificar)')
    ])
    speci_diabetes_treat_condition = fields.Char()
    diabetes_treat_conditions = fields.Many2many('treat.condition')
    dob_2 = fields.Date()
    date_of_diagnosis = fields.Date()
    name_of_doc_treat_diabetes = fields.Selection([
        ('1', 'Medico 1'),
        ('2', 'Medico 2'),
        ('3', 'Medico 3'),
        ('4', 'Otro medico')
    ])
    other_medico = fields.Char()

    # part-3

    insulin_use = fields.Selection([
        ('NPH (Insuman)','Humana de acción intermedia (NPH; conocida como: Humulin N, Novolin N, turbia, vial verde, etc)'),
        ('NPH (Humulin N)','Análoga de acción prolongada (Glargina, Detemir, Degludec; conocidas como: Lantus, Abasaglar, Toujeo, Levemir, Tresiba, etc)'),
        ("NPH (Novolin N)","No uso insulina basal"),
        ("No sé","No sé"),
        ('Otro (Especifique)','Otro (Especifique)')
    ])
    other_insulin_use = fields.Char()
    rapid_insulin = fields.Selection([
        ('Insumar R','Humana de acción rápida (conocida como: Regular Humulin R, Novolin R, cristalina, vial amarillo'),
        ('Humulin R','Análoga de acción rápida (Aspart, Lispro, Glisulina, conocidas como: Humalog, NovoRapid, Apidra, Shorant, Fiasp, Actrapid, Lyumjev, Admelog, Trurapi, etc)'),
        ('Otro (Especifique)','Otro (Especifique)'),
    ])
    other_rapid_insulin = fields.Char()
    method_of_insulin_1 = fields.Selection([
        ('1',"Bomba o microinfusora de insulina"),
        ('2',"Jeringuillas, pens , bolígrafos, otros"),
    ])
    # method_of_insulin_2 = fields.Boolean()
    blood_glucose_monitoring = fields.Selection([
        ('1',"No uso"),
        ('2',"Dexcom"),
        ('3',"VivaChek"),
        ('4',"Eversense"),
        ('5',"Freestyle"),
        ('6',"Medtronic"),
        ('7',"Otro (especifique)"),
    ])
    spe_blood_glucose_monitoring = fields.Char()


    # part-4

    agreement_check = fields.Boolean()


class CrmLead(models.Model):
    _name = 'treat.condition'

    name = fields.Char()