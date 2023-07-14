# Classe Tipo I
from Instrucoes.Instrucao import Instrucao

class TipoJ(Instrucao):
    def __init__(self, texto):
        super().__init__(texto)

        self.mneumonico = super().get_mnemonico()
        self.imm = super().get_unico_imm()


        if (not ((self.imm).isdigit())):
            raise TypeError("Esperado um valor imediato inteiro!")

        if (int(self.imm) > 524287 or int(self.imm) < -524288):
            raise ValueError("Esperado um valor que pode ser representado com 20 bits!")

    def get_imediato(self):
        # Convertendo o valor imediato para binário
        return bin(int(self.imm))[2:].zfill(20)

    def __str__(self):
        rd = '00001' # Na instrucao jump o rd eh sempre o ra

        opcode = '1101111'

        imm = self.get_imediato()

        codigo_inteiro = f'{imm[19]} {imm[0:10][::-1]} {imm[10]} {imm[11:19][::-1]} {rd} {opcode}'

        return ('opcode: ' + opcode + '\n' +
                'rd: ' + rd + '\n' +
                'imm: ' + imm + '\n\n' +
                'Binário: ' + codigo_inteiro + '\n')
