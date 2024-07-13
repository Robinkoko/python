#23p  6-1
from PIL import Image
area = (230,155,1110,770)
size = (640,200)
lion_img = Image.open("Lion.jpg")
fruit_img = Image.open("fruit.png")
print(lion_img.size,lion_img.format,lion_img.mode)
print(fruit_img.size,fruit_img.format,fruit_img.mode)
fruit_resz = fruit_img.resize(size)
lion_cropped = lion_img.crop(area)
lion_img.show()
fruit_img.show()
lion_cropped.save("lion_cropped.jpg")
fruit_resz.save("fruit_resized.png")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#25p   6-2
size = (128,128)
lion_rotated = lion_img.rotate(90)
lion_converted = lion_img.convert("L")
lion_transpose = lion_img.transpose(Image.FLIP_LEFT_RIGHT)
lion_img.thumbnail(size)
print("lion_converted.mode = ", lion_converted.mode)
print("lion_img.size = ", lion_img.size)
lion_converted.show()
lion_transpose.show()
lion_rotated.save("lion_rotated.jpg")
lion_img.save("lion_thumb.jpg")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#27p
fruit_converted = fruit_img.convert("L")
fruit_rotated = fruit_img.rotate(270)
fruit_converted.show()
fruit_rotated.show()
fruit_rotated.save("fruit_rotate.png")
fruit_converted.save("fruit_convert.png")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#29p  6-3
from PIL import ImageDraw
canvas_size = (200,200)
rect_area = [(0,0),(100,100)]
line_cor = [(0,200),(200,0)]
circle_area = [(100,100),(200,200)]
new_img = Image.new("RGB",canvas_size,"orange")
draw_imgs = ImageDraw.Draw(new_img)
draw_imgs.rectangle(rect_area , fill = "red",outline = "yellow")
draw_imgs.line(line_cor,fill = "blue", width = 4)
draw_imgs.ellipse(circle_area,fill = "green",outline = "red")
new_img.show()
new_img.save("imagedraw.jpg")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#31p  6-4
from PIL import ImageFont
c3coding_img = Image.open("c3coding_rt.jpg")
c3coding_img.thumbnail((120,120))
draw = ImageDraw.Draw(lion_img)
stx,sty = (150,285)
c3x,c3y = c3coding_img.size
msg1 = "the               is"
msg2 = "the best!"
mfont = ImageFont.truetype("arial.ttf",40)
m2font = ImageFont.truetype("arial.ttf",52)
draw.text((70,280),msg1,(255,255,0),font = mfont,align = "Left")
draw.text((70,330),msg2,(255,0,0),font = m2font,align = "Left")
lion_img.paste(c3coding_img,(stx, sty, stx+c3x, sty+c3y))
lion_img.show()
lion_img.save("c3lion.jpg")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#32p
lion_img = Image.open("lion.jpg")
draw=ImageDraw.Draw(lion_img)
draw.ellipse([(100,100),(1200,900)],outline="yellow",width=4)
lion_img.show()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#33p
c3coding_img = Image.open("c3coding_rt.jpg")
c3coding_img.thumbnail((120,120))
draw = ImageDraw.Draw(lion_img)
stx,sty = (150,285)
c3x,c3y = c3coding_img.size
msg1 = "the               is"
msg2 = "the best!"
mfont = ImageFont.truetype("arial.ttf",40)
m2font = ImageFont.truetype("arial.ttf",52)
draw.text((70,280),msg1,(255,255,0),font = mfont,align = "Left")
draw.text((70,330),msg2,(255,0,0),font = m2font,align = "Left")
lion_img.paste(c3coding_img,(stx, sty, stx+c3x, sty+c3y))
draw.ellipse([(35,230),(350,420)],outline="yellow",width=4)
draw.ellipse([(320,390),(360,420)],fill="yellow",outline="yellow",width=4)
draw.ellipse([(370,410),(390,425)],fill="yellow",outline="yellow",width=4)
draw.ellipse([(440,430),(390,430)],fill="yellow",outline="yellow",width=4)
lion_img.show()
