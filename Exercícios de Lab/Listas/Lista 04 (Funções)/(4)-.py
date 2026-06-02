BD = {
    1223224: {
        "Nome":"Lucas",
        "Curso":"SI"

    },
    2346765: {
        "Nome": "Claudia",
        "Curso": "SI"
    }
}

def add_aluno(BD,matricula,nome,curso):
    if matricula in BD:
        return False
    BD[matricula] = {
        "Nome":nome,
        "Curso": curso
    }
    return True

def buscar(BD,matricula):
    if matricula in BD:
        aluno = BD[matricula]
        return (aluno["nome"],aluno["Curso"])
    else:
        return (None,None)


