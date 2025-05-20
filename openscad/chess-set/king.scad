$fn = 150;

union() {
	difference() {
		cylinder(d = 30.0, h = 3.9);
		translate(v = [0, 0, -1]) {
			cylinder(d = 15.5, h = 3.5);
		}
	}
	translate(v = [0, 0, 3.9]) {
		rotate_extrude($fn = 250, angle = 360) {
			import(file = "./images/king/King-Profile.dxf", origin = [0, 0]);
		}
	}
	translate(v = [0, 0, 47.7]) {
		union() {
			rotate_extrude(angle = 360) {
				translate(v = [-11, 0, 0]) {
					circle(d = 2);
				}
			}
			difference() {
				cylinder($fn = 5, d1 = 17.5, d2 = 22.0, h = 10);
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
			translate(v = [0, 0, 12.0]) {
				union() {
					translate(v = [0, -1.375, 0]) {
						translate(v = [-1.375, 0, 0]) {
							cube(size = [2.75, 2.75, 11]);
						}
					}
					translate(v = [0, 0, 5.5]) {
						translate(v = [0, -1.375, 0]) {
							translate(v = [-4.5, 0, 0]) {
								cube(size = [9, 2.75, 2.75]);
							}
						}
					}
				}
			}
		}
	}
}
