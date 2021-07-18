#include <iostream>
#include <cmath>
#include <string>

using namespace std;


// class Quaternion {
// 	/**
// 	Quaternion for rotation.

// 	Reference: https://www.gamasutra.com/view/feature/131686/rotating_objects_using_quaternions.php

// 	Q = w + ix + jy + kz
// 	**/	
// protected:
// 	// Easy access components
// 	double* values[4] = {&w, &x, &y, &z};

// 	// Quaternion dot(Quaternion q){
// 	// 	/**
// 	// 	Dot product between the non-real parts of a Quaternion.
// 	// 	**/

// 	// 	Quaternion Q;
// 	// 	for(int i = 1; i < 4; i++){
// 	// 		Q.w = *values[i] * *(q.values)[i];
// 	// 	}

// 	// 	return Q;
// 	// }

// 	// Quaternion dot(Quaternion p, Quaternion q){
// 	// 	/**
// 	// 	Dot product between the non-real parts of a Quaternion.
// 	// 	**/

// 	// 	Quaternion Q;
// 	// 	for(int i = 1; i < 4; i++){
// 	// 		Q.w = *(p.values)[i] * *(q.values)[i];
// 	// 	}

// 	// 	return Q;
// 	// }

// 	// Quaternion cross(Quaternion q){
// 	// 	/**
// 	// 	Cross product between non-real parts of a Quaternion.
// 	// 	**/

// 	// 	Quaternion Q(0, 0, 0, 0);

// 	// 	Q.x = y * q.z - z * q.y;
// 	// 	Q.y = z * q.x - x * q.z;
// 	// 	Q.z = x * q.y - y * q.x;

// 	// 	return Q;
// 	// }

// 	// Quaternion cross(Quaternion p, Quaternion q){
// 	// 	/**
// 	// 	Cross product between non-real parts of a Quaternion.
// 	// 	**/

// 	// 	Quaternion Q(0, 0, 0, 0);

// 	// 	Q.x = p.y * q.z - p.z * q.y;
// 	// 	Q.y = p.z * q.x - p.x * q.z;
// 	// 	Q.z = p.x * q.y - p.y * q.x;

// 	// 	return Q;
// 	// }

// 	// Quaternion real(Quaternion q){
// 	// 	Quaternion re(0, 0, 0, 0);
// 	// 	re.w = q.w;
// 	// 	return re;
// 	// }

// 	// Quaternion imaginary(Quaternion q){
// 	// 	Quaternion im(0, 0, 0, 0);
// 	// 	for(int i = 1; i < 4; i++){
// 	// 		*(im.values)[i] = *(q.values)[i];
// 	// 	}
// 	// 	return im;
// 	// }


// public:
// 	double w = 1; 	// Real
// 	double x = 0;	// i-component
// 	double y = 0;	// j-component
// 	double z = 0;	// k-component

// 	Quaternion(double w_=1, double x_=0, double y_=0, double z_=0){
// 		this->w = w_;
// 		this->x = x_;
// 		this->y = y_;
// 		this->z = z_;
// 	}

// 	Quaternion operator+(const Quaternion& q){
// 		Quaternion r;
// 		for(int i = 0; i < 4; i++){
// 			// values is protected though...
// 			*(r.values)[i] = *(this->values)[i] + *(q.values)[i];
// 		}
// 		return r;
// 	}

// 	Quaternion& operator+=(const Quaternion& q){
// 		Quaternion::add(q);
// 		return *this;
// 	}

// 	Quaternion& operator+=(const double a){
// 		Quaternion::add(a);
// 		return *this;
// 	}

// 	Quaternion operator*(const Quaternion& q){
// 		Quaternion r;

// 		r.w = this->w * q.w - this->x * q.x - this->y * q.y - this->z * q.z;
// 		r.x = this->w * q.x + this->x * q.w + this->y * q.z - this->z * q.y;
// 		r.y = this->w * q.y + this->y * q.w + this->z * q.x - this->x * q.z;
// 		r.z = this->w * q.z + this->z * q.w + this->x * q.y - this->y * q.x;

// 		return r;
// 	}

// 	void add(Quaternion q){			// Legal? Ideally return Quaternion Q = q + q'
// 		for(int i = 0; i < 4; i++){
// 			*(this->values)[i] += *(q.values)[i];
// 		}
// 	}

