function toggleText() {
  var x = document.getElementById("drop-button");
  if (x.innerHTML === "Hide transactions") {
    x.innerHTML = "Show transactions";
  } else {
      console.log(x.innerHTML)    
    x.innerHTML = "Hide transactions";
  }
}

function dropMenu() {
  document.getElementById('myDropdown').classList.toggle('show');
  }

function toggleSpinTable(pos) {
  document.getElementById('spin_id_'+pos).classList.toggle('spin');
  }

function toggleSpinList() {
  document.getElementById('spin-btn-list').classList.toggle('spin');
  }

function toggleDisplay(pos) {
  console.log(pos)
  document.getElementById('drop_id_'+pos).classList.toggle('show-table');
  }

function scream(event) {
  event.preventDefault()
  console.log('SCREAMING')
}


// ---------------------------------------------- //




function dropZoneHandler(ev) {
  var dropzone = document.getElementById('dropzone')

  dropzone.ondrop = function(ev) {
    ev.preventDefault();
    this.className = 'circle';
    var files = ev.dataTransfer.files;
    $.ajax({
      type: "POST",
      processData: false,
      contentType: false,
      url: "../../static/scripts/csv_interpreter.py",
      data: { param: files}
      })
      .done(function(msg){ console.log('Succes!') })
      .fail(function(xhr, status, error) {
        console.log('something went wrong: '+ error)
      });
  };

  dropzone.ondragover = function() {
    this.className = 'circle dragover';
    return false;
  };

  dropzone.ondragleave = function() {
    this.className = 'circle';
    return false;
  };
}


