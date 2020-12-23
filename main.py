from starship.starship import Starship


if __name__ == '__main__':
    a = Starship()
    a.get_position(True)
    print('\n\n')
    a.step(dt=1)
    a.get_position(True)
    print('\n\n')
    a.accelerate(fuel=1)
    a.get_thrust(True)
    a.step()
    a.get_acceleration(True)
    a.get_velocity(True)
    a.get_position(True)
    a.get_thrust(True)
    print('\n\n')
    a.step()
    a.get_acceleration(True)
    a.get_velocity(True)
    a.get_position(True)
    a.get_thrust(True)

    print('\n\n')
    a.accelerate(1)
    a.get_acceleration(True)
    a.step()

    # a.plot()
    for i in range(98):
        a.accelerate(1)
        a.step()

    for i in range(50):
        a.step()

    a.plot()