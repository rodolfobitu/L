#ifndef PWM_H
#define PWM_H

#define PWM_LEFT 0
#define PWM_RIGHT 1

void pwm_init(void);
void pwm_setDutyCycle(unsigned int uiDutyCycle, unsigned char ucDevice);

#endif /* PWM_H */
