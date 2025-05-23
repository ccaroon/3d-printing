# Inkscape Cheatsheet

## Links
* https://inkscape.org/doc/tutorials/shapes/tutorial-shapes.html
* Curves to Lines: https://alpha.inkscape.org/vectors/www.inkscapeforum.com/viewtopic4607.html?t=4308
* Inkscape DXF to OpenScad:
    - https://alpha.inkscape.org/vectors/www.inkscapeforum.com/viewtopic5205.html?t=18501
    - http://repraprip.blogspot.com/2011/05/inkscape-to-openscad-dxf-tutorial.html
*

## Save as OpenSCAD Importable DXF
1. Select Object
2. Path -> Object To Path
3. Extensions -> Modify Path -> Add Nodes...
    * Division method: By number of segments
    * Maximum segment lenght: 10
    * Number of segments: 256
    * Apply & Close
 4. Extensions -> Modify Path -> Straighten Segments...
    * Percent: 100.0
    * Behavior: 1
    * Apply & Close
