//HOJA DE MANEJO EVENTOS
//var objComisionFamilia = new Object();
var dict_ComisionFamilia = new Object();
var jsonEmpleado = new Object();
var dict_ComisionesEliminadas = new Object() // solo usar cuando el MODO es 'edicion'
var MODO = 'alta'; // 'alta', 'edicion'
var MESES = {'enero':'01', 'febrero':'02', 'marzo':'03', 'abril':'04', 'mayo':'05', 'junio':'06', 'julio':'07', 'agosto':'08', 'setiembre':'09', 'octubre':'10', 'noviembre':'11', 'diciembre':'12'}
jsonEmpleado.col_comisiones_eliminadas = {};

$(document).ready(function(){
	//limpio los forms al cargar la pagina
	limpiarFormulario('#form-sueldos');
	
	//MASCARAS
	//$.mask.definitions['n'] = "[0-9]";
	$('#empleado-numero').mask('99999999999', {placeholder: '-'});
	$('#empleado-sueldo-fijo').mask('9999?9.99', {placeholder: '-'});
	$('#producto-valor-comision').mask('9?99', {placeholder: '-'});
	//habilitar los botones correspondientes segun tab activo.
	$('.tab-sueldos, .tab-pagos').on('click', function(){
		if ($(this).hasClass('tab-sueldos')){
			//si estoy en la pestaña de sueldos debo habilitar btn-guardar y btn-copiar
			$('#btn-imprimir, #btn-copiar').addClass('disabled');
			$('#btn-guardar, #btn-buscar').removeClass('disabled');
		}else{
			//si estoy en la pestaña de pagos debo habilitar btn-consultar y btn-copiar
			$('#btn-imprimir, #btn-copiar').removeClass('disabled');
			$('#btn-guardar, #btn-buscar').addClass('disabled');
		}
	});

	//llamadas ajax para cargar datos inciales
	obtenerFamiliasProductos(); 
	
	//ACCIONES DE BOTONES
	$('#btn-guardar').on('click', function(){
		if (validarFormulario('#form-sueldos')) {
			//despues de las validaciones llama a
			jsonEmpleado.nro = $('#empleado-numero').val();
			jsonEmpleado.nombre = $('#empleado-nombre').val();
			jsonEmpleado.direccion = $('#empleado-direccion').val();
			jsonEmpleado.sueldo_fijo = $('#empleado-sueldo-fijo').val();
			jsonEmpleado.comisiones = dict_ComisionFamilia;
			jsonEmpleado.modo = MODO;
			
			//limpio las variables globales para reutilizarlas
			//objComisionFamilia = new Object();
			dict_ComisionFamilia = new Object();

			limpiarFormulario('#form-sueldos');
			//alert('se puede guardar');
			guardarSueldoDeEmpleadoX(jsonEmpleado);
		}
	});
	$('#btn-buscar').on('click', function(){
		limpiarFormulario($('#modal-empleados'));
		buscarEmpleados();
		//obtiene sus datos de
		//buscarEmpleados();
	});

	$('#btn-copiar').on('click', function(){});

	$('#btn-imprimir').on('click', function(){
		alert('Sin implementación momentaneamente.');
	});

	$('#btn-agregar-comision').on('click', function(e){
		e.preventDefault();
		if ($('#producto-valor-comision').val() == '') {
			$('#producto-valor-comision').addClass('invalido');
		}else {
			$('#producto-valor-comision').removeClass('invalido');
			var familia_id = $('#producto-familia').val();
			var familia_nombre = $('#producto-familia option:selected').html();
			var comision = $('#producto-valor-comision').val();
			//si no ingresan los digitos restantes
			if (comision.length == 1) {
				comision = comision + '00';
			}else if (comision.length == 2) {
				comision = comision + '0';
			}
			comision = '0.' + comision;
			var nodo = crearFilaComisionXFamilia(familia_id, familia_nombre, comision);
			if (evaluarSiYaExisteFamiliaListada(familia_id)) {
				$('#id-' + familia_id + ' .valor-comision').html(comision);
				$('#producto-valor-comision').val(''); // limpio la caja de comisiones
				alert('Has sobreescrito la comisión para la familia: ' + familia_nombre);
				// me falta reescribir la familia en el dict_ComisionFamilia
				return false;
			}

			var objComisionFamilia = new Object();

			objComisionFamilia.nombre_familia = familia_nombre;
			objComisionFamilia.id_familia = familia_id;
			objComisionFamilia.porcentaje_comision = comision;
			//objComisionFamilia.objFilaHTML = nodo;
			var key = objComisionFamilia.id_familia;
			dict_ComisionFamilia[key] = objComisionFamilia;
			$('#producto-valor-comision').val(''); // limpio la caja de comisiones
			$(nodo).appendTo('#tabla-familia-comision');
		}
	});
	
	$('#tabla-familia-comision').on('click', function(e){
		//e.preventDefault();
		//alert(e.target.nodeName);
		if ($(e.target).html() == 'X') {
			var id = $(e.target).parent().parent().attr('id').split('-')[1];
			if (MODO == 'edicion') {
				var objComisionFamilia = new Object();

				objComisionFamilia.nombre_familia = $(e.target).parent().parent().find('.comision-nombre-familia').html();
				objComisionFamilia.id_familia = id;
				objComisionFamilia.porcentaje_comision = $(e.target).parent().parent().find('.valor-comision').html();
				dict_ComisionesEliminadas[id] = objComisionFamilia;
				jsonEmpleado[col_comisiones_eliminadas] = dict_ComisionesEliminadas;
			}
			

			$(e.target).parent().parent().remove(); //remuevo de la tabla
			delete dict_ComisionFamilia[id]; //remuevo de la lista
		}
	});

	$('#tabla-empleados').on('click', function(e) {
		e.preventDefault();
		if ($(e.target).html() == 'X') {
			if (confirm('Desea eliminar permanentemente este empleado?')) {
				var id = $(e.target).parent().parent().attr('id').split('-')[1];
				eliminarEmpleadoX(id);	
			}
		}else{
			//alert(e.target.nodeName);
			$('#btn-editar-empleado').removeClass('disabled');
			$('#tabla-empleados').find('.pintado').each(function(){
				$(this).removeClass('pintado');
			});
			$(e.target).parent().addClass('pintado');
		}
	});

	$('#btn-editar-empleado').on('click', function() {
		var fila = $('#tabla-empleados').find('.pintado');
		var id = $(fila).attr('id').split('-')[1];
		//alert(id);
		$('#btn-editar-empleado').addClass('disabled');
		MODO = 'editar';
		$('#modal-empleados').modal('hide');
		obtenerEmpleadoX(id);
		//alert('editar empleado');
	});

	//$(document).on('click', '.clickeable',function(e) { //usar esta forma cuando se bindea nodos creados directamente
	//	e.preventDefault();
	//	//alert(e.target.nodeName);
	//	var id = $(this).attr("id");
	//	var obj = dict_ComisionFamilia[id];
	//	$('#producto-valor-comision').val(obj.porcentaje_comision);
	//	$('#producto-familia option[value="' + id + '"]').attr('selected', 'selected');
	//});
	
	$('#select-sueldo-anio').on('change', function() {
		var mes = MESES[$('#select-sueldo-mes').val()];
		var anio = null;
		//alert('cambia anio');
		$(this).find(':selected').each(function() {
			anio = $(this).val();
		});
		//mediante ajax obtener los empleados y sus sueldos
		obtenerSueldosXMes({'anio':anio, 'mes':mes});
	});
});

