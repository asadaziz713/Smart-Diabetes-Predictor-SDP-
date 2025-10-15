import pygame as p
p.init()

slidercolor = (139, 0, 0)
font_small = p.font.SysFont(None, 25)
barout = 1
option = 1
opt = 1
pred_active = 0
score = 0
age = 20
weight = 50
r = 100
query = 1
selected = 0
gd = p.display.set_mode((1100, 600))
def draw_gradient(surface, color_top, color_bottom):
    """Draw a vertical gradient background"""
    width, height = surface.get_size()
    for y in range(height):
        # Calculate blend ratio between top and bottom color
        ratio = y / height
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        p.draw.line(surface, (r, g, b), (0, y), (width, y))


def about():
    global selected, font_small
    gd.fill((220, 240, 255))  # Background color

    font_title = p.font.SysFont(None, 50)
    font_text = p.font.SysFont(None, 30)

    # --- Title ---
    title = font_title.render("About Smart Diabetes Predictor (SDP)", True, (0, 128, 0))
    gd.blit(title, (200, 50))

    # --- Description ---
    lines = [
        "SDP is a simple AI-inspired system designed to predict the diabetes risk level",
        "based on user-provided health and lifestyle information.",
        "It asks basic questions such as age, family history, exercise habits, and more,",
        "then calculates a total score to estimate Low, Moderate, or High Risk.",
        "",
        "Developed by: Team Hackstorm",
        "From: Sukkur IBA University",
        "",
        "Use arrow keys to navigate and Enter to select options.",
        "Press ESC or Backspace to return to the main menu."
    ]

    y = 120
    for line in lines:
        text = font_text.render(line, True, (0, 0, 0))
        gd.blit(text, (100, y))
        y += 40

    # --- Footer ---
    footer = font_small.render("Version 1.0 | © 2025 Smart Diabetes Predictor", True, (128, 0, 0))
    gd.blit(footer, (365, 520))

    p.display.update()


def menu(option):
    global font_small
    draw_gradient(gd, (255, 0, 40), (0, 204, 204))   
    font = p.font.SysFont(None, 30)
    if option == 1:
        p.draw.rect(gd, slidercolor, (420, 170, 260, 60), border_radius = 15)
    else:
        p.draw.rect(gd, (128, 0, 0), (420, 170, 260, 60), border_radius = 15)
        p.draw.rect(gd, (165, 42, 42), (425, 175, 250, 50), border_radius = 10)
    text = font.render("Start Analysing", True, (0, 0, 0))
    gd.blit(text, (470, 190))
    
    if option == 2:
        p.draw.rect(gd, slidercolor, (420, 245, 260, 60), border_radius = 15)
    else:
        p.draw.rect(gd, (128, 0, 0), (420, 245, 260, 60), border_radius = 15)
        p.draw.rect(gd, (165, 42, 42), (425, 250, 250, 50), border_radius = 10)
    text = font.render("About", True, (0, 0, 0))
    gd.blit(text, (513, 265))
    
    if option == 3:
        p.draw.rect(gd, slidercolor, (420, 320, 260, 60), border_radius = 15)
    else:
        p.draw.rect(gd, (128, 0, 0), (420, 320, 260, 60), border_radius = 15)
        p.draw.rect(gd, (165, 42, 42), (425, 325, 250, 50), border_radius = 10)
    text = font.render("Exit", True, (0, 0, 0))
    gd.blit(text, (520, 340))
    
    # --- Footer ---
    footer = font_small.render("Version 1.0 | © 2025 Smart Diabetes Predictor", True, (128, 0, 0))
    gd.blit(footer, (365, 520))

