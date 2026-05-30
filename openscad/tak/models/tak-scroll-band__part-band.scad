$fn = 150;

difference() {
	cylinder(d = 23.0, h = 5.0);
	#translate(v = [0, 0, -1]) {
		cylinder(d = 22.0, h = 7.0);
	}
}
