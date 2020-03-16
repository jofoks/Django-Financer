function getExtension(filename) {
    var parts = filename.split('.');
    return parts[parts.length - 1];
  }
  
function isCSV(filename) {
    var ext = getExtension(filename);
    switch (ext.toLowerCase()) {
      case 'csv':
      case 'tsv':
        return true;
    }
    return false;
  }
  
$(function() {
    $('form').submit(function() {

  
      var file = $('#file');
      if (!isCSV(file.val())) {
        return failValidation('Please select a valid csv file');
      }
  
      // success at this point
      // indicate success with alert for now
      alert('Valid file! Here is where you would return true to allow the form to submit normally.');
      return false; // prevent form submitting anyway - remove this in your environment
    });
  
  });


function dropHandler(ev) {
console.log('File(s) dropped');

  function failValidation(msg) {
    alert(msg); // just an alert for now but you can spice this up later
    return false;
  }

ev.preventDefault();

if (ev.dataTransfer.items) {
    // Use DataTransferItemList interface to access the file(s)
    for (var i = 0; i < ev.dataTransfer.items.length; i++) {
    // If dropped items aren't files, reject them
    if (ev.dataTransfer.items[i].kind === 'file') {
        var file = ev.dataTransfer.items[i].getAsFile();
        if (!isCSV(file.val())) {
          return failValidation('Please select a valid csv file');
        }
        $.ajax({
        type: "POST",
        url: "../scripts/csv_interpreter.py",
        data: { param: file}
        }).done(function() {
        console.log('success!!!');
        });
    }
    }
} else {
    // Use DataTransfer interface to access the file(s)
    for (var i = 0; i < ev.dataTransfer.files.length; i++) {
    console.log('... file[' + i + '].name = ' + ev.dataTransfer.files[i].name);
    }
}
}
