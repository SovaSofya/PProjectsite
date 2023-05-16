from ruwordnet import RuWordNet

a = str(input())  # user's word


def pfication(get_word):  # to give us p-synonyms, p-antonyms, p-hyponyms and p-hupernyms
    wn = RuWordNet()  # creating a RuWordNet object to work with
    oursynsets = wn.get_synsets(get_word)  # synsets (rows of synonyms) for user's word
    if not oursynsets:
        print('no results found')
        pass

    synshyponyms = []  # these lists are for synsets picked up from ruwordnet based on one-or-another semantic relation
    synshypernyms = []
    synsantonyms = []
    psyno = []  # future filtered by the first letter "P" lists
    phypo = []
    phyper = []
    panto = []

    for synset in oursynsets:  # finding hyponym, hypernym, antonym synsets for each synset with user's word
        synshyponyms.append(synset.hyponyms)
        synshypernyms.append(synset.hypernyms)
        synsantonyms.append(synset.antonyms)
        for i in range(len(synset.senses) - 1):  # synonyms are basically other elements in user's word's synsets
            checklist = synset.senses[i].name.split()  # picking out definitions (without ids and the rest)
            k = 0
            for x in checklist:  # checking every synonym to see if it fits
                if x.lower() != get_word and x[0] == 'П':
                    k += 1
            if k == len(checklist) and synset.senses[i].name.lower() not in psyno:  # if every word in the synonym
                psyno.append(synset.senses[i].name.lower())  # starts with 'П' and haven't been marked as such before

#  Hyponyms and hypernyms are found likewise, next 2 cycles function in the same way as the previous one, but with
#  relevant lists

    for spisok in synshyponyms:
        for m in spisok:
            slova = m.senses
            for i in range(len(slova) - 1):
                checklist = slova[i].name.split()
                k = 0
                for x in checklist:
                    if x.lower() != get_word and x[0] == 'П':
                        k += 1
                if k == len(checklist) and slova[i].name.lower() not in phypo:
                    phypo.append(slova[i].name.lower())

    for spisok in synshypernyms:
        for m in spisok:
            # print(m.senses)
            slova = m.senses
            for i in range(len(slova) - 1):
                checklist = slova[i].name.split()
                k = 0
                for x in checklist:
                    if x.lower() != get_word and x[0] == 'П':
                        k += 1
                if k == len(checklist) and slova[i].name.lower() not in phyper:
                    phyper.append(slova[i].name.lower())

#  Antonyms are found almost in the same way, but we do not concern ourselves with finding antonyms that start with 'П':
#  we just find antonyms that consist of 1 word or, if more, have the rest or the words (except for the first one) and
#  add 'Противо-'

    for spisok in synsantonyms:
        for m in spisok:
            # print(m.senses)
            slova = m.senses
            for i in range(len(slova) - 1):
                checklist = slova[i].name.split()
                i = 0
                for x in range(1, len(checklist) - 1):
                    if checklist[x].lower()[0] != 'п':
                        i += 1
                if len(checklist) == 1 or i > 0:  # checking if antonym is suitable
                    k = 0
                    for x in checklist:
                        if x.lower() != get_word:
                            k += 1
                    if k == len(checklist) and slova[i].name.lower() not in panto:
                        panto.append(slova[i].name.lower())

    if len(psyno) == 0 and len(panto) == 0 and len(phypo) == 0 and len(phyper) == 0:  # in case if our try to compile
        return ["Плохо понимаемо, помощь противоподбирается :("]  # anything was o complete fail
        pass
    else:  # making up a pretty string for the output
        x = f"Похоже на {', '.join(psyno)}. " if len(psyno) != 0 else 'Похожее противоподобрано. '
        y = f"Поконкретнее, чем {', '.join(phyper)}. " if len(phyper) != 0 else 'Превышающее противоподобрано. '
        z = f"Пообщее, чем {', '.join(phypo)}. " if len(phypo) != 0 else 'Подвиды противоподобраны. '
        q1 = []
        for i in range(len(panto)):
            q1.append(f"противо{panto[i].lower()}")  # adding 'Противо' as said before
        that = ", ".join(q1)
        q = f"Похоже на {that}" if len(q1) != 0 else 'Противоположное противоподобрано. '

        return x, y, z, q


print(*pfication(a))
