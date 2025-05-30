$fn = 150;

union() {
	translate(v = [0, 0.5, 0]) {
		translate(v = [0.75, 0, 0]) {
			union() {
				translate(v = [1, 0, 0]) {
					translate(v = [0, 30.0, 0]) {
						cube(size = [80, 7.5, 1.75]);
					}
				}
				translate(v = [5, 0, 0]) {
					rotate(a = 20, v = [0, 0, 1]) {
						cube(size = [80, 7.5, 1.75]);
					}
				}
				translate(v = [0, 27, 0]) {
					rotate(a = -20, v = [0, 0, 1]) {
						cube(size = [80, 7.5, 1.75]);
					}
				}
			}
		}
	}
	translate(v = [8.8, 8.6, 0]) {
		rotate(a = 180) {
			linear_extrude(height = 27.75) {
				import(file = "../resources/twig.svg", origin = [0, 0]);
			}
		}
	}
	translate(v = [7.5, 0, 0]) {
		translate(v = [0, 8.8, 0]) {
			rotate(a = 270) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [15.0, 0, 0]) {
		translate(v = [-2.5, 4.4, 0]) {
			rotate(a = 315) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [22.5, 0, 0]) {
		translate(v = [8.6, 0, 0]) {
			rotate(a = 90) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [30.0, 0, 0]) {
		translate(v = [0, 0, 0]) {
			rotate(a = 0) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [37.5, 0, 0]) {
		translate(v = [0, 8.8, 0]) {
			rotate(a = 270) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [45.0, 0, 0]) {
		translate(v = [4.5, 10.39, 0]) {
			rotate(a = 225) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [52.5, 0, 0]) {
		translate(v = [8.8, 8.6, 0]) {
			rotate(a = 180) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [60.0, 0, 0]) {
		translate(v = [4.5, -2.5, 0]) {
			rotate(a = 45) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [67.5, 0, 0]) {
		translate(v = [10.39, 4.5, 0]) {
			rotate(a = 135) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [75.0, 0, 0]) {
		translate(v = [0, 0, 0]) {
			rotate(a = 0) {
				linear_extrude(height = 27.75) {
					import(file = "../resources/twig.svg", origin = [0, 0]);
				}
			}
		}
	}
	translate(v = [0, 7.5, 0]) {
		union() {
			translate(v = [10.39, 4.5, 0]) {
				rotate(a = 135) {
					linear_extrude(height = 27.75) {
						import(file = "../resources/twig.svg", origin = [0, 0]);
					}
				}
			}
			translate(v = [7.5, 0, 0]) {
				translate(v = [4.5, 10.39, 0]) {
					rotate(a = 225) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
			translate(v = [15.0, 0, 0]) {
				translate(v = [4.5, -2.5, 0]) {
					rotate(a = 45) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
			translate(v = [60.0, 0, 0]) {
				translate(v = [0, 0, 0]) {
					rotate(a = 0) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
			translate(v = [67.5, 0, 0]) {
				translate(v = [8.6, 0, 0]) {
					rotate(a = 90) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
			translate(v = [75.0, 0, 0]) {
				translate(v = [4.5, -2.5, 0]) {
					rotate(a = 45) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 15.0, 0]) {
		union() {
			translate(v = [8.6, 0, 0]) {
				rotate(a = 90) {
					linear_extrude(height = 27.75) {
						import(file = "../resources/twig.svg", origin = [0, 0]);
					}
				}
			}
			translate(v = [7.5, 0, 0]) {
				translate(v = [10.39, 4.5, 0]) {
					rotate(a = 135) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
			translate(v = [67.5, 0, 0]) {
				translate(v = [4.5, -2.5, 0]) {
					rotate(a = 45) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
			translate(v = [75.0, 0, 0]) {
				translate(v = [8.6, 0, 0]) {
					rotate(a = 90) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 22.5, 0]) {
		union() {
			translate(v = [4.5, -2.5, 0]) {
				rotate(a = 45) {
					linear_extrude(height = 27.75) {
						import(file = "../resources/twig.svg", origin = [0, 0]);
					}
				}
			}
			translate(v = [75.0, 0, 0]) {
				translate(v = [10.39, 4.5, 0]) {
					rotate(a = 135) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 30.0, 0]) {
		union() {
			translate(v = [0, 0, 0]) {
				rotate(a = 0) {
					linear_extrude(height = 27.75) {
						import(file = "../resources/twig.svg", origin = [0, 0]);
					}
				}
			}
			translate(v = [75.0, 0, 0]) {
				translate(v = [8.8, 8.6, 0]) {
					rotate(a = 180) {
						linear_extrude(height = 27.75) {
							import(file = "../resources/twig.svg", origin = [0, 0]);
						}
					}
				}
			}
		}
	}
}
