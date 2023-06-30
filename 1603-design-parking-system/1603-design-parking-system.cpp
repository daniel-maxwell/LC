class ParkingSystem {
public:
    int Big;
    int Med;
    int Small;
    ParkingSystem(int big, int medium, int small) {
        Big = big;
        Med = medium;
        Small = small;
    }

    bool addCar(int carType) {
        switch (carType) {
            case 1:
                if (Big > 0) {
                    --Big;
                    return true;
                }
                return false;
            case 2:
                if (Med > 0) {
                    --Med;
                    return true;
                }
                return false;

            case 3:
                if (Small > 0) {
                    --Small;
                    return true;
                }
                return false;

            default:
                return false;
        }
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */