def Reconocimiento(game):    
    import cv2                  
    import mediapipe as mp  
    import pyautogui
    
    #Definir teclas del teclaso
    a_estado=False  
    d_estado=False
    s_estado=10
    w_estado=False 
    SS_estado = False
    R_estado = False

    
    ### Funciones ###
    def controles_Mario(lmList, a_estado, d_estado, SS_estado, w_estado):
        # Determinar si el pulgar está levantado
        if lmList[4][1] > lmList[3][1] and lmList[4][2] > lmList[9][2] and lmList[4][1] != lmList[6][1]:
            if not a_estado: 
                pyautogui.keyDown("left")
                a_estado = True
        else:
            if a_estado:
                pyautogui.keyUp("left")
                a_estado = False
            
        if lmList[20][2] < lmList[18][2]:
            if not d_estado:
                pyautogui.keyDown("right")
                d_estado = True
        else:
            if d_estado:
                pyautogui.keyUp("right")
                d_estado = False

        if lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2]: 
            if not SS_estado: 
                pyautogui.keyDown("down")
                SS_estado = True
        else:
            if SS_estado:
                pyautogui.keyUp("down")
                SS_estado = False
            else:
                if lmList[8][2] < lmList[6][2] and lmList[12][2] > lmList[10][2]:
                    if not w_estado:
                        pyautogui.keyDown("up")
                        w_estado = True
                else:
                    if w_estado:
                        pyautogui.keyUp("up")
                        w_estado = False

        return a_estado, d_estado, SS_estado, w_estado         

    def controles_snake(lmList, a_estado,d_estado,w_estado,SS_estado,R_estado):
        
        if lmList[4][1] > lmList[3][1] and lmList[4][2] > lmList[9][2] and lmList[4][1] != lmList[6][1]:
            if not a_estado:
                pyautogui.keyDown("left")
                pyautogui.keyUp("left")
                a_estado = True
        else:
            if a_estado:
                pyautogui.keyUp("left")
                a_estado = False

        if lmList[20][2] < lmList[18][2]:
            if not d_estado:
                pyautogui.keyDown("right")
                pyautogui.keyUp("right")
                d_estado = True
        else:
            if d_estado:
                pyautogui.keyUp("right")
                d_estado = False

        if lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2]:
            if not SS_estado: 
                pyautogui.keyDown("down")
                pyautogui.keyUp("down")
                SS_estado = True
        else:
            if SS_estado:
                pyautogui.keyUp("down")
                SS_estado = False
            else:
                if lmList[8][2] < lmList[6][2] and lmList[12][2] > lmList[10][2]:
                    if not w_estado:
                        pyautogui.keyDown("up")
                        pyautogui.keyUp("up")
                        w_estado = True
                else:
                    if w_estado:
                        pyautogui.keyUp("up")
                        w_estado = False

        return a_estado,d_estado,w_estado,SS_estado,R_estado
                    
    def controles_Tetris(lmList, a_estado, d_estado, s_estado, w_estado):
        # Determinar si el pulgar está levantado
        if lmList[4][1] > lmList[3][1] and lmList[4][2] > lmList[9][2] and lmList[4][1] != lmList[6][1]:
            if not a_estado:
                pyautogui.keyDown("left")
                pyautogui.keyUp("left")
                a_estado = True
        else:
            if a_estado:
                pyautogui.keyUp("left")
                a_estado = False
            
        if lmList[20][2] < lmList[18][2]:
            if not d_estado:
                pyautogui.keyDown("right")
                pyautogui.keyUp("right")
                d_estado = True
        else:
            if d_estado:
                pyautogui.keyUp("right")
                d_estado = False

        if lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2] :
            if not w_estado: 
                pyautogui.keyDown("up")
                pyautogui.keyUp("up")
                w_estado = True
        else:
            if w_estado:
                w_estado = False
            if lmList[8][2] < lmList[7][2] and lmList[12][2] > lmList[10][2]:
                if s_estado > 0:
                    s_estado -= 1
                if s_estado == 0:
                    pyautogui.keyDown("down")
                    s_estado = 10
            else:
                if s_estado:
                    pyautogui.keyUp("down")
                    s_estado = 10

        return a_estado, d_estado, s_estado, w_estado
 
    # Configuraciones para dibujar en la imagen
    mp_draw = mp.solutions.drawing_utils
    mp_hand = mp.solutions.hands

    #id de las punta de los Dedos de la mano
    tipIds = [4, 8, 12, 16, 20]

    video = cv2.VideoCapture(0)


    # Configuración del objeto de detección de manos
    with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1) as hands:
        while True:

            ret, image = video.read()    # Lectura de un frame del video
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    # Conversión de la imagen de BGR a RGB
            image.flags.writeable = False 
            results = hands.process(image)    # Detección y seguimiento de las manos en la imagen
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)    # Conversión de la imagen de RGB a BGR
            lmList = []    # Lista de landmarks de las manos detectadas

            if results.multi_hand_landmarks:    # Si se han detectado manos en la imagen
                for hand_landmark in results.multi_hand_landmarks:    # Para cada mano detectada
                    myHands = results.multi_hand_landmarks[0]    # Obtiene los landmarks de la mano
                    for id, lm in enumerate(myHands.landmark):    # Para cada landmark de la mano
                        h, w, c = image.shape    # Obtiene las dimensiones de la imagen
                        cx, cy = int(lm.x * w), int(lm.y * h)    # Convierte la posición normalizada del landmark a píxeles
                        lmList.append([id, cx, cy])    # Agrega el landmark a la lista 
                    mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)    # Dibuja los landmarks y conexiones en la imagen
            #print(lmList)
            
                if game == "TETRIS":
                    a_estado, d_estado, s_estado, w_estado = controles_Tetris(lmList, a_estado, d_estado, s_estado, w_estado)
                if game == "SNAKE":
                    a_estado, d_estado, w_estado ,SS_estado, R_estado = controles_snake(lmList,a_estado, d_estado, w_estado ,SS_estado, R_estado)
                if game == "MARIO":
                    a_estado, d_estado, SS_estado, w_estado = controles_Mario(lmList, a_estado, d_estado, SS_estado, w_estado)
            # Mostramos la imagen resultante
            cv2.imshow("Frame",image)
            
                
            # Esperamos la pulsación de la tecla 'q' para salir
            if cv2.waitKey(1) == 27:
                break

    # Liberamos la cámara y cerramos todas las ventanas
    video.release()
    cv2.destroyAllWindows()

#Reconocimiento("MARIO")