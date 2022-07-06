from PIL import Image,ImageEnhance
img1= Image.open('mypic.jpg')
# img1.save('mypic.pdf')
# img1.show()
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(2).save('mypicedt.png')