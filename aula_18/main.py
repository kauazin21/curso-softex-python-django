from escola import Escola
from estudante import Estudante

escola = Escola("Escola Softex")
aluno_1 = Estudante("Kauã",15, "2020")
aluno_2 = Estudante("Maria",11, "2022")

aluno_1.add_nota_materia("Matemática", 9.0)
aluno_1.add_nota_materia("Matemática", 8.5)
aluno_1.add_nota_materia("Português", 7.5)

aluno_2.add_nota_materia("Matemática", 6.0)
aluno_2.add_nota_materia("História", 9.0)

escola.add_estudante(aluno_1)
escola.add_estudante(aluno_2)

escola.mostrar_relatorio()