def prediction(score):
    global font_small, barout
    gd.fill((220,240,255))
    # --- Footer ---
    footer = font_small.render("Version 1.0 | © 2025 Smart Diabetes Predictor", True, (128, 0, 0))
    gd.blit(footer, (365, 520))
    
    font = p.font.SysFont(None, 40)
    out1 = font.render("Final Prediction", True, (255, 0, 0))
    gd.blit(out1, (400, 195))
    p.draw.rect(gd, (0, 255, 0), (400, 235, 100 * 3, 10), border_radius = 5)
    if barout == 1:
        for i in range(score):
            p.draw.rect(gd, (255, 0, 0), (400, 235, ((i / 17) * 100) * 3, 10), border_radius = 5)
            p.time.delay(100)
            q6 = font.render(f"{round(((score / 17) * 100), 2)}%", True, (0, 0, 0))
            gd.blit(q6, (400, 260))
            p.display.update()
    barout = 0
    p.draw.rect(gd, (255, 0, 0), (400, 235, ((score / 17) * 100) * 3, 10), border_radius = 5)
    p.time.delay(100)
    q6 = font.render(f"{round(((score / 17) * 100), 2)}%", True, (0, 0, 0))
    gd.blit(q6, (400, 260))
    if score <= 5:
        out1 = font.render("Low Risk", True, (255, 0, 0))
        gd.blit(out1, (400, 300))
    elif score > 5 and score <= 11:
        out1 = font.render("Moderate Risk", True, (255, 0, 0))
        gd.blit(out1, (400, 300))
    else:
        out1 = font.render("High Risk", True, (255, 0, 0))
        gd.blit(out1, (400, 300))
    
    
    p.display.update()
        

