import os
import shutil

pasta_organizadora = r"d:\Downloads"
tipos_de_arquivos = {
    "executáveis": [".exe", ".msi"],
    "imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "videos": [".mp4", ".mkv", ".avi", ".mov"],
    "audios": [".mp3", ".wav", ".flac"],
    "documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "fantome": [".FANTOME"],
    "zipados": [".zip"],
}
def organizar_arquivos(pasta):
    for arquivo in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_completo):
            _, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()

            
            destino = "Outros"
            for pasta_nome, extensoes in tipos_de_arquivos.items():
                if extensao in extensoes:
                    destino = pasta_nome
                    break

            pasta_destino = os.path.join(pasta, destino)
            os.makedirs(pasta_destino, exist_ok=True)

            shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))
            print(f"Movido: {arquivo} → {destino}/")

if __name__ == "__main__":
    organizar_arquivos(pasta_organizadora)