function cargarCBoxFamilias(datos) {
	var nodo = null;
	for (id in datos) {
		nodo = $('<option value="' + id + '">' + datos[id] + '</option>');
		$(nodo).appendTo('#producto-familia');
	}
}

function evaluarSiYaExisteFamiliaListada(familia_id) {
	for (key in dict_ComisionFamilia) {
		if (key == familia_id) {
			return true;
		}
	}
	
	return false;
}

function crearFilaComisionXFamilia(familia_id, familia_nombre, comision) {
	var fila = '<tr id="id-' + familia_id + '">' +
        						'<td class="comision-nombre-familia">' +
        							familia_nombre +
        						'</td>' +
        						'<td class="valor-comision">' +
        							comision +
        						'</td>' +
        						'<td><a class="btn btn-xs btn-danger eliminar-familia-comision">X</a></td>' +
        					'</tr>';
	return $(fila);
}

function cargarTablaSueldos(obj_json) {
	$('#aviso-tabla-sueldos').hide();

	$.each(obj_json, function(i, val) {
		var fila = '<tr id="id-' + val.id + '">' +
        						'<td class="empleado-nombre">' +
        							val.empleado +
        						'</td>' +
        						'<td class="empleado-sueldo">' +
        							val.monto +
        						'</td>' +
        					'</tr>';
        		$(fila).appendTo('#tabla-salarios');
	});
}

