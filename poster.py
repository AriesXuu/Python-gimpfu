#!/usr/bin/env python

# Hello World in GIMP Python

from gimpfu import *

def poster(back, image1, image2, image3):
    '''
    Function to do make the poster using pythonin-fu scripting for gimp.
    '''
    width = 200
    height = 300
    #create a new image with a width and height
    posterW, posterH = 2480, 3508
    posterImage = gimp.Image(posterW, posterH, RGB)
    
    #create the background layer
    backimage = pdb.file_jpeg_load(back, back)
    backLayer = gimp.Layer(posterImage,"backLayer", posterW, posterH, RGB_IMAGE, 100, NORMAL_MODE)
    posterImage.add_layer(backLayer, 0)
    pdb.gimp_edit_copy(backimage.layers[0])
    pdb.gimp_edit_paste(backLayer, True)
    backLayer.update(0, 0, posterW, posterH)
    backLayer.translate(0, 0)

    picture1 = pdb.file_jpeg_load(image1, image1)
    layer0 = gimp.Layer(posterImage, "Layer 0", 2480, 800, RGB_IMAGE, 100, NORMAL_MODE)
    posterImage.add_layer(layer0, 0)
    pdb.gimp_edit_copy(picture1.layers[0])
    pdb.gimp_edit_paste(layer0, True)
    layer0.update(0, 0, width, height)
    layer0.translate(0, 0)

    picture2 = pdb.file_jpeg_load(image2, image2)
    layer1 = gimp.Layer(posterImage, "Layer 1", 2250, 1885, RGB_IMAGE, 100, NORMAL_MODE)
    posterImage.add_layer(layer1, 0)
    pdb.gimp_edit_copy(picture2.layers[0])
    layer1.update(0, 0, width, height)
    layer1.translate(100, 1400)
    pdb.gimp_edit_paste(layer1, True)
    
    picture3 = pdb.file_jpeg_load(image3, image3)
    layer2 = gimp.Layer(posterImage, "Layer 2", 976, 650, RGB_IMAGE, 100, NORMAL_MODE)
    posterImage.add_layer(layer2, 0)
    pdb.gimp_edit_copy(picture3.layers[0])
    layer2.update(0, 0, width, height)
    layer2.translate(100, 1000)
    pdb.gimp_edit_paste(layer2, True)



    #make a color and setup the background
    colorB = gimpcolor.RGB(255, 255, 0)
    colorF = gimpcolor.RGB(255, 255, 255 )
    pdb.gimp_context_set_background(colorB)
    pdb.gimp_context_set_foreground(colorF)

    textLayer = pdb.gimp_text_fontname(posterImage, None, 370, 1000, "BEST PUB IN CORK", 8, True, 200, PIXELS, "Arial Black")
    #display posterImage
    gimp.Display(posterImage)
    

register(
              "python_fu_poster",
              "Script to Make a Poster",
              "Script has uses 4 pub images to make automaticaly a poster",
              "Yeqi Xu",
              "Copyright@YX",
              "2017",
              "Assignment Poster",
              "", 
              [
                  # list of parameter inputs
                (PF_FILE, "back", "Choose background image", ""),
                (PF_FILE, "image1", "Choose picture1", ""),
                (PF_FILE, "image2", "Choose picture2", ""),
                (PF_FILE, "image3", "Choose picture3", "")
                

              ],
              [],
              poster, menu="<Image>/File/Create/_CS6102"
)

main()
