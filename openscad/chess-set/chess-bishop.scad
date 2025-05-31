$fn = 150;

union() {
	difference() {
		cylinder(d = 30.0, h = 3.9);
		translate(v = [0, 0, -1]) {
			cylinder(d = 20.6, h = 2.75);
		}
	}
	translate(v = [0, 0, 3.9]) {
		rotate_extrude($fn = 250, angle = 360) {
			import(file = "./images/bishop/Bishop-Profile.dxf", origin = [0, 0]);
		}
	}
	translate(v = [0, 0, 42.9]) {
		union() {
			difference() {
				translate(v = [0, 0, 3.75]) {
					resize(newsize = [0, 0, 19.8]) {
						sphere(d = 15.0);
					}
				}
				translate(v = [3, 0, 5]) {
					rotate(a = [0, -50, 0]) {
						cylinder(d = 15.0, h = 1);
					}
				}
			}
			translate(v = [0, 0, 13.7625]) {
				resize(newsize = [5.625, 5.625, 0]) {
					sphere(d = 3.75);
				}
			}
		}
	}
}
