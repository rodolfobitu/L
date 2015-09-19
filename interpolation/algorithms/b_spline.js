/*globals algorithms*/
'use strict'

algorithms.push({
	name: 'B-Spline',
	color: 'blue',
	handler: function (points, resolution) {
		// Generate interpolated values
		let result = new Array(resolution)
		for (let i = 0; i < resolution; i++) {
			let t = i / (resolution - 1),
				t2 = 1 - t,
				values = points.slice(0),
				n = values.length

			while (n > 1) {
				for (let j = 0; j < n - 1; j++) {
					values[j] = t * values[j + 1] + t2 * values[j]
				}
				n--
			}

			result[i] = values[0]
		}
		return result
	}
})