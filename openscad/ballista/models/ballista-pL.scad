$fn = 150;

rotate(a = [0, -90, 0]) {
	union() {
		translate(v = [0, 2.125, 2.125]) {
			rotate(a = [0, 90, 0]) {
				cylinder(d = 4.25, h = 21.25);
			}
		}
		cube(size = [21.25, 4.25, 2.125]);
	}
}
