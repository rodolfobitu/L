#include "L.h"
#include "util.h"
#include "adc.h"
#include "pwm.h"
#include "timer0.h"
#include "pid.h"
#include "task/velocity.h"
#include "task/calibrate.h"
#include "task/position.h"
#include "task/pwmControl.h"
#include "task/velocityControl.h"

/*
 * GLOBALS
 */
volatile unsigned int uiTimer0_endPeriod = 0;	// cyclic executive flag
volatile unsigned int uiLeftCounter = 0;
volatile unsigned int uiRightCounter = 0;
float fLeftReference = 0;
float fRightReference = 0;

/* A value from -1 to 1 (0 = in the middle) */
float fPosition = 0;

/*
 * Calculated speed (averaged over VELOCITY_NUM_SAMPLES),
 * in encoder steps per second
 */
float fLeftSpeed = 0;
float fRightSpeed = 0;

/* Expected min (at 0) and max (at 1) values for each sensor */
unsigned int uiSensorLimits[NUM_OF_SENSORS][2];

/*
#pragma config FOSC   = HSPLL_HS
#pragma config PLLDIV = 5
#pragma config CPUDIV = OSC1_PLL2
#pragma config IESO   = OFF                    //Oscillator Switchover mode disabled
#pragma config PWRT   = ON                     //Power-up Timer enabled
#pragma config BOR    = ON                     //Brown-out Reset enabled
#pragma config BORV   = 0                      //Brown-out Reset to maximum setting
#pragma config WDT    = OFF                    //Watchdog timer disabled
#pragma config LVP    = OFF                    //Single-Supply ICSP disabled
*/

/* setup the interruption */
void isr_CyclicExecutive();
#pragma code high_vector=0x08
void isr_HighVector(void) {
	_asm GOTO isr_CyclicExecutive _endasm
}
#pragma code

/* setup the isr */
#pragma interrupt isr_CyclicExecutive
void isr_CyclicExecutive(void) {
	if (INTCONbits.TMR0IF) {
		/* set the cyclic executive flag */
		uiTimer0_endPeriod = 1;

		/* acknowledge the interrupt */
		INTCONbits.TMR0IF = 0;
	}
	
	if (INTCON3bits.INT1IF) {
		uiLeftCounter++;
		INTCON2bits.INTEDG1 = !INTCON2bits.INTEDG1;
		INTCON3bits.INT1IF = 0;
	}
	
	if (INTCON3bits.INT2IF) {
		uiRightCounter++;
		INTCON2bits.INTEDG2 = !INTCON2bits.INTEDG2;
		INTCON3bits.INT2IF = 0;
	}
}

void L_init(void) {
	/* clean all ports */
	PORTA = PORTB = PORTC = PORTD = PORTE = 0;

	LED_1_DIR = OUTPUT;
	LED_2_DIR = OUTPUT;
	LED_3_DIR = OUTPUT;
	LED_4_DIR = OUTPUT;

	LED_IR0_DIR = OUTPUT;
	LED_IR1_DIR = OUTPUT;
	LED_IR2_DIR = OUTPUT;
	LED_IR3_DIR = OUTPUT;
	LED_IR4_DIR = OUTPUT;
	LED_IR5_DIR = OUTPUT;

	/* Set up interruption bits */
	INTCON3bits.INT1IE = 1;
	INTCON3bits.INT2IE = 1;

	/* Set up (ponte H) pins */
	RIGHT_CW_DIR = OUTPUT;
	RIGHT_CCW_DIR = OUTPUT;
	LEFT_CW_DIR = OUTPUT;
	LEFT_CCW_DIR = OUTPUT;

	/* Set up motor pins */
	RIGHT_MOTOR_DIR = OUTPUT;
	LEFT_MOTOR_DIR = OUTPUT;

	RIGHT_MOTOR = 1;
	LEFT_MOTOR = 1;

	INTCONbits.GIE = 1;		// enables all unmasked interrupts
	INTCONbits.PEIE = 1;	// enables all unmasked peripheral interrupts
}

void main(void) {

	/* Hardware initialization */
	L_init();
	timer0_init();
	adc_init();
	pwm_init();

	/* Start-up Tasks */
	calibrate_run();

	/* Tasks initialization */
	pwmControl_init();
	velocityControl_init();
	
	/* main system loop, runs forever */
	timer0_config(100);
	while (1) {
		
		velocity_task();		
		
		position_task();

		velocityControl_task();
		
		pwmControl_task();
		
		/* Wait for period */
		while(!uiTimer0_endPeriod);
	
		timer0_reset();
	}
}