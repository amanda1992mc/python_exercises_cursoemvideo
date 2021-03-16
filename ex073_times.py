tupla = ('Athletico-PR', 'Atlético - GO', 'Atlético - MG', 'Bahia - BA', 'Botafogo - RJ',
         'Bragantino - SP', 'Ceará - CE','Corinthians - SP', 'Coritiba - PR', 'Flamengo - RJ',
         'Fluminense - RJ', 'Fortaleza - CE', 'Goiás - GO', 'Grêmio - RS', 'Internacional - RS',
         'Palmeiras - SP', 'Santos - SP', 'São Paulo - SP', 'Sport - PE', 'Vasco da Gama - RJ')

print(f"Lista de times: \n {tupla}\n")

print(f"Os cinco primeiros colocados são: {tupla[:5]} \n")

print(f"Os quatro últimos colocados são: {tupla[-4:]}\n")

print(f"Os times em ordem alfabética: {sorted(tupla)}\n")

print(f"O São Paulo se encontra na {tupla.index('São Paulo - SP')+1}ª posição.\n")