# Classe tipo R
from Instrucoes.Instrucao import Instrucao

functs3 = {
    'add' : "000", 
    'sub' : "000", 
    'sll' : "001", 
    'slt' : "010", 
    'sltu': "011",
    'xor' : "100", 
    'srl' : "101", 
    'sra' : "101",
    'or'  : "110", 
    'and' : "111" 
}

functs7 = {
    'add' : "0000000", 
    'sub' : "0100000", 
    'sll' : "0000000", 
    'slt' : "0000000", 
    'sltu': "0000000",
    'xor' : "0000000", 
    'srl' : "0000000", 
    'sra' : "0100000",
    'or'  : "0000000", 
    'and' : "0000000", 
}


class TipoR(Instrucao):
    def __init__(self, texto):
        super().__init__(texto)

        self.mneumonico = super().get_mnemonico()
        self.rd_nome = super().get_primeiro_reg()
        self.rs1_nome = super().get_segundo_reg()
        self.rs2_nome = super().get_imm_ou_reg()

    def get_registradores(self):
        # Conversao do registrador destido (rd)
        rd = super().regParaBin(self.rd_nome)

        # Conversao do registrador origem 1 (rs1)
        rs1 = super().regParaBin(self.rs1_nome)

        # Conversao do regristrador origem 2 (rs2)
        rs2 = super().regParaBin(self.rs2_nome)

        return (rd, rs1, rs2)


    def __str__(self):
        rd, rs1, rs2 = self.get_registradores()
        
        opcode = "0110011"

        funct3 = functs3[self.mneumonico]

        funct7 = functs7[self.mneumonico]

        codigo_inteiro = f'{funct7} {rs2} {rs1} {funct3} {rd} {opcode}'

        return ('opcode: ' + opcode + '\n' +
                'rd: ' + rd + '\n' +
                'funct3: '+ funct3 + '\n' +
                'rs1: ' + rs1 + '\n' +
                'rs2: ' + rs2 + '\n' +
                'funct7: ' + funct7 + '\n\n' +
                'Binário: ' + codigo_inteiro + '\n')