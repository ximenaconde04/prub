(
    function() {
        const checkboxAlumno = document.querySelector("input[name=isNewAlumno]")

        checkboxAlumno.addEventListener('change', function() {
            if (this.checked) {
                document.getElementById("div-numero-control").style.display = 'block'
                document.getElementById("numeroControl").setAttribute('required', '');

                document.getElementById("div-nombre-completo").style.display = 'block'
                document.getElementById("nombreCompleto").setAttribute('required', '');

                document.getElementById("div-select-alumno").style.display = 'none'
                document.getElementById("idAlumno").removeAttribute('required')
            } else {
                document.getElementById("div-numero-control").style.display = 'none'
                document.getElementById("numeroControl").removeAttribute('required')

                document.getElementById("div-nombre-completo").style.display = 'none'
                document.getElementById("idAlumno").removeAttribute('required')

                document.getElementById("div-select-alumno").style.display = 'block'
                document.getElementById("idAlumno").setAttribute('required', '');
            }
          });
        
    }
)();