$fn = 150;

union() {
	difference() {
		cylinder(d = 30.0, h = 3.9);
		translate(v = [0, 0, -1]) {
			cylinder(d = 20.5, h = 2.5);
		}
	}
	translate(v = [0, 0, 3.9]) {
		rotate_extrude($fn = 250, angle = 360) {
			import(file = "./images/bishop/Bishop-Profile.dxf", origin = [0, 0]);
		}
	}
	translate(v = [0, 0, 47.9]) {
		union() {
			difference() {
				translate(v = [0, 0, 4.5]) {
					resize(newsize = [0, 0, 22.5]) {
						sphere(d = 18.0);
					}
				}
				translate(v = [3, 0, 5]) {
					rotate(a = [0, -50, 0]) {
						cylinder(d = 18.0, h = 1);
					}
				}
			}
			translate(v = [0, 0, 16.515]) {
				resize(newsize = [6.75, 6.75, 0]) {
					sphere(d = 4.5);
				}
			}
		}
	}
}
