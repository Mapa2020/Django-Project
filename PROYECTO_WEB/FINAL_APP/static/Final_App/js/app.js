// variables
const carrito = document.querySelector('#carrito');
const contenedorCarrito = document.querySelector('#lista-carrito tbody');
const listaCursos = document.querySelector('#lista-cursos');
const vaciarCarritoBtn = document.querySelector('#vaciar-carrito');
let articulosCarrito =[];

cargarEventListeners();
function cargarEventListeners(){
    //cuando agregas un curso presionando agregar carrito
    listaCursos.addEventListener('click', agregarCurso);

    //Elimina cursos del carrito
    carrito.addEventListener('click', eliminarCurso);

    //Muestra cursos del carrito
    document.addEventListener('DOMContentLoaded', () => {
        articulosCarrito = JSON.parse( localStorage.getItem('carrito')) || [];
        carritoHTML();
    })

    //vaciar carrito
    vaciarCarritoBtn.addEventListener('click', () =>{
        articulosCarrito = [];
        limpiaHTML(); //elimina todo el HTML
    })
}

//Funciones
function agregarCurso(e) {
    e.preventDefault();

    if(e.target.classList.contains('agregar-carrito')) {
        const cursoSeleccionado = e.target.parentElement.parentElement;
        leerDatosCurso(cursoSeleccionado);
    }   
}

//Elimina un curso del carrito
function eliminarCurso(e) {
    //console.log(e.target.classList);
    if(e.target.classList.contains('borrar-curso')){
        const cursoId = e.target.getAttribute('data-id');
        //elimina del arreglo articulosCarrito por el data-id
        articulosCarrito = articulosCarrito.filter( curso => curso.id !== cursoId );
        //console.log(articulosCarrito);
        carritoHTML(); // Iterar sobre el carrito y mostrar el HTML
    }
}

//Lee el contenido del HTML
function leerDatosCurso(curso) {
    console.log(curso);

    //crear el objeto con el contenido
    const infoCurso = {
        imagen: curso.querySelector('img').src,
        titulo: curso.querySelector('h4').textContent,
        precio: curso.querySelector('.precio span').textContent,
        id: curso.querySelector('a').getAttribute('data-id'),
        cantidad: 1
    }

    //Revisa si un elemento ya existe
    const existe = articulosCarrito.some( curso => curso.id === infoCurso.id );
    if(existe) {
        //Actualizamos la cantidad
        const cursos = articulosCarrito.map(curso =>{
            if (curso.id === infoCurso.id){
                curso.cantidad++;
                return curso;  //retorna el obj actualizado
            }else{
                return curso; // retorna los objetos que no son duplicados
            }
        });
        articulosCarrito = [...cursos];
    }else{
        //Agrega elementos al carrito
        articulosCarrito = [...articulosCarrito, infoCurso];
    }

    //console.log(infoCurso);
    
    console.log(articulosCarrito);
    carritoHTML();

    //Agregar el carrito de compras al localstorage
    sincronizarStorage();
}

function sincronizarStorage() {
    localStorage.setItem('carrito', JSON.stringify(articulosCarrito));
}

//muestra el carrito en el HTML
function carritoHTML() {
    //Limpiar el HTML
    limpiaHTML();
    articulosCarrito.forEach( curso => {
        const { imagen, titulo, precio, cantidad, id} = curso;
        const row = document.createElement('tr');
        //${curso.titulo}    ${curso.precio}    ${curso.cantidad}
        row.innerHTML = `
        <td>
            <img src = "${imagen}" width="100">
        </td> 
        <td>${titulo}</td> 
        <td>${precio}</td>
        <td>${cantidad}</td>
        <td>
            <a href="#" class="borrar-curso" data-id="${curso.id}"> X </a>
        </td>  
        `;

        //agregando el HTNL en el tbody
        contenedorCarrito.appendChild(row);

    });
}

//Elimina los cursos del tbody
function limpiaHTML(){
    //forma lenta
    //contendorCarrito.innerHTML ='';
    while(contenedorCarrito.firstChild){
        contenedorCarrito.removeChild(contenedorCarrito.firstChild)
    }
}