#ifndef PWM_H
#define PWM_H

#define PWM_LEFT 0
#define PWM_RIGHT 1

#define PWM_FORWARD 1
#define PWM_BACKWARDS 0

void pwm_init(void);
void pwm_setDutyCycle(unsigned char ucDevice, unsigned int uiDutyCycle);
void pwm_setDirection(unsigned char ucDevice, char foward);

#endif /* PWM_H */