function cargarTablaEmpleados(obj_json) {
	//$('#aviso-tabla-sueldos').hide();

	$.each(obj_json, function(i, val) {
		var fila = '<tr class="fila-empleado" id="id-' + val.id + '">' +
						'<td class="empleado-numero">' +
        							val.numero +
        						'</td>' +
        						'<td class="empleado-nombre">' +
        							val.nombre +
        						'</td>' +
        						'<td><a href="#" class="btn btn-danger empleado-eliminar">X</a></td>' +
        					'</tr>';
        		$(fila).appendTo('#tabla-empleados');
	});
}

function cargarFormularioEmpleado(json) {

	$('#empleado-numero').val(json.numero);
	$('#empleado-nombre').val(json.nombre);
	$('#empleado-direccion').val(json.direccion);
	$('#empleado-sueldo-fijo').val(json.sueldo_fijo);
	jsonEmpleado.modo = MODO;
	
	$.each(	json.comisiones, function(index, value) {
		var familia_id = value.fam_id;
		var familia_nombre = value.fam_nombre;
		var comision = value.porcentaje;
		var nodo = crearFilaComisionXFamilia(familia_id, familia_nombre, comision);

		var objComisionFamilia = new Object();

		objComisionFamilia.nombre_familia = familia_nombre;
		objComisionFamilia.id_familia = familia_id;
		objComisionFamilia.porcentaje_comision = comision;
		
		dict_ComisionFamilia[objComisionFamilia.id_familia] = objComisionFamilia;

		$(nodo).appendTo('#tabla-familia-comision');
	});
}

function validarFormulario(formulario) {
	var valido = true;
	$.each($(formulario).find('.obligatorio'), function(k, v){
		//si es un input type text
		//v.tagName
		if (v.tagName == 'INPUT' && v.type == 'text'){
			if ($(v).val() == '') {
				$(v).addClass('invalido');
				valido = false;
			}else{
				$(v).removeClass('invalido');
			}
		}//continuar aca con otro tipo de controles
	});
	return valido;
}

function limpiarFormulario(formulario) {
	$.each($(formulario).find('.limpiable'), function(k, v){
		if (v.tagName == 'INPUT' && v.type == 'text'){
			$(v).val('');
		} else if ( v.tagName == 'SELECT' ) {
			$(v).prop('selectedIndex', 0);
		} else if (v.tagName == 'TABLE') {
			$(v).find('tr').remove();
			if ($(v).attr('id') == 'tabla-salarios') {
				$('<tr>' +
        						'<th>Empleado</th>' +
        						'<th>Sueldo</th>' +
        					'</tr>').appendTo($(v));
			}else if ($(v).attr('id') == 'tabla-empleados') {
				$('<tr>' +
        						'<th>Número</th>' +
        						'<th>Nombre</th>' +
        						'<th> </th>' +
        					'</tr>').appendTo($(v));
			}
		}//continuar aca con otro tipo de controles
	});
}


//FUNCIONES AJAX A PARTIR DE ACA

