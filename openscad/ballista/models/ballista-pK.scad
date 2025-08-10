$fn = 150;

rotate(a = [0, -90, 0]) {
	union() {
		color(alpha = 1.0, c = "#00ff77") {
			linear_extrude(height = 6.375) {
				polygon(points = [[0, 0], [0, 6.375], [5.3125, 6.375], [6.375, 5.3125], [7.4375, 6.375], [7.4375, 0], [6.375, 1.0625], [5.3125, 0]]);
			}
		}
		translate(v = [7.4375, 0, 0]) {
			color(alpha = 1.0, c = "#0077ff") {
				cube(size = [9.5625, 6.375, 6.375]);
			}
		}
		translate(v = [17.0, 0, 0]) {
			color(alpha = 1.0, c = "#770077") {
				hull() {
					cube(size = [1, 6.375, 6.375]);
					translate(v = [50.0, 3.1875, 3.1875]) {
						rotate(a = [0, 90, 0]) {
							cylinder(d = 6.375, h = 1);
						}
					}
				}
			}
		}
	}
}
