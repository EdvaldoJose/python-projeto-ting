def exists_word(word, instance):
    occurrences = []
    for i in range(len(instance)):
        item = instance.search(i)
        for index, linha in enumerate(item['linhas_do_arquivo']):
            if word.lower() in linha.lower():
                occurrences.append({'linha': index + 1})
    if occurrences:
        occurrences = [
            {'palavra': word,
             'arquivo': item['nome_do_arquivo'],
             'ocorrencias': occurrences}
        ]
    return occurrences


def search_by_word(word, instance):
    returned_list = []

    for index in range(len(instance)):
        search_word = instance.search(index)
        word_info = {
            "palavra": word,
            "arquivo": search_word['nome_do_arquivo'],
            "ocorrencias": []
        }

        for line_pos, line in enumerate(search_word['linhas_do_arquivo']):
            if word.lower() in line.lower():
                word_info['ocorrencias'].append({
                    "linha": line_pos + 1,
                    "conteudo": line,
                })

        if word_info['ocorrencias']:
            returned_list.append(word_info)

    return returned_list