// 	void add(double a){
// 		/**
// 		Add to the scalar part of the quaternion.
// 		**/
// 		this->w += a;
// 	}


// 	void multiply(double a){
// 		/**
// 		Scalar multiply.
// 		**/
// 		for(int i = 0; i < 4; i++){
// 			*(this->values)[i] *= a;
// 		}
// 	}

// 	void multiply(Quaternion q){
// 		double w_ = this->w * q.w - this->x * q.x - this->y * q.y - this->z * q.z;
// 		double x_ = this->w * q.x + this->x * q.w + this->y * q.z - this->z * q.y;
// 		double y_ = this->w * q.y + this->y * q.w + this->z * q.x - this->x * q.z;
// 		double z_ = this->w * q.z + this->z * q.w + this->x * q.y - this->y * q.x;

// 		this->w = w_;
// 		this->x = x_;
// 		this->y = y_;
// 		this->z = z_;
// 	}

// 	void conjugate(){
// 		for(int i = 1; i < 4; i++){
// 			*(this->values)[i] *= -1;
// 		}
// 	}

// 	double norm(){
// 		/**
// 		Find the norm of the Quaternion.
// 		**/
// 		double norm = 0;
// 		for(int i = 0; i < 4; i++){
// 			norm += *(this->values)[i] * *(this->values)[i];		// Error?
// 		}
// 		norm = sqrt(norm);

// 		return norm;
// 	}

// 	void normalize(){
// 		double norm = Quaternion::norm();
// 		for(int i = 0; i < 4; i++){
// 			*(this->values)[i] /= norm;
// 		}
// 	}



// 	void additive_identity(){
// 		/**
// 		Sets to additive identity.
// 		**/
// 		for(int i = 0; i < 4; i++){
// 			*values[i] = 0;
// 		}
// 	}

// 	void multiplicative_identity(){
// 		/**
// 		Sets to multiplicative identity.
// 		**/
// 		w = 1;
// 		for(int i = 1; i < 4; i++){
// 			*(this->values)[i] = 0;
// 		}
// 	}

// 	void print(){
// 		cout << w;
// 		if(x >= 0){
// 			cout << " + i" << x;
// 		}else{
// 			cout << " - i" << -x;
// 		}

// 		if(y >= 0){
// 			cout << " + j" << y;
// 		}else{
// 			cout << " - j" << -y;
// 		}

// 		if(z >= 0){
// 			cout << " + k" << z;
// 		}else{
// 			cout << " - k" << -z;
// 		}

// 		cout << "\n";
// 	}
// };


class Quaternion{
protected:
	double w = 1, x = 0, y = 0, z = 0;
	double* values[4] = {&w, &x, &y, &z};

public:
	Quaternion(double w = 1, double x = 0, double y = 0, double z = 0){
		this->w = w;
		this->x = x;
		this->y = y;
		this->z = z;
	}

	// Display
	void print(){
		cout << w;
		this->x >= 0 ? cout << " + i" << x : cout << " - i" << -x;

		// if(x >= 0){cout << " + i" << x;}
		// else{cout << " - i" << -x;}

		if(y >= 0){cout << " + j" << y;
		}else{
			cout << " - j" << -y;
		}

		if(z >= 0){
			cout << " + k" << z;
		}else{
			cout << " - k" << -z;
		}

		cout << "\n";
	}


	// Functions upon itself
	static Quaternion zero(){
		Quaternion Q(0, 0, 0, 0);

		return Q;
	}

	static Quaternion one(){
		Quaternion Q(1, 0, 0, 0);

		return Q;
	}

	Quaternion real(){
		Quaternion Q(0, 0, 0, 0);
		Q.w = this->w;		// Why can we access Q's 'w' value?
		return Q;
	}

	Quaternion imaginary(){
		Quaternion Q(0, 0, 0, 0);
		for(int i = 1; i < 4; i++){
			*(Q.values)[i] = *(this->values)[i];
		}
		return Q;
	}

	double norm(){
		double norm = 0;

		for(int i = 0; i < 4; i++){
			norm += *(this->values)[i] * *(this->values)[i];
		}
		norm = sqrt(norm);

		return norm;
	}

