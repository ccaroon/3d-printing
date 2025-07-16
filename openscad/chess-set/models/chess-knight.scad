$fn = 150;

union() {
	difference() {
		cylinder(d = 30.0, h = 3.9);
		translate(v = [0, 0, -1]) {
			cylinder(d = 20.6, h = 2.75);
		}
	}
	translate(v = [0, 0, 3.9]) {
		union() {
			scale(v = [1.0, 0.75]) {
				cylinder($fn = 8, d = 25, h = 4.428571428571429);
			}
			translate(v = [0.7142857142857143, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 4.428571428571429]) {
						cylinder($fn = 8, d = 23.571428571428573, h = 4.428571428571429);
					}
				}
			}
			translate(v = [1.4285714285714286, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 8.857142857142858]) {
						cylinder($fn = 8, d = 22.142857142857142, h = 4.428571428571429);
					}
				}
			}
			translate(v = [2.142857142857143, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 13.285714285714286]) {
						cylinder($fn = 8, d = 20.714285714285715, h = 4.428571428571429);
					}
				}
			}
			translate(v = [2.857142857142857, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 17.714285714285715]) {
						cylinder($fn = 8, d = 19.285714285714285, h = 4.428571428571429);
					}
				}
			}
			translate(v = [3.5714285714285716, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 22.142857142857146]) {
						cylinder($fn = 8, d = 17.857142857142858, h = 4.428571428571429);
					}
				}
			}
			translate(v = [4.285714285714286, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 26.571428571428573]) {
						cylinder($fn = 8, d = 16.42857142857143, h = 4.428571428571429);
					}
				}
			}
		}
	}
	translate(v = [4, 0, 33.9]) {
		minkowski() {
			cylinder(d = 17.75, h = 0.5);
			sphere(d = 2);
		}
	}
	translate(v = [3, 0, 34.4]) {
		translate(v = [-16.5, 6.0, 0]) {
			rotate(a = [90, 0, 0]) {
				resize(newsize = [24.75, 25.125, 0]) {
					linear_extrude(height = 12) {
						import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
					}
				}
			}
		}
	}
}
