<!DOCTYPE html>
<html>
<head>
  <App para el tratamiento de fotografías>
</head>
<body>
  <h1>Proyecto de Eliminación de Fondo de Imágenes</h1>
  <p>Aplicación web desarrollada en Streamlit</p>
  
  <h2>Contenido</h2>
  <ul>
    <li><a href="#acerca-del-proyecto">Acerca del Proyecto</a></li>
    <li><a href="#características">Características</a></li>
    <li><a href="#instalación">Instalación</a></li>
    <li><a href="#cómo-usar">Cómo Usar</a></li>
    <li><a href="#contribuir">Contribuir</a></li>
    <li><a href="#colaboradores">Colaboradores</a></li>
  </ul>
  
  <h2 id="acerca-del-proyecto">Acerca del Proyecto</h2>
  <p>Este proyecto consiste en una aplicación web desarrollada con Streamlit que permite quitar el fondo de una imagen y redimensionarla según las especificaciones de SUNEDU (Superintendencia Nacional de Educación Universitaria). La herramienta facilita a los usuarios la eliminación del fondo de una foto de manera rápida y sencilla, así como también la posibilidad de subir una carpeta o varios archivos de imágenes a la aplicación para procesarlos en lotes. Además, los usuarios podrán descargarlas con el fondo eliminado y redimensionado, ya sea de forma individual o en un archivo comprimido (.zip) en caso de haber subido múltiples imágenes..</p>
  
  <h2 id="características">Características</h2>
  <ul>
    <li>Soporte para cargar una o varias imágenes a la vez.</li>
    <li>Posibilidad de cargar una carpeta completa.</li>
    <li>Eliminación del fondo de las imágenes cargadas.</li>
    <li>Redimensionamiento de las imágenes resultantes.</li>
    <li>Descarga individual de las imágenes resultantes.</li>
    <li>Descarga de un archivo ZIP con todas las imágenes resultantes cuando se cargan varias imágenes.</li>
  </ul>
  
  <h2 id="instalación">Instalación</h2>

<h3>Ejecución con Docker</h3>

<ol>
  <li>Asegúrate de tener Docker instalado en tu máquina. Puedes descargar e instalar Docker Desktop desde <a href="https://www.docker.com/products/docker-desktop">el sitio web oficial de Docker</a>.</li>
  
  <li>Clona este repositorio en tu máquina:</li>
  
  <pre><code>git clone https://github.com/tu_usuario/proyecto-eliminacion-fondo-imagenes.git
cd proyecto-eliminacion-fondo-imagenes
  </code></pre>
  
  <li>Construye la imagen de Docker ejecutando el siguiente comando en la raíz del proyecto:</li>
  
  <pre><code>docker build -t eliminacion-fondo-imagenes .
  </code></pre>
  
  <p>Este comando construirá una imagen de Docker llamada <code>eliminacion-fondo-imagenes</code> que contiene la aplicación.</p>
  
  <li>Ejecuta el contenedor Docker con el siguiente comando:</li>
  
  <pre><code>docker run -p 8501:8501 eliminacion-fondo-imagenes
  </code></pre>
  
  <p>Esto iniciará el contenedor Docker y la aplicación estará disponible en tu navegador web en la dirección <code>http://localhost:8501</code>.</p>
</ol>

  
  <h2 id="cómo-usar">Cómo Usar</h2>
  <p>Después de ejecutar la aplicación, simplemente carga una imagen desde tu dispositivo o selecciona una carpeta que contenga imágenes. La aplicación eliminará automáticamente el fondo de las imágenes cargadas y te permitirá descargar el resultado.</p>
  
  <h2 id="contribuir">Contribuir</h2>
  <p>¡Si te interesa contribuir al proyecto, estás más que bienvenido! Puedes:</p>
  <ul>
    <li>Reportar problemas o sugerir nuevas características creando un <a href="https://github.com/tu_usuario/proyecto-eliminacion-fondo-imagenes/issues">issue</a>.</li>
    <li>Enviar propuestas de mejora a través de un <a href="https://github.com/tu_usuario/proyecto-eliminacion-fondo-imagenes/pulls">pull request</a>.</li>
    <li>Ayudar a mejorar la documentación.</li>
    <li>Compartir la aplicación con otros.</li>
  </ul>
  
  <h2 id="autores">Autores</h2>
  <p>Este proyecto fue desarrollado por:</p>
  <ul>
    <li>Daniel Campana</li>
    <li>Joaquín Pozo</li>
    <li>Natalia Escudero</li>
    <li>Angela Anhuamán</li>
  </ul>
