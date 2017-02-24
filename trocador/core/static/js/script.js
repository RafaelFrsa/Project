// Usando query para pegar observar o campo id_nome_fluido1 quando for alterado
$("#id_nome_fluido1").on("change", function (){
	// Se o valor selecionado no campo for igual a duplotubo_agua esconde o campo id_Vazao1
	if ($("#id_nome_fluido1").val() == "duplotubo_agua") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#agua").toggle();
	} else {
		$("#agua").toggle();
	};
});