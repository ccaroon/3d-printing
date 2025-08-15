$fn = 150;

union() {
	difference() {
		union() {
			translate(v = [0.0, 0.0, 0]) {
				difference() {
					cylinder($fn = 6, d = 57.0, h = 3.0);
					translate(v = [0, 0, 1.0]) {
						cylinder($fn = 6, d = 55.0, h = 3.0);
					}
				}
			}
			translate(v = [42.0, 24.24871130596428, 0]) {
				difference() {
					cylinder($fn = 6, d = 57.0, h = 3.0);
					translate(v = [0, 0, 1.0]) {
						cylinder($fn = 6, d = 55.0, h = 3.0);
					}
				}
			}
			translate(v = [0.0, 48.49742261192856, 0]) {
				difference() {
					cylinder($fn = 6, d = 57.0, h = 3.0);
					translate(v = [0, 0, 1.0]) {
						cylinder($fn = 6, d = 55.0, h = 3.0);
					}
				}
			}
		}
		translate(v = [14.0, 24.25768590217984, 1.0]) {
			cylinder(d = 56.0, h = 3.5);
		}
	}
	translate(v = [-42.0, 24.24871130596428, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 55.0, h = 3.0);
			}
		}
	}
	translate(v = [-42.0, 72.74613391789285, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 55.0, h = 3.0);
			}
		}
	}
	translate(v = [42.0, 72.74613391789285, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 55.0, h = 3.0);
			}
		}
	}
	translate(v = [84.0, 48.49742261192856, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 55.0, h = 3.0);
			}
		}
	}
	translate(v = [0.0, 96.99484522385713, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 55.0, h = 3.0);
			}
		}
	}
	translate(v = [42.0, 121.2435565298214, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 55.0, h = 3.0);
			}
		}
	}
	translate(v = [84.0, 96.99484522385713, 0]) {
		difference() {
			cylinder($fn = 6, d = 57.0, h = 3.0);
			translate(v = [0, 0, 1.0]) {
				cylinder($fn = 6, d = 55.0, h = 3.0);
			}
		}
	}
}
