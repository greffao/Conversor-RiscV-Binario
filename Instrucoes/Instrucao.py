# Classe base de instruca
registradores = {
    'x0': '00000',
    'x1': '00001',
    'x2': '00010',
    'x3': '00011',
    'x4': '00100',
    'x5': '00101',
    'x6': '00110',
    'x7': '00111',
    'x8': '01000',
    'x9': '01001',
    'x10': '01010',
    'x11': '01011',
    'x12': '01100',
    'x13': '01101',
    'x14': '01110',
    'x15': '01111',
    'x16': '10000',
    'x17': '10001',
    'x18': '10010',
    'x19': '10011',
    'x20': '10100',
    'x21': '10101',
    'x22': '10110',
    'x23': '10111',
    'x24': '11000',
    'x25': '11001',
    'x26': '11010',
    'x27': '11011',
    'x28': '11100',
    'x29': '11101',
    'x30': '11110',
    'x31': '11111',
    'zero': '00000',
    'ra': '00001',
    'sp': '00010',
    'gp': '00011',
    'tp': '00100',
    't0': '00101',
    't1': '00110',
    't2': '00111',
    's0': '01000',
    's1': '01001',
    'a0': '01010',
    'a1': '01011',
    'a2': '01100',
    'a3': '01101',
    'a4': '01110',
    'a5': '01111',
    'a6': '10000',
    'a7': '10001',
    's2': '10010',
    's3': '10011',
    's4': '10100',
    's5': '10101',
    's6': '10110',
    's7': '10111',
    's8': '11000',
    's9': '11001',
    's10': '11010',
    's11': '11011',
    't3': '11100',
    't4': '11101',
    't5': '11110',
    't6': '11111'
}

class Instrucao:

    # Construtor
    def __init__(self, texto):
        self.instrucao = texto

    def get_partes(self):
        return (self.instrucao).split(",")

    def get_mnemonico(self):
        partes = list(map(str.strip, self.get_partes()))

        return (partes[0].split(" "))[0]
    
    def get_primeiro_reg(self):
        partes = list(map(str.strip, self.get_partes()))

        return partes[0].split(" ")[1]
    
    def get_segundo_reg(self):
        return (self.get_partes()[1]).strip()   

    def get_offset(self):
        partes = list(map(str.strip, (self.instrucao).split("(")))
        
        return partes[0].split(",")[1].strip()
    
    def get_base_reg(self):
        partes = list(map(str.strip, (self.instrucao).split("(")))

        return partes[1][:-1]

    def get_imm_ou_reg(self):
        return (self.get_partes()[2]).strip() 

    def regParaBin(self, reg):
        print("Recebido:" + reg)
        try:
            valor = registradores[reg]
            return valor
        except KeyError:
            return 'ERRO'
