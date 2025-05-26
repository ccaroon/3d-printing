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
			translate(v = [0, 0, 32.87250000000001]) {
				union() {
					cylinder(d1 = 12.0, d2 = 19.8, h = 2);
					translate(v = [0, 0, 2]) {
						cylinder(d1 = 19.8, d2 = 14.399999999999999, h = 2);
					}
				}
			}
			minkowski() {
				sphere(d = 2.0);
				cylinder(d = 22.5, h = 1);
			}
			translate(v = [0, 0, 1]) {
				cylinder(d1 = 19.8, d2 = 15.0, h = 9.131250000000001);
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
