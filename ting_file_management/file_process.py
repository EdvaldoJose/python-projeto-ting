import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)

    if instance and instance.items:
        if instance.items[0]["nome_do_arquivo"] == path_file:
            return None

    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    instance.enqueue(info)
    print(str(info), file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return None

    file = instance.dequeue()
    print(
        f"Arquivo {file['nome_do_arquivo']} removido com sucesso",
        file=sys.stdout
        )


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(f"{file}", file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
