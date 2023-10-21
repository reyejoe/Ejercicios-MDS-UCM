
def obscurecer_palabra(palabra, acertado):
    rv = ''
    for s in palabra:
        if s not in acertado:
            rv = rv+'_'
        else:
            rv = rv+s
    return rv