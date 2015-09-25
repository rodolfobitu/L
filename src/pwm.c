#include "pwm.h"
#include "L.h"

/* constant for PWM module activation */
#define PWM_MODE_MASK 	0x0C

void pwm_init(void) {
	/* configure PWM frequency for 46.875 kHz*/
	/* when 2 PWM are used, the frequency is the same for both */
	PR2 = 0xFF;		// TMR2 counter
	T2CON &= 0xFC;	// TMR2 prescaler configuration = 1
	
	/* configure initial duty cycle */
	pwm_setDutyCycle(PWM_LEFT, 0);
	pwm_setDutyCycle(PWM_RIGHT, 0);

	/* CCPxM3:CCPxM2 = 11 => PWM mode */
	CCP1CON |= PWM_MODE_MASK;
	CCP2CON |= PWM_MODE_MASK;
	 
	/* enable TMR2 */
	T2CONbits.TMR2ON = 1;
}

/* Set duty cycle (0 - 1023) */
void pwm_setDutyCycle(unsigned char ucDevice, unsigned int uiDutyCycle) {
	if (ucDevice == PWM_RIGHT) {
		CCPR1L = uiDutyCycle >> 2;
  		CCP1CONbits.DC1B = uiDutyCycle & 0b11;
 	}
 	
	if (ucDevice == PWM_LEFT) {
		CCPR2L = uiDutyCycle >> 2;
  		CCP2CONbits.DC2B = uiDutyCycle & 0b11;
 	}	
}