"""Modulo de envio de micro-reconhecimentos do SGER."""

from datetime import datetime


def enviar_reconhecimento(remetente, destinatario, badge, mensagem=""):
    """Registra o envio de um badge de reconhecimento entre colaboradores."""
    if remetente == destinatario:
        raise ValueError("Nao e permitido enviar reconhecimento para si mesmo.")
    return {
        "remetente": remetente,
        "destinatario": destinatario,
        "badge": badge,
        "mensagem": mensagem,
        "data": datetime.now().isoformat(timespec="seconds"),
    }


if __name__ == "__main__":
    print(enviar_reconhecimento("yan", "marcos", "Problema Resolvido!"))
