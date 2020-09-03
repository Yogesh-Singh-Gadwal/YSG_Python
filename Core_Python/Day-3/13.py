# Dynamic Value 
print('Welcome to Python Store ')
print()
pro1 = float(input('Enter user value-1 : '))
pro2 = float(input('Enter user value-2 : '))
pro3 = float(input('Enter user value-3 : '))
gst = float(input('Enter GST value : '))
print()
total_Product = pro1+pro2+pro3
gst_value = total_Product * gst
total_Amount = total_Product + gst_value 
print()
print('Product-1 Cost is : ',pro1)
print('Product-2 Cost is : ',pro2)
print('Product-3 Cost is : ',pro3)
print()
print('-------------------')
print('Total Amount is : ',total_Product)
print()
print('Gst Tax Value is : ',gst_value)
print()
print('Total Amount With Tax : ',total_Amount)


