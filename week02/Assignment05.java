class Employee {
private:
    int id;
    string name;
    string department;
    bool isWorkingStatus;

public:
    bool isWorking() const {
        return isWorkingStatus;
    }

    void terminate() {
        isWorkingStatus = false;
    }
};

class EmployeeRepository {
public:
    void saveEmployeeToDatabase(const Employee& employee) { }
};

class EmployeeReportService {
public:
    void printEmployeeReportXml(const Employee& employee) { }
    void printEmployeeReportCsv(const Employee& employee) { }
};
