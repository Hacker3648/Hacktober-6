/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.country_code = publicWidget.Widget.extend({
	selector: '.s_website_form_rows',
	events: {
		'change .country_id': 'country_code',
		'change .1_detail': 'type_diabetes',
		'change .1_detail_hidden, .2_detail_hidden': 'sub_type_diabetes',
		'change .2_country': 'country_2',
		'click .s_website_form_send': 'check_validation',
		'change .medico_type': 'open_medico_other',
	},

	open_medico_other: function (ev) {
		if (ev.currentTarget.value == '4') {
			$('#other_medico')[0].classList.remove('d-none')
		} else	{
			$('#other_medico')[0].classList.add('d-none')
		}
	},

	check_validation: function(ev) {
		const collapseDivIds = [
		    'myCollapse1647024375501',
		    'myCollapseTab1647024375503',
		    'myCollapseTab1647024375504',
		    'myCollapseTab1647024917315'
		];
		let form = document.getElementById('studio_cust');
		let invalidRequiredFields = form.querySelectorAll('[required].is-invalid');
		if (invalidRequiredFields.length > 0) {
		    collapseDivIds.forEach(id => {
		    // Find any fields with the class 'is-invalid' within the current collapse div
			    if ($(`#${id} .is-invalid`).length > 0) {
			        // Add the 'show' class to the current collapse div
			        $(`#${id}`).addClass('show');
			    }
			});
			invalidRequiredFields[0].focus();
		    // invalidRequiredFields[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
		}
		if (invalidRequiredFields.length == 0 && document.querySelector('#s_website_form_result').style.visibility != 'hidden') {
			const form_data = document.getElementById('studio_cust');
			form_data.submit();
		}
	},

	country_2:function(ev) {
		if (ev.currentTarget.value == "172") {
			$('.address_2')[0].classList.remove('d-none')
			$('.city_2')[0].classList.remove('d-none')
			$('.select2_multi')[0].classList.remove('d-none')
			$('.no_select2_multi')[0].classList.add('d-none')
			$('.doctor_name')[0].classList.remove('d-none')
			$('.Provincia_field')[0].classList.remove('d-none')
		} else {
			$('.address_2')[0].classList.add('d-none')
			$('.city_2')[0].classList.add('d-none')
			$('.select2_multi')[0].classList.add('d-none')
			$('.no_select2_multi')[0].classList.remove('d-none')
			$('.doctor_name')[0].classList.add('d-none')
			$('.Provincia_field')[0].classList.add('d-none')
		}
	},

	sub_type_diabetes: function(ev) {
		if (ev.currentTarget.value == '9') {
			$('.others')[0].classList.remove('d-none')
		} else {
			$('.others')[0].classList.add('d-none')
		}
		if (ev.currentTarget.value == '7') {
			disabledCase4a9();
			disabledCase7();
			document.getElementById("myCollapse1647024375501").classList.remove("show");
			document.getElementById("myCollapseTab1647024917315").classList.add("show");
		} else if (ev.currentTarget.value == '8') {
			disabledCase4a9();
			disabledCase8();
			document.getElementById("myCollapse1647024375501").classList.remove("show");
			document.getElementById("myCollapseTab1647024917315").classList.add("show");
		} else if (ev.currentTarget.value == '10') {
			disabledCase4a9();
			disabledCase8();
			document.getElementById("myCollapse1647024375501").classList.remove("show");
			document.getElementById("myCollapseTab1647024917315").classList.add("show");
		}
	},

	type_diabetes: function(ev) {
		if (ev.currentTarget.value == '2') {
			$('.1_select_hidden')[0].classList.remove('d-none')
		} else {
			$('.1_select_hidden')[0].classList.add('d-none')
		}
		if (ev.currentTarget.value == '3') {
			$('.2_select_hidden')[0].classList.remove('d-none')
		} else {
			$('.2_select_hidden')[0].classList.add('d-none')
		} 
	},

	country_code: function (ev) {
		const country_codes = {
			"Afgánistan": "+93",
			"Albania": "+355",
			"Alemania": "+49",
			"Andorra": "+376",
			"Angola": "+244",
			"Anguilla": "+1-264",
			"Antigua y Barbuda": "+1-268",
			"Antártida": "+672",
			"Arabia Saudita": "+966",
			"Argelia": "+213",
			"Argentina": "+54",
			"Armenia": "+374",
			"Aruba": "+297",
			"Australia": "+61",
			"Austria": "+43",
			"Azerbaiyán": "+994",
			"Bahamas": "+1-242",
			"Bahréin": "+973",
			"Bangladesh": "+880",
			"Barbados": "+1-246",
			"Belice": "+501",
			"Benín": "+229",
			"Bermudas": "+1-441",
			"Bhután": "+975",
			"Bielorrusia": "+375",
			"Birmania": "+95",
			"Bolivia": "+591",
			"Bonaire, San Eustaquio y Saba": "+599",
			"Bosnia-Herzegovina": "+387",
			"Botsuana": "+267",
			"Brasil": "+55",
			"Brunei Darussalam": "+673",
			"Bulgaria": "+359",
			"Burkina Faso": "+226",
			"Burundi": "+257",
			"Bélgica": "+32",
			"Cabo Verde": "+238",
			"Camboya": "+855",
			"Camerún": "+237",
			"Canadá": "+1",
			"Chad": "+235",
			"Chile": "+56",
			"China": "+86",
			"Chipre": "+357",
			"Colombia": "+57",
			"Comores": "+269",
			"Congo": "+242",
			"Corea del Norte": "+850",
			"Corea del Sur": "+82",
			"Costa Rica": "+506",
			"Costa de Marfil": "+225",
			"Croacia": "+385",
			"Cuba": "+53",
			"Curaçao": "+599",
			"Dinamarca": "+45",
			"Dominica": "+1-767",
			"EE.UU. Islas Exteriores Menores": "+1-340",
			"Ecuador": "+593",
			"Egipto": "+20",
			"El Salvador": "+503",
			"Emiratos Árabes Unidos": "+971",
			"Eritrea": "+291",
			"Eslovaquia": "+421",
			"Eslovenia": "+386",
			"España": "+34",
			"Estado de Palestina": "+970",
			"Estados Unidos": "+1",
			"Estonia": "+372",
			"Etiopía": "+251",
			"Federación Rusa": "+7",
			"Fiji": "+679",
			"Filipinas": "+63",
			"Finlandia": "+358",
			"Francia": "+33",
			"Gabón": "+241",
			"Gambia": "+220",
			"Georgia": "+995",
			"Ghana": "+233",
			"Gibraltar": "+350",
			"Granada": "+1-473",
			"Grecia": "+30",
			"Groenlandia": "+299",
			"Guadalupe": "+590",
			"Guam": "+1-671",
			"Guatemala": "+502",
			"Guayana": "+592",
			"Guayana Francesa": "+594",
			"Guernsey": "+44-1481",
			"Guinea": "+224",
			"Guinea Ecuatorial": "+240",
			"Guinea-Bisáu": "+245",
			"Haití": "+509",
			"Holanda": "+31",
			"Honduras": "+504",
			"Hong Kong": "+852",
			"Hungría": "+36",
			"India": "+91",
			"Indonesia": "+62",
			"Irak": "+964",
			"Irlanda": "+353",
			"Irán": "+98",
			"Isla Bouvet": "+47",
			"Isla Norfolk": "+672",
			"Isla de Man": "+44-1624",
			"Isla de Navidad": "+61",
			"Islandia": "+354",
			"Islas Caimán": "+1-345",
			"Islas Cocos (Keeling)": "+61",
			"Islas Cook": "+682",
			"Islas Feroe": "+298",
			"Islas Georgia del Sur y Sandwich del Sur": "+500",
			"Islas Heard y McDonald": "+61",
			"Islas Malvinas": "+500",
			"Islas Marianas del Norte": "+1-670",
			"Islas Marshall": "+692",
			"Islas Pitcairn": "+64",
			"Islas Salomón": "+677",
			"Islas Turcas y Caicos": "+1-649",
			"Islas Vírgenes (Británicas)": "+1-284",
			"Islas Vírgenes (EE.UU.)": "+1-340",
			"Islas Åland": "+358-18",
			"Israel": "+972",
			"Italia": "+39",
			"Jamaica": "+1-876",
			"Japón": "+81",
			"Jersey": "+44-1534",
			"Jordania": "+962",
			"Kazajstán": "+7",
			"Kenia": "+254",
			"Kirguistán": "+996",
			"Kiribati": "+686",
			"Kosovo": "+383",
			"Kuwait": "+965",
			"Laos": "+856",
			"Lesotho": "+266",
			"Letonia": "+371",
			"Liberia": "+231",
			"Libia": "+218",
			"Liechtenstein": "+423",
			"Lituania": "+370",
			"Luxemburgo": "+352",
			"Líbano": "+961",
			"Macao": "+853",
			"Macedonia del Norte": "+389",
			"Madagascar": "+261",
			"Malasia": "+60",
			"Malawi": "+265",
			"Maldivas": "+960",
			"Mali": "+223",
			"Malta": "+356",
			"Marruecos": "+212",
			"Martinica": "+596",
			"Mauricio": "+230",
			"Mauritania": "+222",
			"Mayotte": "+262",
			"Micronesia": "+691",
			"Moldavia": "+373",
			"Mongolia": "+976",
			"Montenegro": "+382",
			"Montserrat": "+1-664",
			"Mozambique": "+258",
			"México": "+52",
			"Mónaco": "+377",
			"Namibia": "+264",
			"Nauru": "+674",
			"Nepal": "+977",
			"Nicaragua": "+505",
			"Nigeria": "+234",
			"Niue": "+683",
			"Noruega": "+47",
			"Nueva Caledonia": "+687",
			"Nueva Zelanda": "+64",
			"Níger": "+227",
			"Omán": "+968",
			"Pakistán": "+92",
			"Palau": "+680",
			"Panamá": "+507",
			"Papúa Nueva Guinea": "+675",
			"Paraguay": "+595",
			"Perú": "+51",
			"Polinesia Francesa": "+689",
			"Polonia": "+48",
			"Portugal": "+351",
			"Puerto Rico": "+1-787",
			"Qatar": "+974",
			"Reino Unido": "+44",
			"República Centro Africana": "+236",
			"República Checa": "+420",
			"República Democrática del Congo": "+243",
			"República Dominicana": "+1-809",
			"Reunión": "+262",
			"Ruanda": "+250",
			"Rumania": "+40",
			"Samoa": "+685",
			"Samoa Americana": "+1-684",
			"San Bartolomé": "+590",
			"San Cristóbal y Nieves": "+1-869",
			"San Marino": "+378",
			"San Martín (parte holandesa)": "+599",
			"San Martín (zona francesa)": "+590",
			"San Pierre y Miquelon": "+508",
			"San Vicente y las Granadinas": "+1-784",
			"Santa Elena, Ascensión y Tristán de Acuña": "+290",
			"Santa Lucía": "+1-758",
			"Santa Sede (Ciudad Estado del Vaticano)": "+39",
			"Santo Tomé y Príncipe": "+239",
			"Senegal": "+221",
			"Serbia": "+381",
			"Seychelles": "+248",
			"Sierra Leona": "+232",
			"Singapur": "+65",
			"Siria": "+963",
			"Somalia": "+252",
			"Sri Lanka": "+94",
			"Suazilandia": "+268",
			"Sudáfrica": "+27",
			"Sudán": "+249",
			"Sudán del Sur": "+211",
			"Suecia": "+46",
			"Suiza": "+41",
			"Surinam": "+597",
			"Svalbard y Jan Mayen": "+47",
			"Sáhara occidental": "+212",
			"Tailandia": "+66",
			"Taiwán": "+886",
			"Tajikistán": "+992",
			"Tanzania": "+255",
			"Territorio británico del Océano Índico": "+246",
			"Territorios franceses del sur": "+262",
			"Timor Oriental": "+670",
			"Togo": "+228",
			"Tokelau": "+690",
			"Tonga": "+676",
			"Trinidad y Tobago": "+1-868",
			"Turkmenistán": "+993",
			"Turquía": "+90",
			"Tuvalu": "+688",
			"Túnez": "+216",
			"Ucrania": "+380",
			"Uganda": "+256",
			"Uruguay": "+598",
			"Uzbekistán": "+998",
			"Vanuatu": "+678",
			"Venezuela": "+58",
			"Vietnam": "+84",
			"Wallis y Futuna": "+681",
			"Yemen": "+967",
			"Yibuti": "+253",
			"Zambia": ""
		}
		var code = country_codes[ev.currentTarget.value]
		$('#o1x6djfzjpst').val(code)
		if (ev.currentTarget.value == 'Panamá') {
			$('.panama')[0].classList.remove('d-none')
		} else {
			$('.panama')[0].classList.add('d-none')
		}
	},
}); 