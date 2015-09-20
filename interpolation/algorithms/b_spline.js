/*globals algorithms*/
'use strict'

algorithms.push({
	name: 'B-Spline',
	color: 'blue',
	handler: function (points, resolution) {
		// Generate interpolated values
		let result = new Array(resolution),
			temp = new Array(points.length - 1)
		for (let i = 0; i < resolution; i++) {
			let t = i / (resolution - 1),
				t2 = 1 - t,
				n = points.length - 1

			for (let j = 0; j < n; j++) {
				temp[j] = t * points[j + 1] + t2 * points[j]
			}
			while (n > 1) {
				for (let j = 0; j < n - 1; j++) {
					temp[j] = t * temp[j + 1] + t2 * temp[j]
				}
				n--
			}

			result[i] = temp[0]
		}
		return result
	}
})