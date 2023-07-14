# Classe Tipo I
from Instrucoes.Instrucao import Instrucao

opcodes = {
    "lui"   : "0110111",
    "auipc" : "0010111",
}
class TipoU(Instrucao):
    def __init__(self, texto):
        super().__init__(texto)

        self.mneumonico = super().get_mnemonico()
        self.rd_nome = super().get_primeiro_reg()
        self.imm = super().get_offset()

        print("imm: " + self.imm)
        if (not ((self.imm).isdigit())):
            raise TypeError("Esperado um valor imediato inteiro!")

        if (int(self.imm) > 524287 or int(self.imm) < -524288):
            raise ValueError("Esperado um valor que pode ser representado com 20 bits!")

    def get_imediato(self):
        # Convertendo o valor imediato para binário
        return bin(int(self.imm))[2:].zfill(20)

    def __str__(self):
        rd = super().regParaBin((self.rd_nome))
        print("rd: " + rd)
        opcode = opcodes[self.mneumonico]
        print("opcode: " + opcode)
        imm = self.get_imediato()
        print("imm: " + imm)
        codigo_inteiro = f'{imm[::-1]} {rd} {opcode}'

        return ('opcode: ' + opcode + '\n' +
                'rd: ' + rd + '\n' +
                'imm: ' + imm + '\n\n' +
                'Binário: ' + codigo_inteiro + '\n')
