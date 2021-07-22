<h3 align="center">Vaccination System 1</h3>

<p align="center"> This is the first phase of a vaccination system for a health center
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Requirements](#requirements)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>
The purpose of this project is to let the Health Centers of a city have real-time information about the status of the vaccination campaign for covid-19.

## ✅ Requirements <a name = "requirements"></a>
The requirements for the functions made are:

- addPatient - Receives a patient and adds it to the list of health center patients. The list must be alphabetically sorted and the method should insert the new patient in its corresponding position. The patient is only added if it is not stored in the patient list. The method complexity should be n.

- searchPatients - Receives the parameters: year, covid and vaccine. And returns a new health center whose list of patients meets the search criteria defined by the input arguments of the function. The complexity must be n.

- statistics - Returns the following values: percentage of patients in a health center who have passed COVID-19, percentage of patients older than 70 years, percentage of patients who have not been vaccinated, percentage of patients older than 70 years who have not been vaccinated, percentage of patients who have received the first dose of the vaccine, percentage of patients who have received the second dose of the vaccine. The complexity must be n.

- merge - Receives an object of class HealthCenter, other and returns a new health center whose patient list includes those from the calling center and those from the other center. The complexity must be n.

- minus - Receives an object of class HealthCenter, other, and returns a new health center containing the patients from the invoking center, but these patients cannot belong to the other center. Complexity must be as efficient as possible

- inter - Receives an object of class HealthCenter, other, and returns a new health center whose patient list only includes those patients who belong to both health centers. Complexity must be as efficient as possible

## 👩‍💻 Usage <a name="usage"></a>
You can use it to storage the information about vaccines in your own Health Center, and also prove it goes well through the unittest.

## ⛏️ Built Using <a name = "built_using"></a>
- [Python](https://www.python.org/)
- [Unittest](https://docs.python.org/3/library/unittest.html)
- [TSV files](https://en.wikipedia.org/wiki/Tab-separated_values)

## ✍️ Authors <a name = "authors"></a>
- [@emelyalonzo](https://github.com/emelyalonzo) - Idea & Initial work 🖋️
