 lista.append({"used": evento.flageado,"id":evento.id, "start":start, "end":end, "title":usuarioObj.nombre+" "+usuarioObj.apellido1 ,"body":" ", "multi":0 ,"allDay":False, "extension_id":2})
                data = json.dumps(lista)




                from django.db.models import Count
				data = Usuario.objects.values("jefatura").annotate(cantidad=Count("jefatura")
                resultado = [[x.jefatura,x.cantidad] for x in data]

                len(Usuario.objects.filter(edad__gte=10, edad__lte=30))




                if (usuarioObj.estamento == 5):  
                #CALCULO DE HORAS PARA SECUNDARIA
                suma += delta.seconds / 55 / 55 / 0.75 #se divide por 55 por que los bloques son de 55 minutos, y equivalen a 1 hora // formula aplicable a las horas frente a alumnos
                deltag = delta.seconds / 55 / 55 / 0.75
                deltas.append(round(deltag,2))

            	if (usuarioObj.estamento == 2 or usuarioObj.estamento == 3):
                #CALCULO DE HORAS PARA PRIMARIA
                suma += delta.seconds / 45 / 45 / 0.75 #se divide por 45 por que los bloques son de 45 minutos, y equivalen a 1 hora // formula aplicable a las horas frente a alumnos
                deltag = delta.seconds / 45 / 45 / 0.75
                deltas.append(round(deltag,2))  


                class AccountFormSet(forms.ModelForm)
                	class Meta:
       				model = Account #si es que asi se llama el modelo
      				exclude = [" aqui colocas los campos del modelo que quieres excluir separado por coma"]         

      				<div class="col-xs-6">
                   <label for="filtro">{{ filtro.form.account.label }}:</label>
                   <select class="form-control" >
                       <option>{{ filtro.form.account }}</option>
                   </select>


      if not from_date in request.GET:                   
        from_date = datetime.date(request.GET.get('from'))
        to_date = datetime.date(request.GET.get('to')) 
   
       for m in mov_list:
           if (m.date >= from_date  and m.date <= to_date ):

            DELETE FROM  `cal`.`edt_evento` WHERE  `edt_evento`.`usuario_id` = 



----------------------------------------------------------------------------------------------

objeto = Clase.objects.get(id=1)
objeto.titulo = "nuevo titulo"
objeto.save()


if  usuarioObj.rol.id != 2:
        #permiso =  Permiso.objects.all().order_by("-fecha_creacion")
        #IMPORTANTE: el codigo siguiente crea un campo virtual y luego cuenta cuantas resoluciones tiene asociadas y si el contador es mayor a cero no lo toma en cuenta 
        permiso = Permiso.objects.annotate(num_b=Count('bitacora')).filter(num_b=0).order_by("-fecha_creacion")

        paginator = Paginator(permiso,10) 
        
        try: pagina = int(request.GET.get("page",'1'))
        except ValueError: pagina = 1
            
        try:
            permiso = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            permiso = paginator.page(paginator.num_pages)   
            
        return render_to_response("edt/permisolst.html",{"permiso": permiso,"usuario" : usuarioObj,"permisoObj_list" : permiso.object_list,"months" : mkmonth_lst()})

    else:
        #if     usuarioObj.username == request.session['usuario']:
        if  usuarioObj.rol.id == 2:
            permiso = Permiso.objects.annotate(num_b=Count('resolucion')).filter(usuario=usuarioObj.id).order_by("-fecha_creacion")
            

            paginator = Paginator(permiso,10)       
            try: pagina = int(request.GET.get("page",'1'))
            except ValueError: pagina = 1       
            try:
                permiso = paginator.page(pagina)
            except (InvalidPage, EmptyPage):
                permiso = paginator.page(paginator.num_pages)


            
        return render_to_response("edt/permisolst.html",{"permiso": permiso,"usuario" : usuarioObj,"permisoObj_list" : permiso.object_list,"months" : mkmonth_lst()})
