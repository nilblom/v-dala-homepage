document.addEventListener("DOMContentLoaded", function() {
    enable_translate();

    if (localStorage.getItem("language") == "en")
    	translate();

    enable_contact_helper();
});


/* Functions to enable translation to English. */

function enable_translate() {
	document.getElementById("switch-language").addEventListener("click", function(e) {
		translate();
		if (localStorage.getItem("language") == "sv")
			localStorage.setItem("language", "en");
		else
			localStorage.setItem("language", "sv");
	});
}

function translate() {
	document.querySelectorAll("[t]").forEach(node => {
		var original_text = node.innerText;
		node.innerText = node.getAttribute("t");
		node.setAttribute("t", original_text);
	});
}

function enable_contact_helper() {
	var helper = document.getElementById("contact-helper-select");
	var display = document.getElementById("contact-helper-display");
	helper.onchange = function() {
		display.value = helper.value;
	}
	// Initialize the helper.
	display.value = helper.value;
}
