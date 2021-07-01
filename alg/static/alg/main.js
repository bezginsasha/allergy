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

// Handle user-form

// var originUsername = document.querySelector('#originUsername');
// var originPassword = document.querySelector('#originPassword');
// var copyUsername = document.querySelector('#copyUsername');
// var copyPassword = document.querySelector('#copyPassword');

// originUsername.addEventListener('input', () => copyUsername.value = originUsername.value, false)
// originPassword.addEventListener('input', () => copyPassword.value = originPassword.value, false)

// Handle of drag and drop

var dropArea = document.querySelector('#drop-area');

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, preventDefaults, false)
})

function preventDefaults (e) {
  e.preventDefault()
  e.stopPropagation()
}

['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false)
});

['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unHighlight, false)
});

dropArea.addEventListener('drop', handleDrop, false);

function highlight() {
	dropArea.classList.add('highlight');
}

function unHighlight() {
	dropArea.classList.remove('highlight');
}

function handleDrop(e) {
	var dt = e.dataTransfer;
	var files = dt.files

	handleFiles(files);
}

function handleFiles(files) {
	uploadFile(files.item(0));
}

function uploadFile(file) {
	var url = 'http://localhost:8000/imp';
	var formData = new FormData();

	var csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

	var headers = new Headers({
		'X-CSRFToken': csrfToken,
	});

	formData.append('file', file);

	fetch(url, {
		method: 'POST',
		headers,
		body: formData,
	})
	.then(() => { location.reload() })
	.catch(() => { console.log('not ok') })
}