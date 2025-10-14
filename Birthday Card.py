import qrcode

message=""" 
Hear ye, hear ye! 
On the fifteenth of May, 
a most charming young jester, 
Weezer Willington, did make their grand debut! 

Let us give thanks 
and make merry in celebration of this wondrous day!  
"""

qr= qrcode.make(message)
qr.save("Birthday_Card.png")
print("Birthday QR code saved as Birthday_Card.png")