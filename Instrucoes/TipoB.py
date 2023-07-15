# Classe Tipo B
from Instrucoes.Instrucao import Instrucao

functs3 = {
    "beq"   : "000",
    "bne"   : "001",
    "blt"   : "100",
    "bge"   : "101",
    "bltu"  : "110",
    "bgeu"  : "111",
}


class TipoB(Instrucao):
    def __init__(self, texto):
        super().__init__(texto)

        self.mneumonico = super().get_mnemonico()
        self.rs2_nome = super().get_primeiro_reg()
        self.rs1_nome = super().get_segundo_reg()

        self.imm = super().get_imm_ou_reg()

        if (not ((self.imm).isdigit())):
            raise ValueError("Esperado um valor imediato inteiro!")

        if (int(self.imm) > 4095 or int(self.imm) < -4095):
            raise ValueError("Esperado um valor que pode ser representado com 12 bits!")

    def get_registradores(self):

        # Conversao do registrador origem 1 (rs1)
        rs1 = super().regParaBin(self.rs1_nome)

        # Conversao do regristrador origem 2 (rs2)
        rs2 = super().regParaBin(self.rs2_nome)

        return (rs1, rs2)

    def get_imediato(self):
        # Convertendo o valor imediato para binário
        return bin(int(self.imm))[2:].zfill(12)

    def __str__(self):
        rs1, rs2 = self.get_registradores()

        opcode = "1100011"

        funct3 = functs3[self.mneumonico]

        imm = self.get_imediato()

        codigo_inteiro = f'{imm[0]} {imm[-10:-5]} {rs2} {rs1} {funct3} {imm[-4:]} {imm[1]} {opcode}'

        return ('opcode: ' + opcode + '\n' +
                'rs1: ' + rs1 + '\n' +
                'rs2: ' + rs2 + '\n' +
                'imm: ' + imm + '\n\n' +
                'Binário: ' + codigo_inteiro + '\n')
