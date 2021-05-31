import random
lambetazo = ["queridos ", "apreciados ", "distinguidos ", "honorables ", "estimados ", "respetados "]
select_lambetazo = random.choice(lambetazo)

marranos = ["compatriotas", "conciudadanos", "amigos", "coterráneos", "copartidarios", "electores"]
select_marranos = random.choice(marranos)

condicion = ["en mi gobierno ", "con su apoyo ", "siendo elegido ", "con su ayuda ", "si me siguen ", "durante mi mandato "]
select_condicion = random.choice(condicion)

compromiso = ["voy a derrotar ", "venceré ", "eliminaré ", "acabaré ", "lucharé contra ", "combatiré "]
select_compromiso = random.choice(compromiso)

ilusion = ["la violencia y ", "la delincuencia y ", "la corrupción y ", "la inflación y ", "la pobreza y ", " el desplazamiento y "]
select_ilusion = random.choice(ilusion)

promesa = ["trabajaré por ", "garantizaré ", "protegeré ", "velaré por ", "promoveré ", "defenderé "]
select_promesa = random.choice(promesa)

beneficio = ["la educación ", "el empleo ", "la seguridad ", "la paz ", "la igualdad ", "la salud "]
select_beneficio = random.choice(beneficio)

cantidad = ["del país", "de la ciudad", "de la comunidad", "de la población", "para toda la gente", "de cada colombiano"]
select_cantidad = random.choice(cantidad)

print("Buenos días, " + select_lambetazo + select_marranos + ". Quiero recordarles que " + select_condicion + select_compromiso + select_ilusion + select_promesa + select_beneficio + select_cantidad + ".")

alianza = ["De la mano de", "Con el apoyo de", "Aprovechando la experiencia de", "En estrecha relación con el equipo de", "En unión con el equipo de"]
select_alianza = random.choice(alianza)

politiquera = ["senadora", "gobernadora", "representante", "ministra", "canciller", "vicepresidenta"]
select_politiquera = random.choice(politiquera)

politiquero = ["senador", "gobernador", "representante", "ministro", "canciller", "vicepresidente"]
select_politiquero = random.choice(politiquero)

apellido = ["Fernández", "Duque", "Arce", "Lasso", "Benítez"]
select_apellido = random.choice(apellido)

accion = ["salvaremos el país", "apagaremos todos estos incendios", "alejaremos al país de los extremos", "libertaremos la patria", "arreglaremos los errores del pasado", "venceremos al castrochavismo"]
select_accion = random.choice(accion)

eslogan = ["Todos unidos por Colombia", "Colombia se respeta", "A salvar a Colombia", "Hoy por Colombia, mañana por Colombia", "Pie plano, pulmón diminuto", "Colombia, ni un paso adelante"]
select_eslogan = random.choice(eslogan)

generof = (" la ")
generom = ("l ")

x = random.randint(0,101)

if x>50:
    print(select_alianza + generof + select_politiquera + " " + select_apellido + " " + select_accion + ". " + "¡" + select_eslogan + "!" + ".")
else:
    print(select_alianza + generom + select_politiquero + " " + select_apellido + " " + select_accion + ". " + "¡" + select_eslogan + "!" + ".")

grupo = ["el Comité", "el Movimiento", "el Partido", "la Alianza", "la Asamblea", "la Asociación"]
select_grupo = random.choice(grupo)

causa = ["de los pueblos", "Jesucristo Candidato", "Colombia es grande", "de la unión solidaria", "de ciudadanos enfurecidos", "de Fascistas Felices", "por el futuro de los niños"]
select_causa = random.choice(causa)

print("Mensaje pagado por " + select_grupo + " " + select_causa + ".")
