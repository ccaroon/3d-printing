$fn = 150;

difference() {
	linear_extrude(height = 6.375) {
		polygon(points = [[0, 0], [0, 22.3125], [6.375, 25.5], [27.625, 25.5], [29.75, 23.375], [29.75, 0]]);
	}
	translate(v = [14.875, 4.25, 4.25]) {
		cylinder(d = 2.125, h = 3.125);
	}
	translate(v = [25.5, 22.3125, 4.25]) {
		cylinder(d = 2.125, h = 3.125);
	}
}
