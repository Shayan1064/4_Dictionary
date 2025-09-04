dic1={"Shayan":34,
      "Noman":35,
      "Hmadna":35,
      "Nomii kahan":34,
      }

dic2={"Saddam":34,
      "Saadat":35,
      "Ayyan":35,
      "Kumar kahan":34,
      }

print(dic1)
print()
print(dic2)

merged = {**dic1, **dic2}

print("Merged Dictionary:", merged)

