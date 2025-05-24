$fn = 150;

union() {
	difference() {
		cylinder(d = 30.0, h = 3.9);
		translate(v = [0, 0, -1]) {
			cylinder(d = 15.5, h = 3.5);
		}
	}
	translate(v = [0, 0, 3.9]) {
		union() {
			linear_extrude(height = 36.525000000000006, twist = 360) {
				circle($fn = 5, d = 15.0);
			}
			minkowski() {
				sphere(d = 2.0);
				cylinder(d = 22.5, h = 1);
			}
			translate(v = [0, 0, 1]) {
				minkowski() {
					sphere(d = 2.0);
					cylinder(d = 19.8, h = 1);
				}
			}
		}
	}
	translate(v = [0, 0, 40.425000000000004]) {
		union() {
			difference() {
				translate(v = [0, 0, 3.75]) {
					resize(newsize = [0, 0, 19.8]) {
						sphere(d = 15.0);
					}
				}
				translate(v = [3, 0, 3]) {
					rotate(a = [0, -50, 0]) {
						cylinder(d = 15.0, h = 1);
					}
				}
			}
			translate(v = [0, 0, 13.125]) {
				resize(newsize = [5.625, 5.625, 0]) {
					sphere(d = 3.75);
				}
			}
		}
	}
}
