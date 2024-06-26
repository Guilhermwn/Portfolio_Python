exame = int(input())

if exame < 100:
    print("Colesterol LDL %.0f mg/dl: OTIMO" % exame)
elif exame >= 100 and exame < 130:
    print("Colesterol LDL %.0f mg/dl: DESEJAVEL" % exame)
elif exame >=  130 and exame < 160:
    print("Colesterol LDL %.0f mg/dl: LIMITROFE" % exame)
elif exame >= 160 and exame < 190:
    print("Colesterol LDL %.0f mg/dl: ALTO \nProcure um medico" % exame)
elif exame >= 190:
    print("Colesterol LDL %.0f mg/dl: MUITO ALTO \nProcure um medico" % exame)