'use strict'

/** @const {number} */
const numPoints = 6

/**
 * The point values (from 0 to 100)
 * @var {Array<number>}
 */
let points = new Array(numPoints).fill(50)

/** @var {HTMLCanvasElement} */
let canvas = null

/** @var {CanvasRenderingContext2D} */
let context = null

/** @var {number} */
let width = 0

/** @var {number} */
let height = 0

window.addEventListener('resize', resizeCanvas)
window.addEventListener('load', init)

/**
 * Start the app
 */
function init() {
	canvas = document.getElementById('canvas')
	context = canvas.getContext('2d')
	resizeCanvas()
	draw()
}

/**
 * Handle canvas resizing
 */
function resizeCanvas() {
	width = canvas.width = canvas.clientWidth
	height = canvas.height = canvas.clientHeight
	draw()
}

/**
 * Redraw the canvas content
 */
function draw() {
	// Reset
	context.clearRect(0, 0, width, height)

	// Draw points
	points.forEach((p, i) => {
		let {
			x, y
		} = toCanvasXY(i)
		context.arc(x, y, 5, 0, 2 * Math.PI)
		context.fill()
	})
}

/**
 * Return the i-th point coordinates in canvas space
 * @param {number} i
 * @returns {{x: number, y: number}}
 */
function toCanvasXY(i) {
	return {
		x: width / (numPoints + 1) * (i + 1),
		y: height * (0.1 + 0.8 * points[i] / 100)
	}
}