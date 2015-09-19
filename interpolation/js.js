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

/**
 * `null` if no point is being dragged, point
 * position (`i`) otherwise
 * @var {?number}
 */
let dragging = null

/**
 * @var {boolean}
 */
let waitingDraw = false

window.addEventListener('resize', resizeCanvas)
window.addEventListener('load', init)

/**
 * Start the app
 */
function init() {
	canvas = document.getElementById('canvas')
	context = canvas.getContext('2d')
	resizeCanvas()
	canvas.addEventListener('mousedown', handleMouseDown)
	canvas.addEventListener('mousemove', handleMouseMove)
	canvas.addEventListener('mouseup', handleMouseUp)
}

/**
 * Handle canvas resizing
 */
function resizeCanvas() {
	width = canvas.width = canvas.clientWidth
	height = canvas.height = canvas.clientHeight
	requestDraw()
}

/**
 * Redraw the canvas content
 */
function draw() {
	waitingDraw = false

	// Reset
	context.clearRect(0, 0, width, height)

	// Draw points
	points.forEach((p, i) => {
		let {
			x, y
		} = toCanvasXY(i)
		context.beginPath()
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

/**
 * Convert from canvas space to point space
 * @param {number} x
 * @param {number} y
 * @returns {{i: number, isNear: boolean, value: number}}
 */
function fromCanvasXY(x, y) {
	let value = 100 * (y / height - 0.1) / 0.8,
		rawI = x / width * (numPoints + 1) - 1,
		nearestI = Math.min(Math.max(0, Math.round(rawI)), numPoints - 1)
	return {
		i: nearestI,
		isNear: Math.abs(nearestI - rawI) < 0.1,
		value: Math.min(Math.max(0, value), 100)
	}
}

/**
 * @param {MouseEvent} event
 */
function handleMouseDown(event) {
	let {
		i, isNear
	} = fromCanvasXY(event.clientX, event.clientY)

	if (!isNear) {
		return
	}

	dragging = i
	handleMouseMove(event)
}

/**
 * @param {MouseEvent} event
 */
function handleMouseMove(event) {
	if (dragging === null) {
		return
	}

	points[dragging] = fromCanvasXY(event.clientX, event.clientY).value
	requestDraw()
}

/**
 * @param {MouseEvent} event
 */
function handleMouseUp(event) {
	handleMouseMove(event)
	dragging = null
}

/**
 * Schedule the drawing
 */
function requestDraw() {
	if (!waitingDraw) {
		waitingDraw = true
		window.requestAnimationFrame(draw)
	}
}