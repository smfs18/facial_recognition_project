import cv2
import face_recognition as fr
import os

encodings = []
names = []

# -------------------------------
# Criar encodings das imagens
# -------------------------------
def createEncodings():
    for filename in os.listdir("pessoas"):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            path = os.path.join("pessoas", filename)

            img = fr.load_image_file(path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            face_encs = fr.face_encodings(img)
            if face_encs:
                encodings.append(face_encs[0])
                names.append(os.path.splitext(filename)[0])

    print(f"[INFO] {len(encodings)} rostos cadastrados.")

# -------------------------------
# Comparar faces pela webcam
# -------------------------------
def compareFaces():
    video = cv2.VideoCapture(0)

    if not video.isOpened():
        print("[ERRO] Não foi possível acessar a webcam.")
        return

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Reduz para ganhar performance
        frame_small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        frame_small = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)

        face_locations = fr.face_locations(frame_small)
        face_encodings = fr.face_encodings(frame_small, face_locations)

        for (y1, x2, y2, x1), face_encoding in zip(face_locations, face_encodings):
            # Ajusta escala
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

            # Compara com base conhecida
            matches = fr.compare_faces(encodings, face_encoding)
            name = "Desconhecido"

            if True in matches:
                index = matches.index(True)
                name = names[index]

            # Desenha retângulo
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Exibe nome
            cv2.putText(
                frame,
                name,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2
            )

        cv2.imshow("Reconhecimento Facial", frame)

        # ⛔ ESC para encerrar
        if cv2.waitKey(1) == 27:
            print("[INFO] Encerrando...")
            break

    video.release()
    cv2.destroyAllWindows()

# -------------------------------
# Execução
# -------------------------------
createEncodings()
compareFaces()
