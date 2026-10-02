from pyscript import display, document # type: ignore

def SKU_generator(e):
    document.getElementById('sku_output').innerHTML = " "
    category = document.getElementById('category').value
    product_name = document.getElementById('product_name').value
    stock_qty = document.getElementById('quantity').value
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
    display("SKU: " + sku, target='sku_output')

def create_order(e):
    
    p1 = 150  # Bibimbap
    p2 = 120  # Tteokbokki
    p3 = 130  # Kimchi Fried Rice
    p4 = 200  # Bulgogi
    p5 = 140  # Ramen
    p6 = 99   # Sushi
    p7 = 160  # Tempura
    p8 = 110  # Gyoza
    p9 = 35   # Coke
    p10 = 20  # Water

   
    q1 = float(document.getElementById("item1").value or 0)
    q2 = float(document.getElementById("item2").value or 0)
    q3 = float(document.getElementById("item3").value or 0)
    q4 = float(document.getElementById("item4").value or 0)
    q5 = float(document.getElementById("item5").value or 0)
    q6 = float(document.getElementById("item6").value or 0)
    q7 = float(document.getElementById("item7").value or 0)
    q8 = float(document.getElementById("item8").value or 0)
    q9 = float(document.getElementById("item9").value or 0)
    q10 = float(document.getElementById("item10").value or 0)

  
    subtotal = (p1*q1 + p2*q2 + p3*q3 + p4*q4 + p5*q5 + p6*q6 + p7*q7 + p8*q8 + p9*q9 + p10*q10)

    tax_rate = 0.12 # 12% VAT
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt = f"""==== Receipt ====
Subtotal: ₱{subtotal:.2f}
Tax: ₱{tax:.2f}
Total: ₱{total:.2f}
"""

    document.getElementById("show").innerText = receipt





