#include "L.h"
#include "pwm.h"
#include "adc.h"
#include "timer0.h"

extern volatile unsigned int uiTimer0_endPeriod;

void calibrate_init(void){
	int i;
	unsigned int uiMin[6];
	unsigned int uiMax[6];

	for (i = 0; i < 6 ; i++){
		uiMin[i] = 1024;
		uiMax[i] = 0;		
	}

	pwm_setDutyCycle(PWM_LEFT, 800);
	pwm_setDutyCycle(PWM_RIGHT, 0);
	
	timer0_config(3000);
	while (!uiTimer0_endPeriod){
	/* prepara os adc e vai vendo */
		for (i = 0; i < 6 ; i++){
			unsigned int temp;
			
			temp = adc_get(i);
			if (temp < uiMin[i]){
				uiMin[i] = temp;
			}
			if (temp > uiMax[i]){
				uiMax[i] = temp;
			}
		}
	}

}