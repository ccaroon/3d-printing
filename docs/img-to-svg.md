# How-to Convert an Image to an SVG

1. Take a photo of object on iPhone
2. Long-press object in photo to create a Sticker
3. Upload sticker image from phone to computer
4. Open sticker image in GIMP and clean up as necessary.
   - Outline the object and fill with black
   - or
   - Clean up edges
   - or
   - Whatever
5. At this point the sticker image should only the object you want to model with NO  background, i.e. transparent background.
6. Save / Export as PNG
7. Launch Inkscape
8. File -> Import -> Select Image
   - Embed
   - DPI from file
   - Mode: Auto
   - OK
9. Select imported image, then Edit -> Resize Page to Selection
10. Path -> Trace Bitmap...
   - Multicolor
   - Detection mode: Colors
   - Scans: 2
   - Smooth
   - Remove Background
   - Apply
11. Traced Image will appear ON TOP OF imported image
12. Ctrl-X to Cut it to clipboard
13. Select Original Image -> Delete
14. Ctrl-V to paste Traced Image
15. Position Properly
16. Edit -> Resize Page to Selection
17. Save As...
    - Enter new file name
    - Save
18. SVG can now be imported into OpenSCAD and extruded to a 3D model.
