content = """
College Fee Notice

CS101 fee: Rs. 12000
AI202 fee: Rs. 18000
DS303 fee: Rs. 15000

Merit scholarship: 10%
Hostel lab charges: Rs. 4500
"""

with open("Day_3/big.html", "w", encoding="utf-8") as f:
    f.write("<html><body>")
    
    for i in range(100):
        f.write("<h2>College Fee Notice</h2>")
        f.write("<p>" + content.replace("\n", "<br>") + "</p>")
    
    f.write("</body></html>")

print("big.html created successfully")