(
    function() {
        const btnEliminar = document.querySelectorAll(".btnEliminar")

        btnEliminar.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const isConfirmed = confirm("Se eliminará el registro seleccionado. ¿Desea continuar?")
                
                if (!isConfirmed)
                    e.preventDefault()

            })
        })
        
    }
)();