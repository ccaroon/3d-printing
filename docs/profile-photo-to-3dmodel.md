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
7.  Select the Bezier Curves & Straight Line tool (B)
8.  Layer -> Add Layer...
    - Name: outline
    - Position: Above Current
    - Use the Layers tab to ensure that you are going to be drawing in the new layer
9. Save as an InkScape SVG
10. Now we are going to trace the profile image and create a closed object
    - Start at the bottom
    - Stay in the center of the profile line
    - Always draw straight lines, not curves
    - Create as many line segments as necessary to maintain a "curve"
    - When you reach the top, you'll need to draw a level line all the way to the left edge of the page. Use the Ctrl key to force the line to be level.
    - Then Down, again using the Ctrl key to keep the line vertical
    - Then to the right to finally connect with the starting point
    - The bottom line will be hard to keep level; do your best!
11. Save your work
12. Now we need to get the bottom line level / horizontal
    - Selec the Node tool (N)
    - Grab the left lower corner
    - Use the Arrow keys to adjust the bottom line to be level / aligned with the selection dotted line.
    - Adjust the corner using until the left vertical and bottom horizontal lines are perfect.
13. Delete the original profile image/object layer
    - Layers -> Layers and Object...
    - Select the original layer
    - Right-click -> Delete Layer
    - Save SVG
14. Adjust the shape / form of the profile outline
    - Still using the Node tool
    - Select the top-left and bottom-left node points to adjust the width
    - Other edits as necessary by moving nodes, deleting nodes or adding nodes
    - Trial & Error process
    - Continue only once you have the shape of the profile like you want it
15. Select the Profile object
16. Object -> Transform...Scale
    - Units: mm
    - Height: 40 (or whatever size is appropriate)
    - Scale proportionally: YES
    - Apply
17. Edit -> Resize Page to Selection
    - Page and profil object may not be in the same place
    - View -> Zoom -> Zoom Page ... should fix it.
18. DON'T save the SVG after Scaling it down
    - Save the original size in case you need it again
19. Save As...
    - Desktop Cutter Plotter (...R12...) (.dxf)
20. DXF file can now be imported into OpenSCAD
