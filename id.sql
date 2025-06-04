cart_items = (SELECT product_variant_id, quantity, FROM cart_items
            WHERE user_id = ?,
            session["user_id"])

for cart_item in cart_items:
    product_variant_id = cart_item["product_variant_id"]
    product_id = db.execute(
        """SELECT product_id FROM product_variants WHERE id = ?""", product_variant_id
        )
    product_id = product_id[0]["product_id"]
    row  = db.execute ("""
        SELECT * FROM products WHERE id = ?""",
        product_id
        )
    product_info.append(row[0])


















//////////////old
product_variant_rows = db.execute(
            """SELECT product_variant_id, quantity, FROM cart_items
            WHERE user_id = ?""",
            session["user_id"]
        )

        for row in product_variant_rows:
            variant_info = db.execute(
                """SELECT * FROM product_variants
                WHERE
                id = ?""",
                row["id"]
            )
            product_info =  db.execute(
                """SELECT * FROM product_variants
                WHERE
                id = ?""",
                row["id"]
            )
////////////////
