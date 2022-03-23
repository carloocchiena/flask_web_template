def virtual(people, budget):
    if people < 100 and budget < 1000:
        people_a =  "Un evento di queste dimensioni si gestisce bene con Google Meet. Che tra l'altro, è anche adatto al tuo budget."
    elif people < 100 and budget > 1000:
        people_a =  "Un evento di queste dimensioni si gestisce bene con Google Meet. Siccome hai un po' di budget, lo userei per fare attività promozionale"
    elif people > 100 and budget < 1000:
        people_a = "Mi sembra un evento bello grande, ti consiglio la versione pro di Zoom. Dovresti farcela, anche con un budget ridotto!"
    else:
        people_a = "Mi sembra un evento bello grande, ti consiglio la versione pro di Zoom. Hai un ottimo budget per preparare un bell'evento!"
    '''
    questa parte al momento non la uso
    if budget < 100:
        budget_a = ""
    else:
        budget_a = "Usa un abbonamento"
    '''

    return people_a #+ budget_a
