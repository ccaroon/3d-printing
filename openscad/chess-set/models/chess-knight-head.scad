$fn = 150;

difference() {
	translate(v = [4.85, 0, 0]) {
		translate(v = [-16.5, 5.0, 0]) {
			rotate(a = [90, 0, 0]) {
				resize(newsize = [24.75, 25.125, 0]) {
					linear_extrude(height = 10) {
						import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
					}
				}
			}
		}
	}
	translate(v = [3.57, 0, -1]) {
		union() {
			translate(v = [-0.5, 0, 0]) {
				cylinder(d = 5.5, h = 4.5);
			}
			translate(v = [6, 0, 0]) {
				translate(v = [-0.5, 0, 0]) {
					cylinder(d = 5.5, h = 4.5);
				}
			}
		}
	}
}
