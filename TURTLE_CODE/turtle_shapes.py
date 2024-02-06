 # JAI SHREE RAM 
 
import turtle as t

# for i in range(3):
# # tirangle    
#     t.forward(100)
#     t.left(120)
# for i in range (4):        
#     t.forward(100)
#     t.left(90)


# # pentagon 
# for i in range (5):  
#     t.forward(100)
#     t.left(72)

# # hexgon
# for i in range (6):  
#     t.forward(100)
#     t.left(60)
  
# # heptagon
# for i in range (7):  
#     t.forward(100)
#     t.left(52)

# for i in range (8):  
#     t.forward(100)
#     t.left(45)

# for i in range (9):  
#     t.forward(100)
#     t.left(40)

# for i in range (10):  
#     t.forward(100)
#     t.left(36)   
        
# for i in range (11):  
#     t.forward(100)
#     t.left(33)
# for i in range (12):  
#     t.forward(100)
#     t.left(30)          


def draw_shape(side):
    angle=360/side
    for i in range(side):
        t.forward(100)
        t.left(angle)
for no_side in range(3,11):
    draw_shape(no_side)        

t.exitonclick()

   
 