from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=15)

file_name = "receipt.txt"

with open(file_name, "w") as f:
    a = f.write("")

f = open(file_name, "a")

f.write("*************************  Template Store  *************************\n\n")
sum = 0
i = 1

while True:
    product_purchased = input(
        "Enter the product name (Press q to print the final bill): \n"
    )

    if product_purchased == "q":
        break

    product_quantity = int(input("Enter the product quantity: \n"))
    product_code = input("Enter the product code: \n")
    product_price = input("Enter the unit price: \n")

    if product_purchased != "q":
        sum = sum + (float(product_price) * product_quantity)
        
        billing = f"{i}. \t {product_purchased} of code {product_code}, quantity of {product_quantity}\n billed {product_price}x{product_quantity} units = \n\t ${float(product_price) * (product_quantity)} "

        f.write(billing + "\n")

        print(billing)

        i += 1

print(f"Order total so far ${sum}")

thnx = (
    f"\n\n!!! Your bill total is only Rs. {sum}. Thanks for shopping with us !!!\n\n"
)

print(thnx)
f.write(thnx)

f.close()

f = open(file_name, "r")

for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align="L")

pdf.output("your-bill.pdf")

f.close()




