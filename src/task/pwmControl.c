#include "L.h"
#include "pwm.h"
#include "pid.h"

#define VELOCITY_MAX_RIGHT 45.0
#define VELOCITY_MAX_LEFT 39.0
#define PWM_MIN 650.0

/* Input data */
extern float fLeftReference;
extern float fRightReference;
extern float fLeftSpeed;
extern float fRightSpeed;

PID pidLeft, pidRight;

void pwmControl_init(void) {
	float fPLeft = (1023.0 - PWM_MIN) / VELOCITY_MAX_LEFT;
	float fPRight = (1023.0 - PWM_MIN) / VELOCITY_MAX_RIGHT;

	pwm_setDirection(PWM_RIGHT, PWM_FORWARD);
	pwm_setDirection(PWM_LEFT, PWM_FORWARD);
	
	pidLeft = pid_init(fPLeft, fPLeft / 10.0, 0.0, 0.0, 1023.0 - PWM_MIN);
	pidRight = pid_init(fPRight, fPRight / 10.0, 0.0, 0.0, 1023.0 - PWM_MIN);
}

void pwmControl_task(void) {
 	pwm_setDutyCycle(PWM_LEFT, PWM_MIN + pid_update(&pidLeft, fLeftReference, fLeftSpeed));
	pwm_setDutyCycle(PWM_RIGHT, PWM_MIN + pid_update(&pidRight, fRightReference, fRightSpeed));
}