function guardarSueldoDeEmpleadoX(objEmpleado) {
	
	//TODO:llamada al controlador en cuestion
	//al final debo limpiar la global de abajo
	//url: app/sueldos/guardar-empleado/
	//jsonEmpleado = new Object();
	//alert(JSON.stringify(objEmpleado));
	jQuery.ajax({
	        url: 'http://localhost:8000/app/sueldos/guardar-empleado/',
	        method: "POST",
	        dataType: "json",
	        data:JSON.stringify(objEmpleado),
	        success: function(json) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.success').show();
	              //console.log(json.message);
	              //alert('Resultado: '+ json.numero + '\n' + 'Resultado: '+ json.nombre);
	              if (MODO == 'alta') {
	              	alert('Guardado');	
	              } else if (MODO == 'edicion') {
	              	alert('Modificado');
	              	MODO = 'alta';
	              }
	        },
	        error: function(jqXHR, textStatus, errorThrown) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.fail').show().append(errorThrown);
	              //console.log(textStatus);
	              alert(textStatus);
	              alert(errorThrown);
	        }
    	});
}

function obtenerFamiliasProductos(){
	jQuery.ajax({
	        url: 'http://localhost:8000/app/sueldos/obtener-familias/',
	        method: "POST",
	        dataType: "json",
	        data:{},
	        success: function(json) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.success').show();
	              //console.log(json.message);
	              cargarCBoxFamilias(json);
	        },
	        error: function(jqXHR, textStatus, errorThrown) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.fail').show().append(errorThrown);
	              //console.log(textStatus);
	              alert(textStatus);
	              alert(errorThrown);
	        }
    	});
}

function obtenerSueldosXMes(anioymes){
	//alert('llega a la funcion obtenerSueldosXMes');
	jQuery.ajax({
	        url: 'http://localhost:8000/app/sueldos/sueldos-por-mes/',
	        method: "POST",
	        dataType: "json",
	        data:anioymes,
	        success: function(json) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.success').show();
	              //console.log(json.message);
	              //alert('success');
	              cargarTablaSueldos(json);
	        },
	        error: function(jqXHR, textStatus, errorThrown) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.fail').show().append(errorThrown);
	              //console.log(textStatus);
	              alert(textStatus);
	              alert(errorThrown);
	        }
    	});
}

function buscarEmpleados() {
	//alert('llega a la funcion obtenerSueldosXMes');
	jQuery.ajax({
	        url: 'http://localhost:8000/app/sueldos/obtener-empleados/',
	        method: "POST",
	        dataType: "json",
	        data:{},
	        success: function(json) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.success').show();
	              //console.log(json.message);
	              //alert('success');
	              cargarTablaEmpleados(json);
	        },
	        error: function(jqXHR, textStatus, errorThrown) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.fail').show().append(errorThrown);
	              //console.log(textStatus);
	              alert(textStatus);
	              alert(errorThrown);
	        }
    	});
}

function eliminarEmpleadoX(id) {
	jQuery.ajax({
	        url: 'http://localhost:8000/app/sueldos/eliminar-empleado/',
	        method: "POST",
	        dataType: "json",
	        data:{'id':id},
	        success: function(json) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.success').show();
	              //console.log(json.message);
	              //alert('success');
	             if (json['result']) {
			$('#id-' + id).remove();
	             	//alert('Eliminado');
	             }
	        },
	        error: function(jqXHR, textStatus, errorThrown) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.fail').show().append(errorThrown);
	              //console.log(textStatus);
	              alert(textStatus);
	              alert(errorThrown);
	        }
    	});
}

function obtenerEmpleadoX(id) {
	jQuery.ajax({
	        url: 'http://localhost:8000/app/sueldos/obtener-empleado/',
	        method: "POST",
	        dataType: "json",
	        data:{'id':id},
	        success: function(json) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.success').show();
	              //console.log(json.message);
	              //alert('success');
	             cargarFormularioEmpleado(json); 
	        },
	        error: function(jqXHR, textStatus, errorThrown) {
	              //jQuery(".signup").attr('disabled', false);
	              //$('.fail').show().append(errorThrown);
	              //console.log(textStatus);
	              alert(textStatus);
	              alert(errorThrown);
	        }
    	});
}

function copiar() {} //copiar que??

function consultar() {} //consultar que??
