b. Modify the Daily Life Magazine program so that it produces a count of
readers by gender within age group—that is, under-20 females, under-20 males,
and so on.declerations


	num age;
	num gender;
	num married;
	num income;

	num sub;
	num SIZE = 5;
	num reader_age_range[SIZE] = 0, 20, 30, 40, 50;
	num reader_age_count[SIZE];
	num reader_age_names[SIZE] = "under 20", "20-29", "30-39", 40-49", "50 & older";

	num reader_gender_male[SIZE];
	num reader_gender_famle[SIZE];

housekeeping()
	output "please enter readers, age, gender, marital status, and income";
	input age, gender, married, income;

detailLoop()
	while (age != QUIT) {
		sub = SIZE - 1;
		while (age < reader_age_range[SIZE]) {
			sub = sub - 1;
			}end while
		reader_age_count[sub] = reader_age_count[sub] + 1;
	//gender array addition
	if (gender = "male") {
		reader_gender_male[sub] = reader_gender_male[sub] + 1
	}
	else {
		reader_gender_female[sub] = reader_gender_female[sub] + 1
	}
	output "please enter readers, age, gender, marital status, and income";
	input age, gender, married, income;
	}end while

endoOfJob()
	sub = 0;
	while (sub < SIZE) {
		output "Number of readers in" + reader_age_name[sub] + " age group is " + reader_age_count[sub];
		output "Number of female readers in the" + reader_age_name[sub] + "age group is" + reader_gender_female[sub];
		output "Number of male readers in the" + reader_age_name[sub] + "age group is" + reader_gender_male[sub];
		
	sub = sub + 1;
	}end while

	output "thank you for using this program"