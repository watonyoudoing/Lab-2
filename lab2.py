



def display_main_menu():
    print ("this is america")

def get_user_input():
       x= input(" Enter the number of element ")
       y = x.split(",")
       y= list(map(int, y))
       print(y)
       return(y)
def calc_average_temperature(Temp):
    Total=sum(Temp)
    print(Total)

def calc_min_max_temperature(Temp):
    biggest= Temp[0]
    smallest= Temp[0]
    for i in range(len(Temp)):
        if biggest<Temp[i]:
            biggest=Temp[i]
        elif smallest>Temp[i]:
            smallest=Temp[i]
    return(biggest,smallest)




def main():
    print("xd")
    display_main_menu()
    Temp = get_user_input()
    calc_average_temperature(Temp)
    print(calc_min_max_temperature(Temp))
if __name__ == "__main__":
  main()








