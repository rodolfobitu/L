#include "L.h"
#include "pid.h"

/* Velocity_avg must be less than half of minimum maximum velocity */
#define VELOCITY_AVG 8.89

/* Input data */
extern float fPosition;

/* Output data */
extern float fLeftReference;
extern float fRightReference;

PID pid;

void velocityControl_init(void) {
	float fP = 2 * VELOCITY_AVG / 1.0;
	pid = pid_init(2 * fP, fP / 60.0, 0.0, -2.5 * VELOCITY_AVG, 2.5 * VELOCITY_AVG);
}

void velocityControl_task(void) {
	float fDiffVelocity;

	fDiffVelocity = pid_update(&pid, 0.0, fPosition);

	fLeftReference = VELOCITY_AVG - fDiffVelocity / 2.0;
	fRightReference = VELOCITY_AVG + fDiffVelocity / 2.0;
}
