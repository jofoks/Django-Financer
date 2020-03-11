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

function toggleSpinTable() {
  document.getElementById('spin-btn-table').classList.toggle('spin');
  }

function toggleSpinList() {
  document.getElementById('spin-btn-list').classList.toggle('spin');
  }

function toggleDisplay(pos) {
  document.getElementById('drop-display-'+pos).classList.toggle('show');
  }