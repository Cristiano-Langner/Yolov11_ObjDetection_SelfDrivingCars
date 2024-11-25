import cv2
import random
import os

def extract_random_frames(video_path, output_folder, num_frames):
    """
    Extrai frames aleatórios de um vídeo e salva em uma pasta especificada.

    :param video_path: Caminho para o arquivo de vídeo.
    :param output_folder: Pasta onde os frames serão salvos.
    :param num_frames: Número de frames aleatórios a extrair.
    """
    # Abrir o vídeo
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError("Não foi possível abrir o vídeo.")

    # Obter número total de frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if num_frames > total_frames:
        raise ValueError("O número de frames solicitados excede o total de frames do vídeo.")

    # Criar a pasta de saída, se não existir
    os.makedirs(output_folder, exist_ok=True)

    # Gerar índices de frames aleatórios
    random_indices = random.sample(range(total_frames), num_frames)

    for idx in random_indices:
        # Ir para o frame específico
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)

        # Ler o frame
        ret, frame = cap.read()
        if not ret:
            print(f"Não foi possível ler o frame {idx}. Pulando.")
            continue

        # Salvar o frame como imagem
        frame_filename = os.path.join(output_folder, f"frame_{idx}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Frame {idx} salvo em {frame_filename}")

    # Liberar o vídeo
    cap.release()
    print("Extração concluída.")


if __name__ == "__main__":

    video_path = "20241119_081030.mp4"  
    output_folder = video_path.split('.')[0] + '_rand_frames/'  
    num_frames = 1500  # Número de frames aleatórios a extrair

    extract_random_frames(video_path, output_folder, num_frames)
