"""Nova funcionalidade: catalogo simples de badges do SGER."""

BADGES = ["Bom trabalho!", "Ajudou muito!", "Problema Resolvido!"]


def listar_badges():
    """Retorna os badges disponiveis para envio."""
    return list(BADGES)


if __name__ == "__main__":
    for i, badge in enumerate(listar_badges(), start=1):
        print(i, badge)
