// Table search + category filter (works on any table with class "filterable")
document.addEventListener('DOMContentLoaded', function () {
  var q = document.getElementById('q');
  var cat = document.getElementById('cat');
  var status = document.getElementById('status');
  var table = document.querySelector('table.filterable');
  if (!table || !q) return;
  function apply() {
    var needle = q.value.toLowerCase();
    var c = cat ? cat.value : '';
    var s = status ? status.value : '';
    table.querySelectorAll('tbody tr').forEach(function (tr) {
      var okText = tr.textContent.toLowerCase().includes(needle);
      var okCat = !c || tr.dataset.cat === c;
      var okStatus = !s || tr.dataset.status === s;
      tr.style.display = (okText && okCat && okStatus) ? '' : 'none';
    });
  }
  q.addEventListener('input', apply);
  if (cat) cat.addEventListener('change', apply);
  if (status) status.addEventListener('change', apply);
});
