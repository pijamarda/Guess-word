
$( document ).ready(function() {

	/*
	*	Es la funcion principal que se llama cada vez que se introduce una palabra y se
	*	pulsa enter o se pulsa el boton.
	*	
	*/
	$('.palabra_check_ajax').click(function()
	{	
		$('#no_existe').html("");
		//Primero nos traemos los atributos necesarios desde el "formulario"
		//Estos son los intentos, la palabra introducida y la palabra a adivinar
		var intentos = $(this).attr("data-intentos");
		var guess = $('#input_palabra').val();		
		var palabra = $('#palabra_hidden').val();
		
		//Llamamos al API REST que tenemos creado en la vista de DJANGO views.check_guess
		//y le pasamos 2 parametros para ser obtenidos desde GET
		$.get('/check_guess/', {guess: guess, palabra: palabra},function(data)
		{	
			//Despues de llamar a la API REST esta nos devuelve un JSON que lleva entre
			//otros parametros un numero indicandonos el resultado de la operacion
			var resultado = data.resultado;
			var letras_iguales = parseInt(data.letras_iguales);
			var distancia = parseInt(data.distancia_letra);
			//Si devolvemos 1 entonces la palabra buscada es mayor
			if (resultado == 1)
			{
				console.log("La palabra que buscas es mayor");
				//Tambien deberiamos mirar si la segunda letra es igual ver el orden alfabetico
				var str1 = new String(guess);				
				var str2 = new String($('#under_word').text());				
				if (str2 == '')
				{
					str2 = 'aaaaaaaaaaaaaaaa';
				}
				console.log(str1+" < "+str2);	
				if (str1.localeCompare(str2) == -1)
				{
					console.log("antigua es mayor");														
				}					
				else
				{
					$('#under_word').html(guess);
				}
				
				$('#resultado').html("es MAYOR");				
				$('#listado_palabras').prepend('<li>'+guess+'</li>');
			}
			else if (resultado == 2)
			{
				console.log("La palabra que buscas es menor");
				
				//Tambien deberiamos mirar si la segunda letra es igual ver el orden alfabetico
				var str1 = new String(guess);
				var str2 = new String($('#upper_word').text());
				if (str2 == '')
				{
					str2 = 'zzzzzzzzzzzzzzzz';
				}
				console.log(str1+" < "+str2);
				if (str1.localeCompare(str2) == -1)
				{
					console.log("antigua es mayor")
					$('#upper_word').html(guess);						
				}					
				
				$('#resultado').html("es MENOR");
				$('#listado_palabras').prepend('<li>'+guess+'</li>');
			}
			else if (resultado == 3)
			{
				console.log("La palabra que buscas es igual");
				$('#resultado').html("GANASTE!");
				var link_save = "<a href=\"/save/"+(parseInt(intentos)+1)+"/"+palabra+"\">Save</a>" ;
				var link_save_jquery = "/save/"+(parseInt(intentos)+1)+"/"+palabra;				
				$.get(link_save_jquery, function(data)
				{
					//
				});
				//Una vez que acertamos la palabra deshabilitamos el campo a rellenar y el boton
				$('#input_palabra').prop( "disabled", true );				
				$('#boton_palabra').prop( "disabled", true );
				$('#listado_palabras').prepend('<li><b>'+guess+'</b></li>');

				//window.location.href = "/resultado?intentos="+(parseInt(intentos)+1)+"&word="+palabra;
			} else if (resultado == 4)
			{
				console.log("La palabra que buscas no existe");
				//Vamos a crear un boton de "reportar" de manera que si el usuario piensa que existe
				//se pueda notificar al creador de la aplicacion
				var boton_reportar = "<a target='_blank' href='/reportar/"+guess+"'>REPORTAR</a> ";
				var boton_rae = "<a target='_blank' href='http://lema.rae.es/drae/?val="+guess+"'>"+guess+"</a>";
				$('#resultado').html("No existe");
				$('#no_existe').html("Buscar en RAE: "+boton_rae+" Reportar: "+boton_reportar);
				//Voy a intentar un modal				
			}
			
		});
		var intentos_actualizado;
		intentos_actualizado=parseInt(intentos)+1;
		$(this).attr("data-intentos",intentos_actualizado);
		$('#intentos').html(intentos_actualizado);
		$('#input_palabra').val('');
	});

	$('#input_palabra').on('keyup', function(e) {
    	if (e.keyCode === 13) {
        	$('#boton_palabra').click();
	    }
	});

	$('.me_rindo').click(function()
	{
		var intentos = $('#boton_palabra').attr("data-intentos");
		$('#no_existe').html("");
		var palabra = $('#palabra_hidden').val();
    	$('#input_palabra').prop( "disabled", true );				
		$('#boton_palabra').prop( "disabled", true );
		var html_me_rindo = "<a target='_blank' href='http://lema.rae.es/drae/?val="+palabra+"'>RAE: "+palabra+"</a>";
		$('#me_rindo_resultado').html(html_me_rindo);
		var html_me_rindo_reportar = "<a target='_blank' href='/reportar/"+palabra+"'>REPORTAR</a>";
		$('#me_rindo_reportar').html(html_me_rindo_reportar);
		var link_merindo_jquery = "/merindo/"+(parseInt(intentos))+"/"+palabra;				
		$.get(link_merindo_jquery, function(data)
		{
			//
		});
	});

});