class File_Interactions:
    def __init__(self, _id, _departure, _arriving, _number_of_passengers)
        self.id = _id 
        self.departure = _departure
        self.arriving = _arriving
        self.number_of_passengers = _number_of_passengers

    def read_input_file():
        input_file = open("datos_vuelos.csv", "r") 
        lines_in_file = input_file.readlines()  
        input_file.close()  
        lines_in_file.pop(0)  
        return lines_in_file  

    def convert_plate_to_country(plate):
        plates = {  
            "D": "Alemania",
            "PP": "Brasil",
            "CF": "Canadá",
            "A7": "Catar",
            "CC": "Chile",
            "B": "China",
            "OY": "Dinamarca",
            "HC": "Ecuador",
            "A6": "Emiratos Árabes",
            "EC": "España",
            "N": "Estados Unidos",
            "PK": "Indonesia",
            "JA": "Japón",
            "XA": "México",
            "9V": "Singapur",
            "HS": "Tailandia"
        }

        for i in range(3, 0, -1):  
            plate_prefix = plate[0:i]  
            if plate_prefix in plates.keys():  
                country = plates[plate_prefix] 
                print("Country found for prefix ", plate_prefix, "is ", country)
                return country  

        return "Otro" 


    def convert_date_to_month(date):
        months = {  
            "01": "Enero",
            "02": "Febrero",
            "03": "Marzo",
            "04": "Abril",
            "05": "Mayo",
            "06": "Junio",
            "07": "Julio",
            "08": "Agosto",
            "09": "Septiembre",
            "10": "Octubre",
            "11": "Noviembre",
            "12": "Diciembre"
        }

        month_number = date[3:5] 

        if month_number in months.keys():  
            month_name = months[month_number]  
            print("Month name found for month number ", month_number, "is ", month_name)
            return month_name  

        return "Otro"  


    def process_input_data(input_lines):
        total_per_month = {}  
        total_per_month_per_country = {}  

        for line in input_lines:  
            fields = line.split(",")  
            plate = fields[0]  
            departure_date = fields[1]  
            country = convert_plate_to_country(plate)  
            month = convert_date_to_month(departure_date)  

            if month not in total_per_month.keys():  
                total_per_month[month] = 1  
            else:
                total_per_month[month] += 1  

            if month not in total_per_month_per_country.keys(): 
                total_per_month_per_country[month] = {country: 1} 
                if country not in total_per_month_per_country[month]: 
                    total_per_month_per_country[month][country] = 1  
                else: 
                    total_per_month_per_country[month][country] += 1  

        print("Total per month: ", total_per_month)
        print("Total per month per country: ", total_per_month_per_country)

        return total_per_month, total_per_month_per_country  

    
