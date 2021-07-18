/*
Physics Engine for a Starship.

Started: 2020-10-24 because I was bored
*/

#include <iostream>
#include <string>
#include <cmath>

template <class T>
class triple {
protected:
	T values[3] = {0, 0, 0};

public:
	T& a = values[0];
	T& b = values[1];
	T& c = values[3];

	triple (T a=0, T b=0, T c=0) {
		values[0] = a;
		values[1] = b;
		values[2] = c;
	}

	void set (T a, T b, T c) {
		values[0] = a;
		values[1] = b;
		values[2] = c;
	}

	void set (int i, T value) {
		/**
		Set values[i] to input value if i is in {0, 1, 2}.
		*/
		if (i < 0) {} else if (i > 2) {	// Do nothing
		} else {
			this->values[i] = value;
		}
	}

	void set (T value) {
		/**
		Set all values to input value.
		*/
		for(int i = 0; i < 3; i++){
			this->values[i] = value;
		}
	}

	void zero (int i) {
		/**
		Zero value i if i is in {0, 1, 2}
		*/
		this->set(i, 0);
	}

	void zero () {
		/**
		Zero all values.
		*/
		this->set(0);
	}

	void print () {
		std::cout << "(" << this->a << ", " << this->b << ", " << this->c << ")" << std::endl;
	}
}


class Starship {
/**
A generalstarship class. Defines a starship with properties for linear movement and rotation.

Carries physical properties.
**/

protected:
	// Static logistics
	unsigned short int size = 0; 			// Not implemented - use as shape vector
	unsigned int mass = 1000;				// kg
	unsigned int second_moment_of_inertia[3] = {1, 1, 1};
	
	// Maximum values
	unsigned short int max_crew = 100; 			// Crew
	unsigned int max_fuel = 10000;
	unsigned int max_forward_force = 1000;
	unsigned int max_torque = 100;
	
	// Movement logistics
	double thrust = 0; 					// Between (0, 1), what ratio of the throttle is on
	double engine_efficiency = 1;		// Rate of fuel burn

	// Adaptive logistics
	unsigned short int crew = 100;

public:
	// Logistics
	string ship_name;

	// Straight-line flight
	triple<int> position (0, 0, 0);
	triple<int> velocity (0, 0, 0);
	triple<int> acceleration (0, 0, 0);
	// int position[3] = {0, 0, 0};			// m
	// int velocity[3] = {0, 0, 0}; 			// m/s
	// int acceleration[3] = {0, 0, 0};		// m/s^2 - determined by thrust

	
	// Rotations - defined about positive - in arcseconds (360 degrees = 360 * 60 arcminutes = 360 * 60 * 60 arcseconds)
	// Need multiple points to define 3D object
	int angular_position[3] = {0, 0, 0};		// m
	int angular_velocity[3] = {0, 0, 0};		// m/s
	int angular_acceleration[3] = {0, 0, 0};	// m/s^2

	Starship(string name="None"){
		this->ship_name = name;
	}

	void accelerate(double thrust=1){
		/**
		Accelerate the ship by increasing thrust. Uses Newton's a = F/m. More thrust results in more fuel usage.
		**/

		// Check if fuel -- else return
		if (this->fuel == 0) {
			return;
		}

		// Cap thrust between (0, 1)
		if(thrust > 1){
			this->thrust = 1;
		}else if(thrust < 0){
			this->thrust = 0;
		}else{
			this->thrust = thrust;
		}

		for(int i=0;i<3;i++){
			this->acceleration[i] = std::round(this->thrust / this->mass * this->max_forward_force * this->angular_position[i]);
		}
	}

	void time_step(double dt=1){
		/**
		Move the ship one time step, burn fuel
		:param dt: time step, s
		**/

		// Move ship's location
		for(int i = 0; i < 3; i++){
			this->position[i] += std::round(this->velocity[i] * dt + 1/2 * this->acceleration[i] * dt * dt);
		}

		// Rotate ship
		// Use quaternions

		// Update fuel
		if(this->fuel == 0){
			this->acceleration.zero();
		}
	}

	void print_statistics(){
		std::cout << "STATISTICS OF " << this->ship_name << std::endl;
		// Static statistics
		std::cout << "mass = " << this->mass;
		std::cout << "max forward force = " << this->max_forward_force << std::endl;
		std::cout << "";
		
		// Linear statistics
		std::cout << "--- LINEAR STATISTICS ---" << std::endl;
		std::cout << "position = ";
		this->position.print();  			// << this->position[0] << ", " << this->position[1] << ", " << this->position[2] << ")" << std::endl;
		std::cout << "velocity = "; 
		this->velocity.print(); 			// << this->velocity[0] << ", " << this->velocity[1] << ", " << this->velocity[2] << ")" << std::endl;
		std::cout << "acceleration = ";
		this->acceleration.print();		// << this->acceleration[0] << ", " << this->acceleration[1] << ", " << this->acceleration[2] << ")" << std::endl;


	}
}

class Enterprise: public Starship {
public: 
	string allegiance = "Federation";


}

int main(){
	std::cout << "Hello World!";
	return 0;
}