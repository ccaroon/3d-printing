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
				cylinder($fn = 8, d = 25, h = 4.142857142857143);
			}
			translate(v = [0.7142857142857143, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 4.142857142857143]) {
						cylinder($fn = 8, d = 23.571428571428573, h = 4.142857142857143);
					}
				}
			}
			translate(v = [1.4285714285714286, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 8.285714285714286]) {
						cylinder($fn = 8, d = 22.142857142857142, h = 4.142857142857143);
					}
				}
			}
			translate(v = [2.142857142857143, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 12.42857142857143]) {
						cylinder($fn = 8, d = 20.714285714285715, h = 4.142857142857143);
					}
				}
			}
			translate(v = [2.857142857142857, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 16.571428571428573]) {
						cylinder($fn = 8, d = 19.285714285714285, h = 4.142857142857143);
					}
				}
			}
			translate(v = [3.5714285714285716, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 20.714285714285715]) {
						cylinder($fn = 8, d = 17.857142857142858, h = 4.142857142857143);
					}
				}
			}
			translate(v = [4.285714285714286, 0, 0]) {
				scale(v = [1.0, 0.75]) {
					translate(v = [0, 0, 24.85714285714286]) {
						cylinder($fn = 8, d = 16.42857142857143, h = 4.142857142857143);
					}
				}
			}
		}
	}
	translate(v = [3.57, 0, 28.757142857142856]) {
		union() {
			hull() {
				translate(v = [-5.0, -5.0, 5]) {
					cube(size = [14.5, 10, 0.25]);
				}
				scale(v = [1.0, 0.75]) {
					cylinder($fn = 8, d = 17.857142857142858, h = 0.25);
				}
			}
			translate(v = [4.5, 0, 0]) {
				rotate(a = [0, 0, 180]) {
					translate(v = [0, 0, 10.5]) {
						mirror(v = [0, 0, 1]) {
							hull() {
								translate(v = [-5.0, -5.0, 5]) {
									cube(size = [14.5, 10, 0.25]);
								}
								translate(v = [0, 0, -1]) {
									scale(v = [1.0, 0.75]) {
										cylinder($fn = 3, d = 17.857142857142858, h = 0.25);
									}
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [4.85, 0, 33.75714285714285]) {
		translate(v = [-16.5, 5.0, 0]) {
			rotate(a = [90, 0, 0]) {
				resize(newsize = [24.75, 25.125, 0]) {
					linear_extrude(height = 10) {
						import(file = "../images/knight/piper-profile-fill.svg", origin = [0, 0]);
					}
				}
			}
		}
	}
}