def queries(e = None):
    global barout, score, age, weight, opt, query, r, pred_active, selected, font_small
    if pred_active == 1:
        prediction(score)
    gd.fill((220,240,255))
    font = p.font.SysFont(None, 40)
    out1 = font.render("Answer all questions accurately", True, (0, 0, 0))
    gd.blit(out1, (340, 50))
    
    # Queries Input Managment
    if e and e.type == p.KEYDOWN:
        if e.key == p.K_UP:
            opt = 3 - opt
        elif e.key == p.K_DOWN:
            opt = 3 - opt
        elif e.key == p.K_RIGHT:
            if query == 1 and age < 100:
                age += 1
            elif query == 6 and weight < 100:
                weight += 50
            elif query == 11 and r == 0:
                r += 100
        elif e.key == p.K_LEFT:
            if query == 1 and age > 1:
                age -= 1
            elif query == 6 and weight > 1:
                weight -= 50
            elif query == 11 and r == 100:
                r -= 100
        elif e.key == p.K_RETURN:
            if query < 11:
                if query == 1:
                    if age >= 26 and age <= 35:
                        score += 1
                    elif age > 35 and age <= 45:
                        score += 2
                    elif age > 45 and age <= 55:
                        score += 3
                    elif age > 55:
                        score += 4
                        
                elif query == 6:
                    if weight == 0:
                        score += 0
                    elif weight == 50:
                        score += 1
                    elif weight == 100:
                        score += 2
                        
                elif query == 2 and opt == 1:
                    score += 2
                elif query == 3 and opt == 1:
                    score += 2
                elif query == 4 and opt == 1:
                    score += 1
                elif query == 5 and opt == 1:
                    score += 2
                elif query == 7 and opt == 2:
                    score += 1
                elif query == 8 and opt == 1:
                    score += 1
                elif query == 9 and opt == 1:
                    score += 1
                elif query == 10 and opt == 1:
                    score += 1
            elif query == 11:
                if r == 0:
                    score = 0
                    query = 0
                    age = 20
                    weight = 50
                    r = 100
                    barout = 0
                else:
                    selected = -1
            
            query += 1
                    
    
    font = p.font.SysFont(None, 30)
    q1 = font.render(f"(Q no {query})", True, (0, 0, 0))
    gd.blit(q1, (480, 150))
    
    if query == 1:
        # Question no 1
        font = p.font.SysFont(None, 30)
        q1 = font.render("What is your Age?", True, (0, 0, 0))
        gd.blit(q1, (400, 195))
        p.draw.rect(gd, (0, 255, 0), (400, 235, 100 * 3, 10), border_radius = 5)
        p.draw.rect(gd, (255, 0, 0), (400, 235, age * 3, 10), border_radius = 5)
        q6 = font.render(f"{age}", True, (0, 0, 0))
        gd.blit(q6, (400, 260))
    
    elif query == 2:
        # Question no 2
        q2 = font.render("Do you feel excessive thirst frequently?", True, (0, 0, 0))
        gd.blit(q2, (310, 195))
        if opt == 1:
            p.draw.rect(gd, (0, 255, 0), (360, 227, 60, 30), border_radius = 5)
        elif opt == 2:
            p.draw.rect(gd, (0, 255, 0), (360, 257, 60, 30), border_radius = 5)
        q2_o1 = font.render("Yes", True, (0, 0, 0))
        gd.blit(q2_o1, (367, 230))
        q2_o2 = font.render("No", True, (0, 0, 0))
        gd.blit(q2_o2, (370, 260))
    
    elif query == 3:
        # Question no 3
        q3 = font.render("Do you urinate more than usual?", True, (0, 0, 0))
        gd.blit(q3, (340, 195))
        if opt == 1:
            p.draw.rect(gd, (0, 255, 0), (360, 227, 60, 30), border_radius = 5)
        elif opt == 2:
            p.draw.rect(gd, (0, 255, 0), (360, 257, 60, 30), border_radius = 5)
        q3_o1 = font.render("Yes", True, (0, 0, 0))
        gd.blit(q3_o1, (367, 230))
        q3_o2 = font.render("No", True, (0, 0, 0))
        gd.blit(q3_o2, (370, 260))
    
    elif query == 4:
        # Question no 4
        q4 = font.render("Do you often feel tired or sleepy after meals?", True, (0, 0, 0))
        gd.blit(q4, (320, 195))
        if opt == 1:
            p.draw.rect(gd, (0, 255, 0), (360, 227, 60, 30), border_radius = 5)
        elif opt == 2:
            p.draw.rect(gd, (0, 255, 0), (360, 257, 60, 30), border_radius = 5)
        q4_o1 = font.render("Yes", True, (0, 0, 0))
        gd.blit(q4_o1, (367, 230))
        q4_o2 = font.render("No", True, (0, 0, 0))
        gd.blit(q4_o2, (370, 260))
    
    elif query == 5:
        # Question no 5
        q5 = font.render("Do you have a family history of diabetes?", True, (0, 0, 0))
        gd.blit(q5, (355, 195))
        if opt == 1:
            p.draw.rect(gd, (0, 255, 0), (360, 227, 60, 30), border_radius = 5)
        elif opt == 2:
            p.draw.rect(gd, (0, 255, 0), (360, 257, 60, 30), border_radius = 5)
        q5_o1 = font.render("Yes", True, (0, 0, 0))
        gd.blit(q5_o1, (367, 230))
        q5_o2 = font.render("No", True, (0, 0, 0))
        gd.blit(q5_o2, (370, 260))
    
    elif query == 6:
        # Question no 6
        q6 = font.render("What describes your weight best?", True, (0, 0, 0))
        gd.blit(q6, (390, 195))
        p.draw.rect(gd, (0, 255, 0), (400, 235, 100 * 3, 10), border_radius = 5)
        p.draw.rect(gd, (255, 0, 0), (400, 235, weight * 3, 10), border_radius = 5)
        if weight == 0:
            q6 = font.render("Underweight", True, (0, 0, 0))
            gd.blit(q6, (400, 260))
        elif weight == 50:
            q6 = font.render("Normal", True, (0, 0, 0))
            gd.blit(q6, (400, 260))
        elif weight == 100:
            q6 = font.render("Overweight", True, (0, 0, 0))
            gd.blit(q6, (400, 260))
    
    elif query == 7:
        # Question no 7
        q7 = font.render("Do you exercise regularly?", True, (0, 0, 0))
        gd.blit(q7, (360, 195))
        if opt == 1:
            p.draw.rect(gd, (0, 255, 0), (360, 227, 60, 30), border_radius = 5)
        elif opt == 2:
            p.draw.rect(gd, (0, 255, 0), (360, 257, 60, 30), border_radius = 5)
        q7_o1 = font.render("Yes", True, (0, 0, 0))
        gd.blit(q7_o1, (367, 230))
        q7_o2 = font.render("No", True, (0, 0, 0))
        gd.blit(q7_o2, (370, 260))
    
    elif query == 8:
        # Question no 8
        q8 = font.render("Do you have blurred vision sometimes?", True, (0, 0, 0))
        gd.blit(q8, (360, 195))
        if opt == 1:
            p.draw.rect(gd, (0, 255, 0), (360, 227, 60, 30), border_radius = 5)
        elif opt == 2:
            p.draw.rect(gd, (0, 255, 0), (360, 257, 60, 30), border_radius = 5)
        q8_o1 = font.render("Yes", True, (0, 0, 0))
        gd.blit(q8_o1, (367, 230))
        q8_o2 = font.render("No", True, (0, 0, 0))
        gd.blit(q8_o2, (370, 260))
    
    elif query == 9:
        # Question no 9
        q9 = font.render("Have you noticed unexplained weight loss recently?", True, (0, 0, 0))
        gd.blit(q9, (310, 195))
        if opt == 1:
            p.draw.rect(gd, (0, 255, 0), (360, 227, 60, 30), border_radius = 5)
        elif opt == 2:
            p.draw.rect(gd, (0, 255, 0), (360, 257, 60, 30), border_radius = 5)
        q9_o1 = font.render("Yes", True, (0, 0, 0))
        gd.blit(q9_o1, (367, 230))
        q9_o2 = font.render("No", True, (0, 0, 0))
        gd.blit(q9_o2, (370, 260))
    
    elif query == 10:
        # Question no 10
        q10 = font.render("Do you have increased hunger even after eating?", True, (0, 0, 0))
        gd.blit(q10, (325, 195))
        if opt == 1:
            p.draw.rect(gd, (0, 255, 0), (360, 227, 60, 30), border_radius = 5)
        elif opt == 2:
            p.draw.rect(gd, (0, 255, 0), (360, 257, 60, 30), border_radius = 5)
        q10_o1 = font.render("Yes", True, (0, 0, 0))
        gd.blit(q10_o1, (367, 230))
        q10_o2 = font.render("No", True, (0, 0, 0))
        gd.blit(q10_o2, (370, 260))
        
    else:
        # Question no 11 If wanna re-enter data
        q6 = font.render("Do you want to Re-Enter data or Submission?", True, (0, 0, 0))
        gd.blit(q6, (390, 195))
        p.draw.rect(gd, (0, 255, 0), (400, 235, 100 * 3, 10), border_radius = 5)
        p.draw.rect(gd, (255, 0, 0), (400, 235, r * 3, 10), border_radius = 5)
        if r == 0:
            q6 = font.render("Re-Enter Data", True, (0, 0, 0))
            gd.blit(q6, (400, 260))
        elif r == 100:
            q6 = font.render("Submit and Predict", True, (0, 0, 0))
            gd.blit(q6, (400, 260))
    
    # --- Footer ---
    footer = font_small.render("Version 1.0 | © 2025 Smart Diabetes Predictor", True, (128, 0, 0))
    gd.blit(footer, (365, 520))
    
    p.display.update()
    
 
while True:
    
    if selected == 0:
        menu(option)
    font = p.font.SysFont('Comic Sans MS', 40)
    header = font.render("Smart Diabetes Predictor (SDP)", True, (40, 200, 200))
    gd.blit(header, (260, 55))
    e = None
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
        elif event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE or event.key == p.K_BACKSPACE:
                if selected == 1 or selected == 2:
                    gd.fill((220,240,255))
                    selected = 0
                elif selected == -1:
                    gd.fill((220,240,255))
                    score = 0
                    age = 20
                    weight = 50
                    r = 100
                    query = 1
                    barout = 1
                    pred_active = 0
                    selected = 0
                else:
                    p.quit()
                    exit()
            if selected == 0:
                if event.key == p.K_UP and option > 1:
                    option -= 1
                elif event.key == p.K_DOWN and option < 3:
                    option += 1
                elif event.key == p.K_RETURN:
                    if selected == -1:
                        selected = 0
                    if option == 1:
                        selected = 1
                    elif option == 2:
                        selected = 2
                    elif option == 3:
                        p.quit()
                        exit()
            else:
                e = event
    if selected == -1:
        prediction(score)
    if selected == 1:
        queries(e)
    if selected == 2:
        about()
    
    
    p.display.update()


p.quit()