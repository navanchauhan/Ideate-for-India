# Ideate-for-India

## Index
* [To-Do](#To-Do)
* [Problem](#Problem)
* [WorkFlow](#WorkFlow)
* [Solution](#Solution)
* [Modules](#Modules)
  * [Garuda](#Garuda)
  * [Sheesh](#Sheesh)
  * [Vasuki](#Vasuki)

----

## To-Do
- [x] Design AQI Monitoring Program
- [x] Design Autonomous Drone Program
- [x] Design Photocatalytic Purifier
- [ ] Build the modules

----

## Problem
Air Pollution is a huge issue in India, that is why I chose the theme 'Environment' to combat this issue

----

## WorkFlow

```
Logic Behind the workflow
```
![Logic](https://raw.githubusercontent.com/navanchauhan/Ideate-for-India/master/assets/logic.png)

----

## Solution
The National Air Monitoring Programme provides real-time access to the Air Quality Index, but currently there is no API that can be utilised to fetch data in the json format. Therefore I use the [WAQI's](https://waqi.info) API to fetch the air quality index. The air quality is assigned three colours:
* Red - For Harmful Air Quality
* Yellow - For Moderate to Unsatisfactory Air Quality
* Green - For Good Air Quality

```
Script demo here:
```
![Demo](https://raw.githubusercontent.com/navanchauhan/Ideate-for-India/master/assets/aqi.gif)

* If the major pollutant is PM2.5, it deploys the Garuda Drone Module which can efficiently reduce PM2.5 via HEPA filters
* If the major pollutant is dust and smoke, it deploys the Vasuki Drone Module, which is an Electro-Static Precipitator, which can efficiently reduce smoke and dust from industrial exhaust
* Depending on the intensity of the situation, it can trigger the Sheesh module, which are affixed to street lights and charge via solar-energy. These can also act as Air Quality monitoring stations

----

## Modules

It is a tri-fold modular solution. The Drone Modules are to be constructed using raspberry-pi zero or another suitable microcontroler (They are inherrently cheap). Because this is a modular solution, even if one module fails, the others can take over. For e.g If the DGCA doesn't allow the flight of drones temporarily, the Sheesh module can run for extra duration to compensate for them.

The base drone is fully autonomous and can be remotely controlled from anywhere, it uses magnets to align the modules with the correct port. **An alternative method is to have two seperate drones.** 

### Garuda Module
Garuda is going to be a mini drone with a DIY mini HEPA filter, which could suck in PM2.5 Pollutants

**Why HEPA?:** High Efficiency Patriculate Air Filter, can filter pollen, pet dander, dust mites, and tobacco smoke through a mechanical process wherein air is made to pass thorugh the filter. Researches have showed that HEPA filters are good at cleaning PM2.5 [1](https://www.sciencedirect.com/science/article/pii/S0048969717326426)

----

### Sheesh Module
It is a photocatalytic air purifier that can be attached to existing street-lights

**What is Photocatalytic Air Purifier?** Photocatalyic Air Purifiers use the power of light to convert nasty harmful air pollutants into harmless substances. 

**Don't Photocatalytic Air Purifiers produce Ozone?** They produce Ozone in minute quantities, and because this will be installed in streetlights, it would be away from the humans. 

----

### Vasuki Module
It is an Electro-Static Precipitator, it can remove fine particles like dust and smoke from the air. 

----
