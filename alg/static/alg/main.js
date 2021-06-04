var lastId;

function getElementById(id) {
	return document.querySelector('#' + id);
}

function hideElement(element) {
	element.style.display = 'none';
}

function showElement(element) {
	element.style.display = 'inline-block';
}

function showEditButtons(allergyId) {
	showElement(getElementById('delete' + allergyId));
	showElement(getElementById('edit' + allergyId));

	hideElement(getElementById('enrage' + allergyId));
	hideElement(getElementById('more' + allergyId));
}

function showEnrageButton(allergyId) {
	hideElement(getElementById('delete' + allergyId));
	hideElement(getElementById('edit' + allergyId));

	showElement(getElementById('enrage' + allergyId));
	showElement(getElementById('more' + allergyId));
}

function show(allergyId) {
	if (lastId != undefined) {
		showEnrageButton(lastId);
	}
	showEditButtons(allergyId);
	lastId = allergyId;
}

function duplicateInput(allergyId) {
	var name = getElementById('name' + allergyId);
	var hiddenName = getElementById('hiddenName' + allergyId);

	hiddenName.value = name.innerText;
}