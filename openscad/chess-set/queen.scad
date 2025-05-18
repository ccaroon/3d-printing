$fn = 150;

union() {
	difference() {
		cylinder(d = 30.0, h = 3.8);
		translate(v = [0, 0, -1]) {
			cylinder(d = 15.5, h = 3.3);
		}
	}
	translate(v = [0, 0, 3.8]) {
		rotate_extrude($fn = 250, angle = 360) {
			import(file = "./images/queen/Queen-Profile.dxf", origin = [0, 0]);
		}
	}
	translate(v = [0, 0, 50.7]) {
		union() {
			rotate_extrude(angle = 360) {
				translate(v = [-11, 0, 0]) {
					circle(d = 2);
				}
			}
			difference() {
				cylinder($fn = 15, d1 = 17.5, d2 = 22.0, h = 10);
				translate(v = [0, 0, 10.5]) {
					rotate_extrude(angle = 360) {
						translate(v = [-8.5, 0, 0]) {
							circle(d = 8);
						}
					}
				}
			}
			translate(v = [0, 0, 8.0]) {
				sphere(d = 11);
			}
			translate(v = [0, 0, 13.5]) {
				sphere(d = 4);
			}
		}
	}
}
