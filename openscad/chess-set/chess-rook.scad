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
			translate(v = [0, 9.3125, 0]) {
				color(alpha = 1.0, c = "red") {
					translate(v = [-3.8125, -1.8125, 0]) {
						cube(size = [7.625, 3.625, 2.25]);
					}
				}
			}
			translate(v = [6.6875, 0, 0]) {
				translate(v = [0, 6.6875, 0]) {
					rotate(a = [0, 0, -45]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
				}
			}
			translate(v = [9.3125, 0, 0]) {
				rotate(a = [0, 0, -90]) {
					color(alpha = 1.0, c = "red") {
						translate(v = [-3.8125, -1.8125, 0]) {
							cube(size = [7.625, 3.625, 2.25]);
						}
					}
				}
			}
			translate(v = [6.6875, 0, 0]) {
				translate(v = [0, -6.6875, 0]) {
					rotate(a = [0, 0, 45]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
				}
			}
			translate(v = [0, -9.3125, 0]) {
				color(alpha = 1.0, c = "red") {
					translate(v = [-3.8125, -1.8125, 0]) {
						cube(size = [7.625, 3.625, 2.25]);
					}
				}
			}
			translate(v = [-6.6875, 0, 0]) {
				translate(v = [0, -6.6875, 0]) {
					rotate(a = [0, 0, -45]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
				}
			}
			translate(v = [-9.3125, 0, 0]) {
				rotate(a = [0, 0, 90]) {
					color(alpha = 1.0, c = "red") {
						translate(v = [-3.8125, -1.8125, 0]) {
							cube(size = [7.625, 3.625, 2.25]);
						}
					}
				}
			}
			translate(v = [-6.6875, 0, 0]) {
				translate(v = [0, 6.6875, 0]) {
					rotate(a = [0, 0, 45]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
				}
			}
			rotate(a = [0, 0, -22.5]) {
				translate(v = [0, 0, 2.25]) {
					union() {
						translate(v = [0, 9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [9.3125, 0, 0]) {
							rotate(a = [0, 0, -90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [0, -9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [-9.3125, 0, 0]) {
							rotate(a = [0, 0, 90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 4.5]) {
				union() {
					translate(v = [0, 9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [9.3125, 0, 0]) {
						rotate(a = [0, 0, -90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [0, -9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [-9.3125, 0, 0]) {
						rotate(a = [0, 0, 90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
				}
			}
			rotate(a = [0, 0, -22.5]) {
				translate(v = [0, 0, 6.75]) {
					union() {
						translate(v = [0, 9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [9.3125, 0, 0]) {
							rotate(a = [0, 0, -90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [0, -9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [-9.3125, 0, 0]) {
							rotate(a = [0, 0, 90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 9.0]) {
				union() {
					translate(v = [0, 9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [9.3125, 0, 0]) {
						rotate(a = [0, 0, -90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [0, -9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [-9.3125, 0, 0]) {
						rotate(a = [0, 0, 90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
				}
			}
			rotate(a = [0, 0, -22.5]) {
				translate(v = [0, 0, 11.25]) {
					union() {
						translate(v = [0, 9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [9.3125, 0, 0]) {
							rotate(a = [0, 0, -90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [0, -9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [-9.3125, 0, 0]) {
							rotate(a = [0, 0, 90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 13.5]) {
				union() {
					translate(v = [0, 9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [9.3125, 0, 0]) {
						rotate(a = [0, 0, -90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [0, -9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [-9.3125, 0, 0]) {
						rotate(a = [0, 0, 90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
				}
			}
			rotate(a = [0, 0, -22.5]) {
				translate(v = [0, 0, 15.75]) {
					union() {
						translate(v = [0, 9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [9.3125, 0, 0]) {
							rotate(a = [0, 0, -90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [0, -9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [-9.3125, 0, 0]) {
							rotate(a = [0, 0, 90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 18.0]) {
				union() {
					translate(v = [0, 9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [9.3125, 0, 0]) {
						rotate(a = [0, 0, -90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [0, -9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [-9.3125, 0, 0]) {
						rotate(a = [0, 0, 90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
				}
			}
			rotate(a = [0, 0, -22.5]) {
				translate(v = [0, 0, 20.25]) {
					union() {
						translate(v = [0, 9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [9.3125, 0, 0]) {
							rotate(a = [0, 0, -90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [0, -9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [-9.3125, 0, 0]) {
							rotate(a = [0, 0, 90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 22.5]) {
				union() {
					translate(v = [0, 9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [9.3125, 0, 0]) {
						rotate(a = [0, 0, -90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [0, -9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [-9.3125, 0, 0]) {
						rotate(a = [0, 0, 90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
				}
			}
			rotate(a = [0, 0, -22.5]) {
				translate(v = [0, 0, 24.75]) {
					union() {
						translate(v = [0, 9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [9.3125, 0, 0]) {
							rotate(a = [0, 0, -90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [0, -9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [-9.3125, 0, 0]) {
							rotate(a = [0, 0, 90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 27.0]) {
				union() {
					translate(v = [0, 9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [9.3125, 0, 0]) {
						rotate(a = [0, 0, -90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [0, -9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [-9.3125, 0, 0]) {
						rotate(a = [0, 0, 90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
				}
			}
			rotate(a = [0, 0, -22.5]) {
				translate(v = [0, 0, 29.25]) {
					union() {
						translate(v = [0, 9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [9.3125, 0, 0]) {
							rotate(a = [0, 0, -90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [0, -9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [-9.3125, 0, 0]) {
							rotate(a = [0, 0, 90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 31.5]) {
				union() {
					translate(v = [0, 9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [9.3125, 0, 0]) {
						rotate(a = [0, 0, -90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [0, -9.3125, 0]) {
						color(alpha = 1.0, c = "red") {
							translate(v = [-3.8125, -1.8125, 0]) {
								cube(size = [7.625, 3.625, 2.25]);
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, -6.6875, 0]) {
							rotate(a = [0, 0, -45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
					translate(v = [-9.3125, 0, 0]) {
						rotate(a = [0, 0, 90]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
					}
					translate(v = [-6.6875, 0, 0]) {
						translate(v = [0, 6.6875, 0]) {
							rotate(a = [0, 0, 45]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
					}
				}
			}
			rotate(a = [0, 0, -22.5]) {
				translate(v = [0, 0, 33.75]) {
					union() {
						translate(v = [0, 9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [9.3125, 0, 0]) {
							rotate(a = [0, 0, -90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [0, -9.3125, 0]) {
							color(alpha = 1.0, c = "red") {
								translate(v = [-3.8125, -1.8125, 0]) {
									cube(size = [7.625, 3.625, 2.25]);
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, -6.6875, 0]) {
								rotate(a = [0, 0, -45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
						translate(v = [-9.3125, 0, 0]) {
							rotate(a = [0, 0, 90]) {
								color(alpha = 1.0, c = "red") {
									translate(v = [-3.8125, -1.8125, 0]) {
										cube(size = [7.625, 3.625, 2.25]);
									}
								}
							}
						}
						translate(v = [-6.6875, 0, 0]) {
							translate(v = [0, 6.6875, 0]) {
								rotate(a = [0, 0, 45]) {
									color(alpha = 1.0, c = "red") {
										translate(v = [-3.8125, -1.8125, 0]) {
											cube(size = [7.625, 3.625, 2.25]);
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [0, 0, 39.75]) {
		difference() {
			union() {
				cylinder(d = 22.5, h = 1.125);
				difference() {
					cylinder(d1 = 22.5, d2 = 24.5, h = 10.0);
					translate(v = [0, 0, 11.25]) {
						sphere(d = 22.5);
					}
				}
			}
			translate(v = [-1.0, 7.25, 3.625]) {
				cube(center = false, size = [2, 8, 7.5]);
			}
			translate(v = [-1.0, -15.25, 3.625]) {
				cube(center = false, size = [2, 8, 7.5]);
			}
			rotate(a = [0, 0, 90]) {
				translate(v = [-1.0, -15.25, 3.625]) {
					cube(center = false, size = [2, 8, 7.5]);
				}
			}
			rotate(a = [0, 0, -90]) {
				translate(v = [-1.0, -15.25, 3.625]) {
					cube(center = false, size = [2, 8, 7.5]);
				}
			}
		}
	}
}
