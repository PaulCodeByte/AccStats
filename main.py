import json

macchine_acc = {
    0: 'Porsche 991 GT3 R',
    1: 'Mercedes-AMG GT3',
    2: 'Ferrari 488 GT3',
    3: 'Audi R8 LMS',
    4: 'Lamborghini Huracan GT3',
    5: 'McLaren 650S GT3',
    6: 'Nissan GT-R Nismo GT3 2018',
    7: 'BMW M6 GT3',
    8: 'Bentley Continental GT3 2018',
    9: 'Porsche 991II GT3 Cup',
    10: 'Nissan GT-R Nismo GT3 2017',
    11: 'Bentley Continental GT3 2016',
    12: 'Aston Martin V12 Vantage GT3',
    13: 'Lamborghini Gallardo R-EX',
    14: 'Jaguar G3',
    15: 'Lexus RC F GT3',
    16: 'Lamborghini Huracan Evo (2019)',
    17: 'Honda NSX GT3',
    18: 'Lamborghini Huracan SuperTrofeo',
    19: 'Audi R8 LMS Evo (2019)',
    20: 'AMR V8 Vantage (2019)',
    21: 'Honda NSX Evo (2019)',
    22: 'McLaren 720S GT3 (2019)',
    23: 'Porsche 911II GT3 R (2019)',
    24: 'Ferrari 488 GT3 Evo 2020',
    25: 'Mercedes-AMG GT3 2020',
    26: 'Ferrari 488 Challenge Evo',
    27: 'BMW M2 CS Racing',
    28: 'Porsche 911 GT3 Cup (Type 992)',
    29: 'Lamborghini Huracán Super Trofeo EVO2',
    30: 'BMW M4 GT3',
    31: 'Audi R8 LMS GT3 evo II',
    32: 'Ferrari 296 GT3',
    33: 'Lamborghini Huracan Evo2',
    34: 'Porsche 992 GT3 R',
    35: 'McLaren 720S GT3 Evo 2023',
    36: 'Ford Mustang GT3',
    50: 'Alpine A110 GT4',
    51: 'AMR V8 Vantage GT4',
    52: 'Audi R8 LMS GT4',
    53: 'BMW M4 GT4',
    55: 'Chevrolet Camaro GT4',
    56: 'Ginetta G55 GT4',
    57: 'KTM X-Bow GT4',
    58: 'Maserati MC GT4',
    59: 'McLaren 570S GT4',
    60: 'Mercedes-AMG GT4',
    61: 'Porsche 718 Cayman GT4',
    80: 'Audi R8 LMS GT2',
    82: 'KTM XBOW GT2',
    83: 'Maserati MC20 GT2',
    84: 'Mercedes AMG GT2',
    85: 'Porsche 911 GT2 RS CS Evo',
    86: 'Porsche 935'
}
piloti={

}

def laptime(time):
    time = int(time)
    if time == 2147483647:
        return 'Invalid'
    minuti = time // 60000
    secondi = (time % 60000) // 1000
    millisecondi = time % 1000
    return f'{minuti}:{secondi:02}:{millisecondi:03}'

class Pilota():

    def __init__(self, nome, numero, macchina, giro, penalita,id):
        self.nome=nome
        self.numero=numero
        self.macchina= macchina
        self.giro=giro
        self.penalita=penalita
        self.id=id

    def __str__(self):
        if self.penalita:
            return f'{self.nome}, N.{self.numero}, {self.macchina}, {self.giro}, {self.penalita}'
        return f'{self.nome}, N.{self.numero}, {self.macchina}, {self.giro}'

def stats(data):

    data = json.loads(data)

    for entry in data["sessionResult"]["leaderBoardLines"]:
        nome = entry["car"]["drivers"][0]["lastName"]
        numero = entry["car"]["raceNumber"]
        giro = laptime(entry["timing"]["bestLap"])
        macchina = macchine_acc[int(entry["car"]["carModel"])]
        id = int(entry["car"]["carId"])
        pilota= Pilota(nome, numero, macchina, giro, None,id)
        piloti[nome] = pilota

    for entry in data["penalties"]:
        id = int(entry['carId'])
        penalita = entry['penalty']

        for pilota in piloti:
            if piloti[pilota].id == id:
                piloti[pilota].penalita = penalita
    
    return piloti

for pilota in piloti:
    print(piloti[pilota])