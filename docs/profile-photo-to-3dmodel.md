# Profile Photo to 3D Model

1. Open photo with GIMP
2. Add new, transparent Layer on "top" of photo named "Profile"
3. Choose Pencil Tool (N)
   - Harness: 100%
   - Size: 5
   - Mode: Normal
   - Color: Black
4. Carefully trace the facial profile using the Pencil tool in the new layer
    - Zoom in/out as necessary
    - Be precise
    - As continuous as possible
5. Save Profile layer as PNG
    - Select Profile layer and set as Visible
    - Unset photo layer as Visible
    - You should only see the pencil drawn profile on a transparent background
    - File -> Export As...
    - Type in file name with `.png` suffix: `profile.png`
    - Export
    - Compression Level: 0
    - Export
6. Open Profile PNG in Inkscape
    - File -> Open...
    - Select `profile.png` file
    - Image DPI: From file
    - Image Rendering Mode: None (auto)
    - OK
8.  Path -> Trace Bitmap...
    - Multicolor
    - Detection mode: Colors
    - Scans: 2
    - Smooth
    - Remove Background
    - Update Preview ... look OK?
    - Apply
    - Profile selection box will shrink to profile dimensions
9.  Traced Image will appear ON TOP OF imported image
10. Ctrl-X to Cut it to clipboard
11. Select original profile image & press Delete
12. Ctrl-V to paste Traced Image
14. File -> Document Properties
    - Units: mm
    - Set Width & Height to be slightly larger than profile image
    - Need enough room to draw / tweak the image a bit
    - We'll resize again later to the correct size
15. Save as Inkscape SVG
16. Select the Bezier Curves & Straght Line tool (B)
17. Layer -> Add Layer...
    - Name: outline
    - Position: Above Current
18. Now we are going to trace the profile image and create a close object
    - Start at the bottom
    - Stay in the center of the profile line
    - Create as many line segments as necessary to maintain a "curve"
    - When you reach the top, you'll need to draw a level line all the way to the left edge of the page. Use the Ctrl key to force the line to be level.
    - Then Down, again using the Ctrl key to keep the line vertical
    - Then to the right to finally connect with the starting point
    - The bottom line will be hard to keep level; do your best!
19. Save your work
20. Now we need to get the bottom line level / horizontal
    - Selec the Node tool (N)
    - Grab the left lower corner
    - Adjust the corner using the Ctrl key to keep things aligned until the left vertical and bottom horizontal lines are perfect.
21. Delete the original profile image/object layer
    - Layers -> Layers and Object...
    - Select the original layer
    - Right-click -> Delete Layer
    - Save SVG
22. Select the drawn profile object
23. Object -> Transform...Scale
    - Units: mm
    - Height: 45
    - Scale proportionally: YES
24. Edit -> Resize Page to Selection
    - Page and profil object may not be in the same place
    - View -> Zoom -> Zoom Page ... should fix it.
25. Save As...a different name ... um ...because?!
26. SAve As...
    - Desktop Cutter Plotter (...R12...) (.dxf)
    -


-----

1.  Select profile object and move up and left
    - Left such that the nose is as close as you want to the left side be the thinness part
    - Up to give room to edit

2.  Edit -> Resize Page to Selection

3.  Center the profile image
4.  Remember, we're looking at the **negative** space
18.

1.  Position Properly





16. Transform -> Scale...
    - Units: mm
    - Scale proportionally: YES
    - Adjust Height to required values (45'is for Chess Set)
    - Apply
17. Document Properties...
    - Click "Resize to content" button
