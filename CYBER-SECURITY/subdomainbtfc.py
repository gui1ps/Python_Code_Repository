import dns.resolver


arquivo=open('SUB.txt')
conteudo=arquivo.read()
subdomains=conteudo.splitlines()
dom=input("Dominio: ")
listabtfc=[]
checkallbtfc=[]
res= dns.resolver.Resolver()


for sub in subdomains:
    completedomain='{x}.{y}'.format(x=sub, y=dom)
    listabtfc.append(completedomain)

for btf in listabtfc:

    try:
        resultado=res.resolve(btf,"A")
        for ip in resultado:
            print(btf,'->',ip)
            checkallbtfc.append([btf,ip])
    except:
        pass

