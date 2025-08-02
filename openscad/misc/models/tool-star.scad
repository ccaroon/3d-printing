$fn = 150;

union() {
	cylinder(center = true, d = 20.0, h = 1.0);
	cube(center = true, size = [100.0, 5.0, 1.0]);
	rotate(a = [0, 0, 45]) {
		cube(center = true, size = [100.0, 5.0, 1.0]);
	}
	rotate(a = [0, 0, 90]) {
		cube(center = true, size = [100.0, 5.0, 1.0]);
	}
	rotate(a = [0, 0, 135]) {
		cube(center = true, size = [100.0, 5.0, 1.0]);
	}
}
