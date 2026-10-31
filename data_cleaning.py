

def main():
    data = open("DIS_data", mode="w")
            
    if data != None:
        print("Data available!")

    for row in data:
        price,close,dividends,high,low,open_price,close_price,splits,volume = row.split(",")
        split = 0
        if splits != 0:
            split += 1

    print(split)
    data.close()
    

if __name__=="__main__":
    main()