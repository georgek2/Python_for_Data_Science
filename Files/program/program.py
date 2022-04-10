

def file_handler():
    with open('first.txt', 'r') as file:
        data = file.readlines() # Read all the data in the file
        
        names = []
        designations = []
        total_exp = []
        r_hourly_rate = []
        o_hourly_rate = []
        w_hourly_rate = []

        for line in data[1:]: # Grab individual pieces of data from each line
            name = line.split(',')[0]
            designation = line.split(',')[1]
            Total_Exp = line.split(',')[2]
            Regular_Hourly_rate = line.split(',')[3]
            Overtime_Hourly_rate = line.split(',')[4]
            Weekend_Hourly_rate = line.strip().split(',')[5]
            # Append each each piece to tha corresponding list
            names.append(name)
            designations.append(designation)
            total_exp.append(Total_Exp)
            r_hourly_rate.append(Regular_Hourly_rate)
            o_hourly_rate.append(Overtime_Hourly_rate)
            w_hourly_rate.append(Weekend_Hourly_rate)

    with open('second.txt', 'r') as file:
        data = file.readlines()
        r_hours = []
        w_hours = []
        o_hours = []
        for line in data[1:]:
            Regular_Hours = line.split(',')[1]
            Weekend_Hours = line.split(',')[2]
            Overtime_Hours = line.strip().split(',')[3]

            r_hours.append(Regular_Hours)
            w_hours.append(Weekend_Hours)
            o_hours.append(Overtime_Hours)

    return names, designations, total_exp, r_hourly_rate,\
         o_hourly_rate, w_hourly_rate, r_hours, w_hours, o_hours


def main():
    names, designations, total_exp, r_hourly_rate,\
        o_hourly_rate, w_hourly_rate, r_hours, w_hours, o_hours = file_handler()
    Regular_Hourly_Total_Pay = []
    Weekend_Hourly_Total_pay = []
    Overtime_Hourly_Total_pay = []
    Overall_Total_pay = []

    for r_h_r, r_h, o_h_r, o_h, w_h_r, w_h in\
        zip(r_hourly_rate, r_hours, o_hourly_rate, o_hours, w_hourly_rate, w_hours):
        r_tp = int(r_h_r) * int(r_h)
        o_tp = int(o_h_r) * int(o_h)
        w_tp = int(w_h_r) * int(w_h)

        Regular_Hourly_Total_Pay.append(r_tp)
        Weekend_Hourly_Total_pay.append(w_tp)
        Overtime_Hourly_Total_pay.append(o_tp)

        total_pay = r_tp + w_tp + o_tp

        Overall_Total_pay.append(total_pay)

    with open('Third.txt', 'a') as file:
        file.write('Name, Designation, Total_Exp, Regular_Hours, Regular_Hourly_rate, ')
        file.write('Regular_Hour_Total_pay, Weekend_Hours, Weekend_Hourly_rate, Weekend_Hourly_Total_pay, ')
        file.write('Overtime_Hours, Overtime_Hourly_rate, Overtime_Hourly_Total_pay, Overall_Total_pay')
        
        for p, d, t_e, r_h, r_h_r, r_tp, w_h, w_h_r, w_tp, o_h, o_hr, o_tp, tp,  in \
            zip(names, designations, total_exp, r_hours, r_hourly_rate, Regular_Hourly_Total_Pay, \
                w_hours, w_hourly_rate, Weekend_Hourly_Total_pay, o_hours, o_hourly_rate, \
                    Overtime_Hourly_Total_pay, Overall_Total_pay):

            file.write(f'\n{p},')
            file.write(f'{d},')
            file.write(f'{t_e},')
            file.write(f'{r_h},')
            file.write(f'{r_h_r},')
            file.write(f' {str(r_tp)},')
            file.write(f'{w_h},')
            file.write(f'{w_h_r},')
            file.write(f' {str(w_tp)},')
            file.write(f'{o_h},')
            file.write(f'{o_hr},')
            file.write(f' {str(o_tp)},')
            file.write(f' {str(tp)}')

if __name__ == '__main__':

    main()

    print('Thank you for running the program!')

