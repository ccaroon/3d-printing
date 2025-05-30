$fn = 150;

translate(v = [0, 0, 0]) {
	rotate(a = 0) {
		linear_extrude(height = 22) {
			import(file = "../resources/twig.svg", origin = [0, 0]);
		}
	}
}