	Quaternion normalize(){
		Quaternion Q(0, 0, 0, 0);
		double norm = Quaternion::norm();

		for(int i = 0; i < 4; i++){
			*(Q.values)[i] = *(this->values)[i] / norm;
		}

		return Q;
	}

	Quaternion& self_normalize(){
		double norm = Quaternion::norm();

		for(int i = 0; i < 4; i++){
			*(this->values)[i] /= norm;
		}

		return *this;
	}

	Quaternion conjugate(){
		Q = Quaternion(0, 0, 0, 0);

		for(int i = 1; i < 4; i++){
			*(Q.values)[i] = *(this->values)[i];
		}

		return Q;
	}

	Quaternion& self_conjugate(){
		for(int i = 1; i < 4; i++){
			*(this->values)[i] *= -1;
		}

		return *this;
	}

	Quaternion invert(){
		Q = Quaternion(0, 0, 0, 0);
		Q = Quaternion::conjugate();
		Q = Quaternion::multiply(1 / Quaternion::norm());

		return Q;
	}

	Quaternion& self_invert(){
		// Why do these work?
		Quaternion::self_conjugate();
		Quaternion::multiply(1 / norm());
	}


	// Quaternion-Quaternion Math
	static Quaternion add(Quaternion& p, Quaternion& q){
		Quaternion Q(0, 0, 0, 0);

		cout << "Q = "; Q.print();

		cout << "p = "; p.print();
		cout << "q = "; q.print();

		for(int i = 0; i < 4; i++){
			*(Q.values)[i] = *(p.values)[i] + *(q.values)[i];
			cout << *(Q.values)[i] << " = " << *(p.values)[i] << " + " << *(q.values)[i] << "\n";
		}

		Q.print();

		return Q;
	}

	static Quaternion multiply(const Quaternion p, const Quaternion q){
		Quaternion Q(0, 0, 0, 0);

		Q.w = p.w * q.w - p.x * q.x - p.y * q.y - p.z * q.z;
		Q.x = p.w * q.x + p.x * q.w + p.y * q.z - p.z * q.y;
		Q.y = p.w * q.y + p.y * q.w + p.z * q.x - p.x * q.z;
		Q.z = p.w * q.z + p.z * q.w + p.x * q.y - p.y * q.x;

		return Q;
	}

	Quaternion& add(const Quaternion q){
		for(int i = 0; i < 4; i++){
			*(this->values)[i] += *(q.values)[i];
		}
		return *this;
	}

	Quaternion& multiply(const Quaternion q){
		double w_ = this->w * q.w - this->x * q.x - this->y * q.y - this->z * q.z;
		double x_ = this->w * q.x + this->x * q.w + this->y * q.z - this->z * q.y;
		double y_ = this->w * q.y + this->y * q.w + this->z * q.x - this->x * q.z;
		double z_ = this->w * q.z + this->z * q.w + this->x * q.y - this->y * q.x;

		this->w = w_;
		this->x = x_;
		this->y = y_;
		this->z = z_;

		return *this;
	}

	Quaternion operator +(const Quaternion& q){
		Quaternion Q(0, 0, 0, 0);
		for(int i = 0; i < 4; i++){
			// values is protected though...
			*(Q.values)[i] = *(this->values)[i] + *(q.values)[i];
		}
		return Q;
	}

	// Scalar Math
	Quaternion& add(double a){
		this->w += a;

		return *this;
	}

	Quaternion& multiply(double a){
		for(int i = 0; i < 4; i++){
			*(this->values)[i] *= a;
		}

		return *this;
	}
};

void test_quaternions(){
	Quaternion Q(1, 2, 3, 4);
	Quaternion P(2, 3, 4, 5);

	Q.print();
	P.print();
	cout << '\n';

	P = Q.real();
	Q.print();
	P.print();
	cout << '\n';

	P = Q.imaginary();
	Q.print();
	P.print();
	cout << '\n';

	Quaternion R;
	R = P.add(P, Q);
	R.print();
	Q.print();
	P.print();
	cout << '\n';

	R = Q + P;
	R.print();
	Q.print();
	P.print();
	cout << '\n';

	// Q += P;

	// Q.print();
	// P.print();

	// Q.invert() * ;
	// Q.print();
	// P.print();
}



int main(){
	test_quaternions();
	
	return 0;
}