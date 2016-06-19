#Gestionando Campos de Enlace Dinámico

Un campo de Enlace Dinámico permite buscar y retener un valor desde cualquier documento/doctype. Considere el siguiente ejemplo para aprender como funciona este tipo de campos.

Mientras se crea una Oportunidad o Cotización, se debe definir de manera explícita si es para un Líder o para un Cliente. Basado en la selección (Líder/Cliente), otro campo enlazado se mostrará para poder seleccionar un determinado Líder (o Cliente).  

El campo donde se selecciona si es Líder o Cliente debe ser del tipo Enlace Dinámico y el campo emergente deberá enlazarse al maestro seleccionado en el primer campo. Por tanto, no es necesario insertar enlaces separados para los Clientes y los Líderes.

A continuación se presentan los pasos para insertar un campo personalizado de tipo Enlace Dinámico. Por ejemplo: para insertar un campo de Enlace Dinámico en el documento de Ingreso Diario.

#### Paso 1: Insertar un campo tipo Enlace para seleccionar un Doctype

Crear un campo tipo enlace. En la sección de Opción escribir Doctype.

<img alt="Custom Link Field" class="screenshot" src="{{docs_base_url}}/assets/img/articles/dynamic-field-1.gif">

El **Doctype** mencionado en el campo de opción hace referencia al doctype padre.Es decir, enlaza a un Doctype que tiene todos los registros de los doctypes creados en la aplicación.
 
-- Doctype<br>
---- Orden de Venta<br>
---- Factura de Compra<br>
---- Cotización<br>
---- Factura de Venta<br>
---- Empleado<br>
---- Orden de Producción<br>
.. y otros...

<img alt="journal Voucher Link Field" class="screenshot" src="{{docs_base_url}}/assets/img/articles/dynamic-field-2.png">

#### Paso 2: Insertar un campo de Enlace Dinámico

Agregar un campo del tipo "Enlace Dinámico". En el campo Opción colocar el nombre del campo anteriormente creado.

<img alt="Custom Dynamic Field" class="screenshot" src="{{docs_base_url}}/assets/img/articles/dynamic-field-3.gif">

Este campo permitirá seleccionar el id del documento, basado en el valor seleccionado en el campo enlazado. Por ejemplo: si se selecciona Órden de Venta en el campo anterior, este campo mostrará los id de las Órdenes de Venta.

<img alt="Custom Dynamic Field" class="screenshot" src="{{docs_base_url}}/assets/img/articles/dynamic-field-4.gif">

<div class="well">

**Personalizar las opciones en el campo tipo Enlace**

De manera predeterminada, el campo tipo Enlace proveerá todos los formularios/doctypes para hacer la selección. Si solo se requiere mostrar un determinado conjunto de ellos se deberá escribir Scripts Personlazados.
</div>

<!-- markdown -->
