def km_to_m():
    km=float(input("Enter distance in kilometers : "))
    meter=km*1000
    print(f"Distance in metres : {meter} metres")
    
def m_to_km():
    meter=float(input("Enter distance in kilometers : "))
    km=meter/1000
    print(f"Distance in kilometers : {km} kilometers")
    
print("1. Convert Kilometers to Meter")
print("1. Convert Metres to Kilometer")

choice=int(input("Enter your choice (1 or 2): "))

if choice==1:
    km_to_m()
elif choice==2:
    m_to_km()
else:
    print("Invalid choice")
    

    
    
