#ifndef MIN_PWM_H
#define MIN_PWM_H

/*
 * Run the min PWM calibration task, to gather:
 * - the least PWM value to make each motor start moving
 * - the least PWM value to make a moving motor stop
 */
void minPwm_run(void);

#endif /* MIN_PWM_H */