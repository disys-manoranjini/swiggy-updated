user=int(input("enter the choice of rating 1 to 5"))
data=filter(lambda x: x["rating"]==user,[{"name":"sangeetha","biriyani":345,"rating":5,"pref":"veg"},
                                     {"name":"thalabakatt9i","biriyani":345,"rating":4,"pref":"nonveg"},
                                     {"name":"buhari","biriyani":345,"rating":3,"pref":"nonveg"},
                                     {"name":"subway","biriyani":345,"rating":2,"pref":"nonveg"},
                                     {"name":"merit","biriyani":345,"rating":1,"pref":"nonveg"},
                                     {"name":"annapurana","biriyani":345,"rating":5,"pref":"nonveg"},
                                     {"name":"sai","biriyani":345,"rating":4,"pref":"veg"}])


swiggyorder = {"sangeetha":{"rating":5,"spl parotta":15,"chicken parotta":120,"mutton parota":190,"pepper mutton":145,"nalli soup":50,"kaal kolambu":100,"brain roast":200,"liver roast":240},
"thalabakatt9i":{"rating":4,"egg parotta":80,"chicken parotta":100,"full grill":100,"half grill":55,"leg fry":100,"egg kuruma":100,"chicken wings":200,"chicken friedrice":70,"green chicken":250,"soup":100,"egg fried rice":50},
"buhari":{"rating":3,"chilli parotta":70,"veg meals":90,"carrot rice":45,"beetroot rice":100,"spinach rice":80,"beabs rice":55,"carrot alwa":60,"beetroot alwa":80},
"subway":{"rating":2,"prawn briyani":120,"fish briyani":150,"beef briyani":150," turkey briyani":190,"duck briyani":145,"egg briyani":55,"country chicken briyani":180,"plain briyani":100,"rabbit briyani":140},
"merit":{"rating":1,"Fish curry":50,"fish fried rice":90,"chicken fried rice":145,"mutton fried rice":150,"egg fried rice":80,"veg fried rice":70,"birinji":60,"fish grill":100,"chicken toast":200},
"annapurana":{"rating":5,"egg veechu parotta":80,"chicken veechu parotta":100,"full meals(veg)":100,"half meals(veg)":55,"full meals(non veg)":100,"egg vadiyal":30,"chicken leg":100,"chicken wings":70,"green rice":250,"mutton soup":100,"chicken fried rice":50},
"sai":{"rating":4,"green chicken":90,"mutton chukka":145,"chicken chukka":150,"leaf parotta":140,"oil parotta":20,"egg parotta":60,"kerala parotta":50,"gopi manchurian":90,"chicken manjurian":100}}


ordering={}
class Hotels:
    

    def __init__(self):
        print("Hotels available")
        for  i in data:
            print(i)
       
        self.hotelname=input("Enter your faverout hotel name : ")
        
    def menu(self):
        if isinstance(self.hotelname,str):
            if self.hotelname in swiggyorder:
                hotel=self.hotelname
                value=swiggyorder.get(self.hotelname)
                for i,j in value.items():
                    print(f"{i} : {j}")
                    
            else:
                raise ValueError("sorry detailes unavailable")

        else:
            raise TypeError("invalid type data")

    def ordering(self):
        print("here is your Booking details")
        inpt=input("continue ordering : yes or no ? ")
        if inpt == "yes":
            items=input("number of dishes : ")
            if int(items)>0 and int(items)<15:
                for i in range(int(items)):
                    dish=input("Enter your fav dish name : ")
                    if(dish in swiggyorder[self.hotelname]):
                        quantity=input(f"Enter Quantity : ")
                        ordering[dish]=quantity
                    else:
                        raise ValueError("its an value error")
            else:
                raise ValueError("invalid value occrence")
        else:
            print("Thank you")

    def bill(self):
        amount=0
        for i,j in ordering.items():
            val=swiggyorder[self.hotelname]
            amount=val[i]*int(j)
            print("your ordered confirmed")
            print(f"total bill amount : {amount}")
            print("Thank you for using swiggy")
              
            
        
            
        
            
        
food=Hotels()
food.menu()
food.ordering()
food.bill()
