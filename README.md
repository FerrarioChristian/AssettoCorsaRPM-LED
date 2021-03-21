# AssettoCorsaRPM-LED

A python script that changes led strips color to match the Assetto Corsa car engine RPM.

## Description

Simple python script that access the Assetto Corsa shared memory, retrieving the car engine RPM, changing the LED strip color fading from green to red when it's needed to shift gear.  
The LED strip will turn purple when you hit the engine limiter.

> 20/03/2021 - The LED interface is based on [TinyTuya](https://github.com/jasonacox/tinytuya), a python module to communicate with the Tuya API.  
> This is temporary, the LED controller will be a microcontroller asap, due to the fact that too many color change in little time make the device crash.
## How To Setup

## How To Fix Values For Specific Cars

## Credits
Thanks to @jasonacox for writing the [TinyTuya](https://github.com/jasonacox/tinytuya) module.

## Future Updates
- [ ] Arduino as the LED controller, so that it does not crash when too many color change occur in short time.
- [ ] List of cars to choose so that you dont need to manually adjust RPM values for different car engines.
- [ ] _Game already opened?_ functio, so that the script rembmers you to open the game before launching it.